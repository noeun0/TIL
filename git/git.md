# command

> git 기본 명령어 정리

### 생성

##### init

- 현재 폴더를 git으로 관리하겠다.
- 현재 폴더에 `.git` 폴더를 생성
- 최초 한번만 실행하는 명령어
- 프로젝트 단위에서 실행

```bash
git init
```



### 확인

##### status

- 현재 git 이 관리하고 있는 파일들의 상태를 보여주는 명령어

```bash
git status
```



##### log

- 커밋의 히스토리를 보여주는 명령어

```bash
git log
```



### 관리(로컬)

##### add

- working directory에서 staging area에 파일을 업로드 하는 명령어
  - `.`  : 현재 폴더, 하위 폴더, 하위 파일 모두 의미

```bash
git add <file name>
# git add .
```

##### commit

- staging area에 올라온 파일들을 하나의 커밋으로 만들어주는 (스냅샷 찍는) 명령어

```bash
git commit -m "commit massage"
#-로 시작하는 것은 옵션
```



### 관리(원격)

##### remote add

- 원격 저장소 주소를 로컬에 저장하는 명령어
  - nickname에는 일반적으로 `origin`

```bash
git remote add <nickname> <url>
```



##### push

- 원격 저장소로 로컬의 커밋기록을 업로드 하는 명령어

``` bash
git push <nickname> <branch name>
```



# ERROR

에러 메세지

```
error: src refspec master does not match any.  
error: failed to push some refs to 'https://github.com/xxxxx/xxxxx.git'
```

master 브랜치가 존재하지 않기 때문. master 브랜치를 생성하여 이동 후 푸시를 하면 된다.

```bash
git checkout -b "master"
git push origin master
```





---



### 첫 시작



1. init

```bash
git init
```

2. 변경사항 추가하기

```bash
$ git add README.md
```

3. commit 하기

```bash
$ git commint -m "First"
```

4. 원격저장소와 연결

```bash
$ git branch -M main
$ git remote add origin https://github.com/noeun0/TIL.git
```

5. push

```bash
git push -u origin main
```



---

### 깃랩연결하기

1. touch README.md
2. 깃랩에서 새 프로젝트 생성
3. git init

4. git add .

5. git commit -m "git init"
6. git remote add origin https://lab.ssafy.com/noeun_y/hws.git

7. git push -u origin master

### 깃랩올리는법 push

1. git add .

2. git commit -m 

3. git push origin master



### 깃랩 가져오는 법 pull

1. git pull origin master