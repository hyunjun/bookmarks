---
title: Hermes Agent에 Google Drive를 연결하는 9 STEP
subtitle: Google Cloud 프로젝트 개설부터 Desktop OAuth 인증·파일 검색·다운로드·업로드까지
version: v1.0
created: 2026-09-01
updated: 2026-09-01
status: draft
format: setup-guide
---

> Hermes가 볼트 밖의 파일을 다뤄야 하는 사용자. 백업 ZIP이나 완성 파일을 Google Drive에 올리고 내려받으려는 경우

# 이 연결이 하는 일과 하지 않는 일

Hermes가 사용자가 지정한 Google Drive 파일을 검색·다운로드·업로드할 수 있게 OAuth를 연결합니다. **볼트 동기화가 아닙니다.**

| 역할 | 사용 도구 |
|---|---|
| Obsidian 볼트 양방향 동기화 | Obsidian Headless + Obsidian Sync |
| Hermes가 선택한 Drive 파일 검색·다운로드·업로드 | Google Drive OAuth/API |

Google Drive는 Obsidian Sync를 대체하지 않습니다. 두 도구가 같은 폴더를 동시에 관리하면 서로의 변경을 덮어씁니다.

| 구분 | Obsidian 동기화 | Google Drive 연결 |
|---|---|---|
| 대상 | 볼트 폴더 전체 | 사용자가 지정한 파일 |
| 시점 | 변경이 생기면 자동으로 계속 | 명령을 보낸 그 순간만 |
| 파일이 놓이는 곳 | `/opt/data/vaults/obsidian` | `/tmp/hermes-drive-work` |
| 필수 여부 | 필수 | 선택 |

# 준비물

- [ ] Google 계정 1개
- [ ] Hermes Agent 컨테이너 Terminal 접근(Hostinger Docker Manager)
- [ ] Hermes에 google-workspace 스킬 설치
- [ ] 비밀번호 관리자

> OAuth JSON과 `google_token.json`은 볼트·채팅·Git 저장소에 저장하지 않습니다.

# 명령 실행 위치 표기

- **[노트북]** 내 컴퓨터의 브라우저
- **[Hermes]** Docker Manager → Hermes Agent 프로젝트 → Terminal

# 전체 흐름

```text
Google Cloud 프로젝트 + Drive API 사용 설정
        ↓
Desktop OAuth 클라이언트 생성 → JSON 다운로드
        ↓
Drive에 Hermes Backup 폴더 생성 → 폴더 ID 확보
        ↓
JSON을 /opt/data/.secrets/google-drive/ 에 보관
        ↓
drive 범위만으로 인증 URL 생성 → 브라우저 승인 → 코드 교환
        ↓
검색 → /tmp/hermes-drive-work 로 다운로드 → 승인 뒤 업로드
```

---

## STEP 1. Google Cloud 프로젝트를 만듭니다

**[노트북]**

1. 브라우저에서 [Google Cloud Console](https://console.cloud.google.com/projectselector2/home/dashboard)을 엽니다.
2. 상단 프로젝트 선택 메뉴에서 **새 프로젝트**를 누릅니다.
3. 프로젝트 이름은 `Hermes Drive Backup`처럼 용도를 알 수 있게 적고 만듭니다.
4. 프로젝트가 선택된 상태에서 [API Library](https://console.cloud.google.com/apis/library)를 엽니다.
5. `Google Drive API`를 검색하고 **사용(Enable)**을 누릅니다.

## STEP 2. OAuth 동의 화면과 Desktop 앱을 만듭니다

**[노트북]**

1. [Google Auth Platform → Audience](https://console.cloud.google.com/auth/audience)를 엽니다.
2. 앱이 테스트 상태라면 **Test users**에 실제로 사용할 Google 계정을 추가합니다.
3. [Credentials](https://console.cloud.google.com/apis/credentials)에서 **Create Credentials → OAuth client ID**를 선택합니다.
4. 애플리케이션 유형은 반드시 **Desktop app**을 선택합니다.
5. 이름은 `Hermes VPS Drive`처럼 구분해 만들고 **JSON 다운로드**를 누릅니다.

> JSON 파일에는 OAuth client secret이 들어 있습니다. Telegram, 채팅창, Obsidian 볼트, Git 저장소에 올리지 않습니다.

## STEP 3. Google Drive에 전용 폴더를 만듭니다

**[노트북]**

1. 브라우저에서 Google Drive를 열고 `Hermes Backup` 폴더를 만듭니다.
2. 그 폴더를 열고 주소창에서 `folders/` 뒤의 문자열을 복사합니다. 이 값이 폴더 ID입니다.

```text
Hermes Backup 폴더 ID: ______________________________
```

## STEP 4. JSON 파일을 Hermes 영구 저장소에 보관합니다

**[Hermes]**

```bash
mkdir -p /opt/data/.secrets/google-drive
chmod 700 /opt/data/.secrets/google-drive
```

1. 다운로드한 JSON 파일을 Docker Manager가 제공하는 안전한 업로드 방식으로 `/opt/data/.secrets/google-drive/`에 올립니다.
2. 파일 이름을 확인합니다.

**[Hermes]**

```bash
ls -l /opt/data/.secrets/google-drive/
```

3. 실제 JSON 파일 이름을 아래 명령의 `<다운로드한_JSON_파일명>` 자리에 넣고 권한을 제한합니다.

**[Hermes]**

```bash
chmod 600 /opt/data/.secrets/google-drive/<다운로드한_JSON_파일명>
```

## STEP 5. Drive 범위만으로 OAuth 인증을 시작합니다

아래 명령은 Hermes Agent 컨테이너 Terminal에서 실행합니다. `drive`만 지정하므로 Gmail·Calendar 등 다른 Google 서비스 권한은 요청하지 않습니다.

**[Hermes]**

```bash
GSETUP="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/setup.py"

# 스크립트가 있는지 먼저 확인
ls -l ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/

# 기존 인증 상태를 먼저 확인
$GSETUP --check

# 내려받은 Desktop OAuth JSON 등록
$GSETUP --client-secret /opt/data/.secrets/google-drive/<다운로드한_JSON_파일명>

# Drive 권한만 요청하는 인증 URL 생성
$GSETUP --auth-url --services drive --format json
```

`ls` 결과에 `setup.py`가 없으면 google-workspace 스킬이 설치되지 않은 상태입니다. 스킬을 먼저 설치한 뒤 진행합니다.

마지막 명령이 표시한 `auth_url` 전체를 노트북 브라우저 주소창에 붙여 넣습니다.

## STEP 6. Google 계정 승인과 인증 코드 교환을 마칩니다

**[노트북]**

1. 브라우저에서 Google 계정으로 로그인합니다.
2. 화면에 보이는 Drive 권한 요청을 확인하고 승인합니다.
3. 승인 뒤 주소가 `http://localhost:1/?code=...`로 바뀌며 페이지가 열리지 않아도 정상입니다.
4. **주소 표시줄의 전체 URL**을 복사합니다.

**[Hermes]** 그 URL을 Telegram이나 채팅창이 아니라 컨테이너 터미널에 아래처럼 넣습니다.

```bash
$GSETUP --auth-code "여기에_브라우저_주소창의_전체_URL을_붙여넣기" --format json
$GSETUP --check
```

`AUTHENTICATED`가 표시되면 연결이 끝났습니다. `403 access_denied`가 나오면 Google Cloud Console의 Test users에 현재 Google 계정을 추가한 뒤 새 인증 URL로 다시 진행합니다.

## STEP 7. 작업할 Google Drive 파일을 찾습니다

아래 명령은 파일을 읽기 전용으로 검색합니다. `<검색어>`만 바꿔 실행하고, 결과의 파일명·형식·수정 시각을 보고 작업 대상을 고릅니다.

**[Hermes]**

```bash
GAPI="python ${HERMES_HOME:-$HOME/.hermes}/skills/productivity/google-workspace/scripts/google_api.py"
$GAPI drive search "<검색어>" --max 10
```

## STEP 8. 선택한 파일만 임시 작업 경로로 내려받습니다

검색 결과에서 선택한 파일 ID를 `<FILE_ID>`에 넣습니다. 이 명령은 Obsidian 볼트가 아닌 `/tmp/hermes-drive-work/`에만 파일을 내려받습니다.

**[Hermes]**

```bash
mkdir -p /tmp/hermes-drive-work
$GAPI drive download <FILE_ID> \
  --output /tmp/hermes-drive-work/<작업할_파일명>
ls -lh /tmp/hermes-drive-work/<작업할_파일명>
```

다운로드한 파일을 Hermes가 읽거나 수정해야 하면, 파일 경로와 할 작업을 Desktop 대화 세션 또는 Telegram에서 명시적으로 요청합니다.

## STEP 9. 결과 파일은 승인 뒤에만 Google Drive에 올립니다

업로드 전에는 대상 파일·Google Drive 폴더·업로드 파일명을 먼저 확인합니다. `<대상_폴더_ID>`는 STEP 3에서 적어 둔 `Hermes Backup` 폴더 ID입니다.

**[Hermes]**

```bash
$GAPI drive upload /tmp/hermes-drive-work/<결과_파일명> \
  --name "<Google_Drive에_표시할_파일명>" \
  --parent <대상_폴더_ID>
```

> 이 명령은 새 파일을 업로드합니다. 기존 파일을 바꾸거나 삭제하지 않습니다. 기존 파일 덮어쓰기·공유 설정 변경·삭제는 별도 요청과 확인이 있어야 합니다.

# 작업 규칙

```text
Obsidian 볼트 동기화: Obsidian Headless + Obsidian Sync만 사용
Google Drive 사용 방식: 사용자가 선택한 파일만 검색·다운로드·업로드
기본 다운로드 위치: /tmp/hermes-drive-work/
금지: Google Drive 데스크톱 동기화 앱을 VPS 볼트 경로에 연결
금지: OAuth JSON·google_token.json을 볼트·채팅·Git에 저장
```

# 전체 점검

- [ ] Desktop OAuth 클라이언트를 만들고 Drive 범위로 인증을 마쳤습니다.
- [ ] `Hermes Backup` 폴더 ID를 적어 두었습니다.
- [ ] 시험 파일 업로드와 다운로드를 확인했습니다.

# 참고

- 같은 폴더의 [[Hermes Agent VPS hosting 구축 가이드 — 호스팅·AI 모델·텔레그램·슬랙]] PART 5와 짝을 이룹니다
- 볼트 동기화는 [[Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP]]을 사용합니다
- Drive 폴더를 통째로 동기화해야 한다면 `rclone bisync`를 VPS 호스트에 별도로 구성합니다. 볼트 경로가 아닌 전용 작업 폴더에만 연결합니다
