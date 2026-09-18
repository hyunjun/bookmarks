---
title: Hermes Agent에 Slack을 연결하는 6 STEP
subtitle: Slack 앱 매니페스트 생성부터 두 토큰 발급·Hermes 입력·게이트웨이 재시작·DM과 채널 테스트까지
version: v1.0
created: 2026-09-01
updated: 2026-09-01
status: draft
format: setup-guide
---

> Hermes Agent를 VPS에서 운영 중이고, Telegram에 이어 Slack을 명령 창구로 추가하려는 사용자

# 이 가이드에 대하여

Slack 연결은 Telegram보다 손이 많이 갑니다. 토큰이 두 개이고, 권한 스코프 14개와 이벤트 5개를 설정해야 합니다. 체크박스를 하나씩 누르면 누락이 생기므로 이 가이드는 **앱 매니페스트 붙여넣기**로 한 번에 처리합니다.

메신저 게이트웨이는 Hermes 서버와 별개 프로세스로 VPS에서 실행됩니다. 노트북 Hermes Desktop을 종료해도 Slack 응답은 유지됩니다. Desktop은 설정 화면 역할만 합니다.

# 준비물

- 앱을 설치할 Slack 워크스페이스와 설치 권한
- VPS에서 실행 중인 Hermes Agent
- 노트북의 Hermes Desktop (Remote Gateway 연결 상태)
- 비밀번호 관리자

> 회사 워크스페이스라면 설치 시 관리자 승인 화면이 뜹니다. 승인 전까지 STEP 3에서 멈춥니다.

# 명령 실행 위치 표기

- **[노트북]** 내 컴퓨터의 브라우저 또는 Hermes Desktop
- **[Slack]** Slack 앱 화면
- **[Hermes]** VPS 컨테이너 터미널

---

## STEP 1. 매니페스트로 Slack 앱을 만듭니다

### 목표

스코프·이벤트·Socket Mode·Messages Tab을 한 번에 적용한 앱을 만듭니다.

### 기존 Hermes 앱과의 관계

Slack은 앱이 다르면 같은 워크스페이스에 여러 개가 공존합니다. 이전 서버가 쓰는 Hermes 앱을 지우거나 끌 필요가 없습니다.

다만 하나의 앱(토큰)을 두 서버가 Socket Mode로 동시에 연결하면 이벤트가 두 서버로 갈립니다. 새 서버에는 반드시 새 앱을 만듭니다.

### 먼저 확인할 것: 이름 중복

워크스페이스에 같은 이름의 Hermes 앱이 여러 개 있으면 App ID로만 구분됩니다. 새 앱 이름에는 **어느 서버용인지**를 넣습니다.

```text
Hermes Hostinger
```

### 실행

**[노트북]**

1. https://api.slack.com/apps 에 접속해 로그인합니다.
2. **Create New App**을 누릅니다. 기존 앱을 클릭하지 않습니다.
3. **From an app manifest**를 고릅니다.
4. 설치할 워크스페이스를 선택하고 **Next**를 누릅니다.
5. 입력창의 기본 내용을 모두 지우고 아래를 붙여넣습니다.

```yaml
display_information:
  name: Hermes Hostinger
  description: Hermes Agent gateway on Hostinger VPS
features:
  bot_user:
    display_name: Hermes Hostinger
    always_online: true
  app_home:
    home_tab_enabled: false
    messages_tab_enabled: true
    messages_tab_read_only_enabled: false
oauth_config:
  scopes:
    bot:
      - app_mentions:read
      - channels:history
      - channels:read
      - chat:write
      - files:read
      - files:write
      - groups:history
      - groups:read
      - im:history
      - im:read
      - im:write
      - mpim:history
      - mpim:read
      - users:read
settings:
  event_subscriptions:
    bot_events:
      - app_mention
      - message.channels
      - message.groups
      - message.im
      - message.mpim
  interactivity:
    is_enabled: false
  org_deploy_enabled: false
  socket_mode_enabled: true
  token_rotation_enabled: false
```

6. **Next** → 요약 확인 → **Create**를 누릅니다.

이름을 바꿀 때는 `name`과 `display_name` 두 줄만 같은 값으로 고칩니다. 나머지는 그대로 둡니다.

### 결과 확인

- [ ] 앱이 생성되었고 이름에 서버 구분이 들어갔습니다.
- [ ] OAuth & Permissions에 bot scope 14개가 들어가 있습니다.
- [ ] Event Subscriptions에 bot event 5개가 들어가 있습니다.
- [ ] Socket Mode가 켜져 있습니다.

---

## STEP 2. App-Level Token(`xapp-`)을 발급합니다

### 목표

Socket Mode 연결용 토큰을 받습니다. 봇 토큰과는 별개입니다.

### 실행

**[노트북]**

1. 만든 앱에서 **Settings → Basic Information**을 엽니다.
2. 아래로 내려 **App-Level Tokens** 섹션을 찾습니다.
3. **Generate Token and Scopes**를 누릅니다.
4. Token Name에 `socket`을 입력합니다.
5. **Add Scope**에서 `connections:write`를 고릅니다.
6. **Generate**를 누릅니다.

> 이 토큰은 화면을 닫으면 다시 볼 수 없습니다. 즉시 복사해 비밀번호 관리자에 저장합니다. 놓치면 새로 발급해야 합니다.

### 결과 확인

- [ ] `xapp-`로 시작하는 토큰을 확보했습니다.
- [ ] 스코프는 `connections:write` 하나입니다.
- [ ] 비밀번호 관리자에 저장했습니다.

---

## STEP 3. 워크스페이스에 설치하고 Bot Token(`xoxb-`)을 받습니다

### 목표

앱을 워크스페이스에 설치하고 봇 토큰을 확보합니다.

### 실행

**[노트북]**

1. **Settings → Install App**을 엽니다.
2. **Install to Workspace**를 누릅니다.
3. 권한 요청 화면에 스코프 14개가 표시되는지 확인합니다.
4. **Allow**를 누릅니다.
5. 표시되는 **Bot User OAuth Token**을 복사합니다.

`xoxb-` 토큰은 **OAuth & Permissions**에서 언제든 다시 볼 수 있습니다. `xapp-`와 달리 한 번만 보이는 값이 아닙니다.

### 두 토큰 구분

| 토큰 | 접두어 | 확인 위치 | Hermes 입력 칸 |
|---|---|---|---|
| App-Level Token | `xapp-` | Basic Information | Slack app token |
| Bot User OAuth Token | `xoxb-` | OAuth & Permissions | Slack bot token |

### 결과 확인

- [ ] 워크스페이스 설치를 마쳤습니다.
- [ ] `xoxb-`로 시작하는 토큰을 확보했습니다.
- [ ] 두 토큰을 접두어로 구분해 따로 보관했습니다.

---

## STEP 4. 본인 Slack Member ID를 확인합니다

### 목표

허용 목록에 넣을 `U`로 시작하는 ID를 확보합니다.

### 실행

**[Slack]** api.slack.com이 아니라 Slack 앱에서 합니다.

1. 아무 대화방에서 본인 이름이나 프로필 사진을 누릅니다.
2. 프로필 패널에서 **더보기(⋮)**를 누릅니다.
3. **Copy member ID**를 고릅니다.

메뉴가 없으면 브라우저용 Slack에서 본인 프로필을 열고 주소창 끝의 `U`로 시작하는 값을 씁니다.

### 값 구분

| 값 | 형태 | 용도 |
|---|---|---|
| Member ID | `U01ABC2DEF3` | 허용 목록에 넣을 값 |
| 표시 이름 | 홍길동 | 사용하지 않음 |
| 핸들 | `@hong` | 사용하지 않음 |
| 채널 ID | `C01234567890` | 홈 채널 지정용, 선택 사항 |

### 결과 확인

- [ ] `U`로 시작하는 Member ID를 확보했습니다.
- [ ] 표시 이름이나 핸들이 아닌 숫자·영문 조합 ID입니다.

---

## STEP 5. Hermes에 입력하고 활성화합니다

### 목표

세 값을 등록하고 Slack 커넥터를 켭니다.

### 실행

**[노트북]** Hermes Desktop 좌측 메뉴에서 **Messaging**을 열고 **Slack**을 고릅니다.

1. **Slack bot token** 칸에 `xoxb-` 값을 붙여넣습니다.
2. **Slack app token** 칸에 `xapp-` 값을 붙여넣습니다.
3. **Allowed Slack user IDs** 칸에 Member ID를 넣습니다. 여러 명은 공백 없이 쉼표로 잇습니다.

```text
U01ABC2DEF3,U04XYZ9GHI7
```

4. 화면 우측 하단 **토글**을 켭니다.
5. **Save changes** 버튼을 누릅니다.

> Telegram 화면은 자동 저장이지만 Slack 화면은 저장 버튼을 눌러야 반영됩니다.

### 배지 판정

| 배지 | 의미 |
|---|---|
| `Disabled` 사라짐 | 토글이 켜졌습니다 |
| `Needs setup` 사라짐 | 세 값이 형식 검증을 통과했습니다 |
| `Restart needed` 등장 | 정상입니다. 다음 단계에서 재시작합니다 |

`Needs setup`이 남아 있으면 두 토큰을 서로 바꿔 넣었을 가능성이 큽니다. 접두어를 다시 확인합니다.

### 결과 확인

- [ ] 세 칸을 모두 채웠습니다.
- [ ] 토글을 켜고 **Save changes**를 눌렀습니다.
- [ ] `Disabled`와 `Needs setup` 배지가 사라졌습니다.

---

## STEP 6. 게이트웨이를 재시작하고 시험합니다

### 목표

설정을 적용하고 DM과 채널에서 응답을 확인합니다.

### 실행

#### 1. 재시작

**[노트북]** Hermes Desktop 하단 상태 표시줄에서 게이트웨이 상태를 누르고 **Restart**를 실행합니다. `Restart needed` 배지가 사라지면 완료입니다.

재시작 전에는 설정이 적용되지 않습니다.

#### 2. DM 시험

**[Slack]** 좌측 목록의 **앱(Apps)**에서 만든 봇을 열고 메시지를 보냅니다.

```text
현재 사용 중인 모델 이름과 연결 상태만 알려줘.
```

응답이 오면 Socket Mode 연결과 봇 토큰이 모두 정상입니다.

#### 3. 채널 시험

봇은 초대된 채널에서만 반응합니다.

```text
/invite @Hermes Hostinger
```

초대 후 멘션으로 호출합니다.

```text
@Hermes Hostinger 지금 연결 상태 알려줘
```

#### 4. 명령 시험

```text
/status
/model
/help
```

### 응답이 없을 때

| 증상 | 원인 | 조치 |
|---|---|---|
| DM 무응답 | 게이트웨이 미재시작 | `Restart needed` 배지 확인 |
| DM 무응답 | Member ID 불일치 | `U` 시작 여부와 오타 확인 |
| DM 입력창 없음 | Messages Tab 꺼짐 | App Home → Messages Tab 켜기 |
| 채널만 무응답 | 봇 미초대 | `/invite` 실행 |
| 연결 자체 실패 | 두 토큰 뒤바뀜 | `xoxb`/`xapp` 위치 확인 |
| 특정 기능만 실패 | 스코프 누락 | 스코프·이벤트 변경 후 앱 재설치 |

> 스코프나 이벤트를 바꾸면 **반드시 앱을 재설치**해야 반영됩니다.

### 결과 확인

- [ ] 게이트웨이를 재시작해 `Restart needed` 배지가 사라졌습니다.
- [ ] 허용된 본인 계정 DM에서 응답을 받았습니다.
- [ ] 채널에 봇을 초대하고 멘션으로 응답을 받았습니다.
- [ ] `/status`, `/model`, `/help`가 작동합니다.

---