---
title: "옵시디언 헤드리스"
tags: [Obsidian, Headless, Hermes, VPS, Sync]
status: active
---

# 옵시디언 헤드리스

VPS의 Hermes Docker 컨테이너에서 Obsidian Headless를 설치하고 원격 Vault를 연결하는 절차를 정리한 운영 노트다.

## 현재 환경

- 컨테이너: `hermes-agent-tknh-hermes-agent-1`
- Hermes 데이터 경로: `/opt/data`
- Hermes 사용자 홈: `/opt/data/home`
- Obsidian Headless 실행 파일: `/opt/data/home/.local/bin/ob`
- 로컬 Vault: `/opt/data/vaults/obsidian`
- 원격 Vault: `hongss`
- 장치 이름: `hermes-vps`

## 단계별 진행 상태

| 단계 | 작업 | 실제 상태 |
|---:|---|---|
| 1 | Hermes 사용자 환경 설정 | 완료 |
| 2 | Node.js/npm 확인 및 Obsidian Headless 설치·검증 | 완료 |
| 3 | Obsidian 계정 로그인 | 완료 |
| 4 | 원격 Vault 목록 조회 | 완료 |
| 5 | 로컬 경로 생성 및 원격 Vault 연결 | 완료 |
| 6 | 동기화 모드 및 충돌 정책 설정 | 완료 |
| 7 | 최초 동기화 및 상태 확인 | 완료 |
| 8 | Hermes Agent에 Vault 경로 등록 | 완료 |
| 9 | Hermes Agent 읽기 검증 | 완료 |
| 10 | 노트 생성·쓰기 및 원격 업로드 검증 | 완료 |
| 11 | s6 자동 연속 동기화 및 watchdog 구성 | 완료 |
| 12 | 권한·디스크·운영 상태 점검 | 기본 점검 완료 |

> 12단계의 독립 외부 백업, 복원 테스트, 실제 컨테이너 재시작 테스트는 별도 저장소와 유지보수 시간이 필요한 후속 선택 작업이다.

## 1단계: Hermes 사용자 환경 설정

컨테이너 프롬프트가 `root@...#`인 경우 Hermes 사용자로 전환한다.

```bash
su -s /bin/bash hermes
```

환경변수를 설정한다.

```bash
export HOME=/opt/data/home
export PATH="$HOME/.local/bin:$PATH"
```

확인:

```bash
whoami
echo "$HOME"
```

정상값:

```text
hermes
/opt/data/home
```

이미 프롬프트가 `hermes@...$`이면 `su`는 다시 실행하지 않는다.

## 2단계: Node.js/npm 확인 및 Obsidian Headless 설치·검증

```bash
node --version
npm --version
command -v ob
```

Obsidian Headless는 Node.js 22 이상이 필요하다.

설치되지 않은 경우:

```bash
mkdir -p "$HOME/.local"
npm install --global --prefix "$HOME/.local" obsidian-headless
export PATH="$HOME/.local/bin:$PATH"
```

검증:

```bash
ob --version
ob sync-list-local --json
```

## 3단계: Obsidian 계정 로그인 및 인증 확인

실행 위치는 Hermes 컨테이너 내부의 `hermes` 사용자 셸이다.

```text
hermes@ae3858ce9921:/opt/hermes$
```

로그인 전에 사용자와 HOME을 확인한다.

```bash
whoami
echo "$HOME"
```

정상값:

```text
hermes
/opt/data/home
```

로그인:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob login
```

터미널에서 다음 항목을 입력한다.

```text
Email:
Password:
MFA code:  # 2단계 인증을 사용하는 경우
```

비밀번호·MFA·E2EE 암호는 채팅이나 문서에 기록하지 않는다. 비밀번호 입력 문자가 보이지 않는 것은 정상이다. Obsidian Headless Sync를 사용하려면 계정에 활성화된 Obsidian Sync 구독과 접근 가능한 원격 Vault가 있어야 한다.

로그인 성공 기준:

```text
Logged in as <사용자 이름> (<이메일>)
```

인증 정보는 `HOME=/opt/data/home` 기준으로 저장되어야 Hermes Agent와 자동 동기화 서비스가 함께 사용할 수 있다.

## 4단계: 원격 Vault 목록 조회

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-list-remote --json
```

확인 항목:

- `id`: 연결에 사용할 원격 Vault ID
- `name`: 원격 Vault 이름
- `region`: 동기화 서버 리전
- `shared`: 공유 Vault 목록

실제 확인 결과:

```text
Vault 이름: hongss
리전: Asia
공유 Vault: 없음
```

Vault 이름이 중복될 수 있으므로 `sync-setup`에는 이름보다 ID를 사용하는 것이 안전하다. 외부 공유 문서에서는 Vault ID와 계정 정보를 가린다.

다음 오류가 나오면 현재 HOME에 로그인 정보가 없는 것이다.

```text
No account logged in. Run "ob login" first.
```

이 경우 3단계의 절대 경로 로그인 명령을 다시 실행한다.

## 5단계: 로컬 경로 생성 및 원격 Vault 연결

로컬 Vault 경로를 만들고 권한을 확인한다.

```bash
mkdir -p /opt/data/vaults/obsidian
stat -c '%A %U:%G %n' /opt/data/vaults/obsidian
```

정상 소유자:

```text
hermes:hermes
```

기존 파일과의 충돌을 막기 위해 최초 연결 전 디렉터리가 비어 있는지 확인한다.

```bash
find /opt/data/vaults/obsidian \
  -mindepth 1 \
  -maxdepth 1 \
  -print
```

아무것도 출력되지 않으면 빈 디렉터리다. 기존 파일이 있다면 별도 백업 후 연결한다.

원격 Vault 연결:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-setup \
  --vault "<VAULT_ID>" \
  --path /opt/data/vaults/obsidian \
  --device-name "hermes-vps"
```

원격 Vault가 E2EE를 사용하면 `Encryption password:`가 나타난다. 이 암호는 계정 비밀번호와 다를 수 있으며 터미널에만 입력한다.

연결 확인:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-list-local --json
```

상태 확인:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-status \
  --path /opt/data/vaults/obsidian
```

완료 기준:

- 원격 Vault `hongss`가 등록됨
- 로컬 경로가 `/opt/data/vaults/obsidian`으로 표시됨
- 장치 이름이 `hermes-vps`로 표시됨

## 6단계: 동기화 모드 및 충돌 정책 설정

Hermes Agent가 노트를 읽고 수정한 뒤 다시 업로드해야 하므로 양방향 동기화를 명시한다.

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-config \
  --path /opt/data/vaults/obsidian \
  --mode bidirectional \
  --conflict-strategy merge \
  --device-name "hermes-vps"
```

설정 의미:

- `bidirectional`: 원격→VPS 및 VPS→원격 양방향 동기화
- `merge`: 같은 Markdown 파일이 양쪽에서 바뀌면 가능한 범위에서 병합
- `hermes-vps`: Obsidian Sync 버전 기록에 표시할 장치 이름

읽기 전용 서버라면 `pull-only`, 원격 상태를 강제로 미러링하려면 `mirror-remote`를 사용할 수 있지만, Hermes가 노트를 수정하는 현재 목적에는 `bidirectional`이 적합하다.

설정 확인:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-config \
  --path /opt/data/vaults/obsidian
```

현재 운영 설정:

```text
Sync mode: bidirectional
Conflict strategy: merge
Device name: hermes-vps
File types: image, audio, pdf, video
Configs: none (config syncing disabled)
```

Markdown 노트와 지정된 첨부파일은 동기화하지만, VPS에는 필요하지 않은 Obsidian 앱·테마·플러그인 설정은 동기화하지 않는다.

## 7단계: 최초 1회 동기화 및 상태 확인

최초 1회 동기화:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync \
  --path /opt/data/vaults/obsidian
```

이 명령은 현재 변경분을 비교해 다운로드·업로드한 후 종료한다. 최초 실행에서는 Vault 크기에 따라 많은 파일과 첨부파일을 내려받아 오래 걸릴 수 있다.

동기화 범위:

- Markdown 노트와 폴더 구조
- 이미지, 오디오, PDF, 비디오
- 생성·수정·삭제 변경 사항
- `.obsidian` 앱 설정은 현재 구성에서 제외

상태 확인:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync-status \
  --path /opt/data/vaults/obsidian
```

진행 중인 동기화를 안전하게 중지하려면 해당 터미널에서 `Ctrl+C`를 누른다. 강제 종료인 `kill -9`는 가급적 사용하지 않는다. 중지해도 연결 설정과 완료된 파일은 유지되며 다음 실행에서 이어서 처리한다.

다운로드된 Markdown 노트 확인:

```bash
find /opt/data/vaults/obsidian \
  -type f \
  -name '*.md' \
  -print
```

현재 운영 환경에서는 이후 연속 동기화가 초기 다운로드를 마쳤고 로그에서 `Fully synced`가 확인됐다.

## 8단계: Hermes Agent에 Vault 경로 등록

중복 등록을 피하기 위해 먼저 설정 존재 여부를 확인한다.

```bash
grep '^OBSIDIAN_VAULT_PATH=' /opt/data/.env
```

아무것도 출력되지 않을 때만 `/opt/data/.env`에 값을 한 번 추가한다.

```bash
printf '\nOBSIDIAN_VAULT_PATH=/opt/data/vaults/obsidian\n' >> /opt/data/.env
```

등록 확인:

```bash
grep '^OBSIDIAN_VAULT_PATH=' /opt/data/.env
```

정상 결과:

```text
OBSIDIAN_VAULT_PATH=/opt/data/vaults/obsidian
```

현재 SSH 셸에도 적용한다.

```bash
export OBSIDIAN_VAULT_PATH=/opt/data/vaults/obsidian
echo "$OBSIDIAN_VAULT_PATH"
```

Vault 경로 확인:

```bash
test -d "$OBSIDIAN_VAULT_PATH" \
  && echo "Vault 경로 정상" \
  || echo "Vault 경로 없음"
```

`.env`에는 API 키 등 비밀정보가 있을 수 있으므로 파일 전체를 출력하거나 공유하지 않는다. 새 Hermes 프로세스는 `.env`를 읽으며, 현재 대화 중인 Gateway 재시작은 모든 설정 작업이 끝난 뒤 수행해도 된다.

## 9단계: Hermes Agent 읽기 검증

Hermes Agent에서 Vault의 Markdown 파일을 검색하고 기존 노트 하나를 읽는다. 이 단계에서는 파일을 생성·수정·삭제하지 않는다.

실제 읽기 검증에 사용한 노트:

```text
10 외부 강의/00 일정별 강의/2026-07/
0709목 경상국립대학교 - 4차/실습자료/LLM위키·지식관리/
LLM 위키 활용과 원소스 멀티유즈/
LLM 위키 활용과 원소스 멀티유즈.md
```

검증 항목:

- 한글 파일명과 긴 경로
- YAML 프런트매터
- Markdown 본문
- 체크박스와 목록
- `[[위키링크]]`
- 읽기 권한

실제 결과:

- 60줄의 한글 Markdown 본문 읽기 성공
- YAML 제목·날짜·태그·상태 인식 성공
- 10개 하위 주제 위키링크 인식 성공
- 생성·수정·삭제 없음

## 10단계: 노트 생성·쓰기 및 원격 업로드 검증

현재 검증 노트의 최종 파일명:

```text
/opt/data/vaults/obsidian/Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md
```

파일 확인:

```bash
test -f '/opt/data/vaults/obsidian/Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md' \
  && echo "노트 생성 확인" \
  || echo "노트 없음"
```

수동 동기화로 검증할 경우:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync \
  --path /opt/data/vaults/obsidian
```

11단계의 연속 동기화가 실행 중인 현재 상태에서는 수동 `ob sync`를 동시에 실행하지 않는다. 자동 로그에서 업로드를 확인한다.

```bash
grep -F 'Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md' \
  /opt/data/logs/obsidian-sync/current
```

파일명 변경 동기화 결과:

```text
Push: 옵시디언 헤드리스.md (deleted)
Deleting 옵시디언 헤드리스.md
Push: Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md (updated)
Downloaded Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md
Accepted Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP.md
Fully synced
```

최종 독립 검증은 데스크톱 또는 모바일 Obsidian의 `hongss` Vault에서 `Hermes Agent 옵시디언 헤드리스 연결 — 12 STEP` 노트를 열어 내용이 보이는지 확인하는 것이다.

## 11단계: s6 자동 연속 동기화 구성

Hermes Docker 컨테이너 내부의 s6가 Obsidian Headless를 상시 실행하고, 프로세스가 종료되면 다시 시작하도록 구성한다.

현재 실행 명령:

```bash
HOME=/opt/data/home \
  /opt/data/home/.local/bin/ob sync \
  --path /opt/data/vaults/obsidian \
  --continuous
```

### s6 서비스 정의

영구 데이터 영역에 다음 서비스 파일을 둔다.

```text
/opt/data/services/obsidian-sync/run
/opt/data/services/obsidian-sync/log/run
```

`/opt/data/services/obsidian-sync/run`:

```sh
#!/bin/sh
exec 2>&1
export HOME=/opt/data/home
export PATH=/opt/data/home/.local/bin:/usr/local/bin:/usr/bin:/bin
exec /command/s6-setuidgid hermes \
  /opt/data/home/.local/bin/ob sync \
  --path /opt/data/vaults/obsidian \
  --continuous
```

`/opt/data/services/obsidian-sync/log/run`:

```sh
#!/bin/sh
exec /command/s6-setuidgid hermes \
  /command/s6-log n10 s1000000 /opt/data/logs/obsidian-sync
```

서비스와 로그 디렉터리를 준비하고 실행 권한을 설정한다.

```bash
mkdir -p /opt/data/logs/obsidian-sync
chmod 755 \
  /opt/data/services/obsidian-sync/run \
  /opt/data/services/obsidian-sync/log/run
```

영구 서비스 정의를 s6 실행 디렉터리에 연결한다.

```bash
ln -s /opt/data/services/obsidian-sync \
  /run/service/obsidian-sync
/command/s6-svscanctl -a /run/service
```

이미 링크가 있으면 `ln`을 다시 실행하지 않는다.

실행 서비스 연결:

```text
/run/service/obsidian-sync
→ /opt/data/services/obsidian-sync
```

서비스는 `hermes` 사용자 권한으로 실행한다. 수동 `ob sync`와 연속 동기화 서비스를 같은 Vault에서 동시에 실행하지 않는다.

프로세스 확인:

```bash
pgrep -af '^node /opt/data/home/.local/bin/ob sync'
```

정상 결과에는 다음 인자가 포함된다.

```text
--path /opt/data/vaults/obsidian --continuous
```

s6 상태 파일은 일반 `hermes` 사용자에게 읽기 권한이 제한될 수 있으므로, 실제 프로세스와 로그를 함께 확인한다.

### 영구 로그

로그 위치:

```text
/opt/data/logs/obsidian-sync/current
```

로그는 1MB 단위, 최대 10개로 회전하도록 설정했다.

최근 상태 확인:

```bash
grep -E 'Connection successful|Fully synced|Sync failed|Disconnected' \
  /opt/data/logs/obsidian-sync/current
```

특정 노트 업로드 확인:

```bash
grep -F '옵시디언 헤드리스.md' \
  /opt/data/logs/obsidian-sync/current
```

### 컨테이너 재시작 후 서비스 복원

복원 스크립트:

```text
/opt/data/scripts/ensure_obsidian_sync_service.py
```

스크립트의 역할:

1. `/opt/data/services/obsidian-sync` 영구 정의가 존재하는지 확인
2. `/run/service/obsidian-sync` 링크가 없으면 다시 생성
3. `/command/s6-svscanctl -a /run/service`로 s6 재스캔 요청
4. 정상일 때는 출력하지 않음

수동 검증:

```bash
python3 /opt/data/scripts/ensure_obsidian_sync_service.py
echo "$?"
```

정상 종료 코드는 `0`이다.

Hermes의 no-agent cron이 1분마다 스크립트를 실행한다.

```text
이름: Obsidian sync service watchdog
주기: every 1m
반복: forever
방식: no_agent
전달: local
```

확인:

```bash
hermes cron list
```

완료 기준:

```text
state: scheduled
enabled: true
last_status: ok
repeat: forever
```

watchdog은 LLM을 호출하지 않으며 정상 상태에서는 출력이나 알림을 보내지 않는다. 컨테이너 재시작 후 최대 1분 안에 서비스 링크 복원을 시도한다.

### 별도 Docker 서비스는 필요하지 않음

현재 구조에서는 Docker Manager에 별도의 `obsidian-headless-service` 컨테이너를 추가할 필요가 없다.

```text
Hermes Docker 컨테이너
└── s6
    └── Obsidian Headless continuous sync
```

같은 Vault에 Hermes 내부 서비스와 별도 Docker 서비스를 동시에 실행하면 안 된다. 두 클라이언트가 같은 경로를 동기화하면 파일 충돌과 동기화 상태 잠금이 발생할 수 있다.

11단계 완료 기준:

- `ob sync --continuous` 프로세스 실행
- `Connection successful` 확인
- `Fully synced` 확인
- s6 자동 재시작 구성
- 영구 로그 구성
- 재시작 복원 watchdog 등록

## 12단계: 백업·권한·운영 상태 최종 점검

Obsidian Sync는 동기화 서비스이지 독립적인 백업이 아니다. 잘못된 수정이나 삭제도 다른 장치로 전달되므로 Vault와 분리된 백업이 필요하다.

### 디스크와 Vault 크기

```bash
df -h /opt/data
du -sh /opt/data/vaults/obsidian
```

점검 당시 상태:

```text
디스크 전체: 96GB
사용: 8.7GB
여유: 88GB
Vault 크기: 2.1GB
```

### 권한 점검

```bash
stat -c '%A %U:%G %n' \
  /opt/data/vaults/obsidian \
  /opt/data/services/obsidian-sync \
  /opt/data/logs/obsidian-sync
```

각 경로의 소유자는 `hermes:hermes`여야 한다.

### 자동 동기화 상태

```bash
pgrep -af '^node /opt/data/home/.local/bin/ob sync'
```

최근 오류 점검:

```bash
grep -E 'Sync failed|Disconnected' \
  /opt/data/logs/obsidian-sync/current
```

최근 정상 상태:

```bash
grep -F 'Fully synced' \
  /opt/data/logs/obsidian-sync/current
```

### 독립 백업 정책

백업은 다음 경로 안에 만들지 않는다.

```text
/opt/data/vaults/obsidian
```

권장 백업 대상:

- Backblaze B2
- AWS S3 또는 S3 호환 스토리지
- 별도 VPS
- NAS
- 별도 외장 디스크나 서버 볼륨

권장 보존 정책:

```text
일간 7개
주간 4개
월간 12개
```

권장 백업 대상 경로:

```text
/opt/data/vaults/obsidian
/opt/data/services/obsidian-sync
/opt/data/scripts/ensure_obsidian_sync_service.py
/opt/data/cron
```

`/opt/data/.env`에는 비밀정보가 있으므로 암호화된 백업에만 포함한다.

### 복원 테스트

백업은 원본 Vault가 아닌 별도 경로에 복원해 검증한다.

```text
/opt/data/restore-test/obsidian
```

검증 항목:

- Markdown 파일 존재
- 한글 파일명 보존
- 첨부파일 존재
- YAML 프런트매터 정상
- 원본 Vault를 덮어쓰지 않음

### 컨테이너 재시작 테스트

VPS 호스트에서 유지보수 시간에 실행한다.

```bash
docker restart hermes-agent-tknh-hermes-agent-1
```

재시작 약 1분 후 자동 동기화 프로세스와 로그를 확인한다.

```bash
docker exec hermes-agent-tknh-hermes-agent-1 \
  pgrep -af '/opt/data/home/.local/bin/ob sync'
```

```bash
docker exec hermes-agent-tknh-hermes-agent-1 \
  grep -E 'Connection successful|Fully synced|Sync failed' \
  /opt/data/logs/obsidian-sync/current
```

### 12단계 현재 상태

- 디스크 공간: 정상
- Vault 권한: 정상
- 자동 동기화: 정상
- watchdog 최근 실행: 정상
- 독립 외부 백업: 미구성
- 백업 복원 테스트: 미실행
- 컨테이너 재시작 테스트: 미실행

## 다음 작업

- 외부 백업 대상 선택 및 암호화 백업 구성
- 백업 복원 테스트
- 유지보수 시간에 컨테이너 재시작 후 자동 복원 확인

## 운영 명령 모음

### 원격 Vault 조회

```bash
HOME=/opt/data/home /opt/data/home/.local/bin/ob sync-list-remote --json
```

### 로컬 Vault 조회

```bash
HOME=/opt/data/home /opt/data/home/.local/bin/ob sync-list-local --json
```

### 1회 동기화

```bash
HOME=/opt/data/home /opt/data/home/.local/bin/ob sync --path /opt/data/vaults/obsidian
```

### 연속 동기화

```bash
HOME=/opt/data/home /opt/data/home/.local/bin/ob sync --path /opt/data/vaults/obsidian --continuous
```

### 상태 확인

```bash
HOME=/opt/data/home /opt/data/home/.local/bin/ob sync-status --path /opt/data/vaults/obsidian
```
