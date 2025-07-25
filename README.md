# 🐍 Python 기초 학습 커리큘럼

## 📖 소개
이 저장소는 **Python의 기초 개념을 단위 테스트 방식으로 학습하는 커리큘럼**입니다.  
각 학습 단원은 `unittest`를 활용한 테스트 코드로 구성되어 있으며, **직접 코드를 작성하고 실행하며 학습할 수 있도록 설계되었습니다.**
중요도와 과정은 제가 스스로 공부하면서 중요하다고 생각하던 부분들을 포함시키고, 점차 수정해 나가고 있습니다.

## 🛠️ 학습 방식
기본적으로 이 프로젝트는 [PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)을 기반으로 만들어졌습니다.
따라서 이 학습에 [PyCharm](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)을 사용하시는 것을 추천드립니다.
- 각 디렉토리에는 Python 기초 개념을 익힐 수 있는 **학습 단원**이 포함되어 있습니다.
- 학습 단원 안에는 과정을 설명하는 `course.md`가 있습니다.
- `unittest` 기반으로 테스트를 실행하며, 학습자가 직접 `TODO` 부분을 채우면서 학습하는 방식입니다.
- `complete` 폴더에 있는 코드는 정답 코드로, 학습 후 비교할 수 있습니다. (v2.0에서 solution으로 수정되었습니다.)
- ※ 절대 solution의 코드가 유일한 정답이 아닙니다. 이런 방식도 있다 라고 참고하고 넘어가주시면 감사하겠습니다.

## 파이썬 버전
`3.9.7`

- 각 패키지 파일에는 Python 기초 개념을 익힐 수 있는 **학습 단원**이 포함되어 있습니다.
- `unittest` 기반으로 테스트를 실행하며, 학습자가 직접 `TODO` 부분을 채우면서 학습하는 방식입니다.
- `complete` 폴더에 있는 코드는 정답 코드로, 학습 후 비교할 수 있습니다. (v2.0에서 solution으로 수정되었습니다.)
- 또한, `HINT`가 중간중간 들어있습니다. 따라서, 아래에 있는 Pycharm 설정도 같이 해주시면 감사하겠습니다.

## 🚀 시작하기
### 1️⃣ 저장소 클론

```bash
git clone https://github.com/kangdora/EduPy.git
cd 저장소명
```

### 2️⃣ 파일로 다운 받기
#### Download
[v2.0](https://github.com/kangdora/EduPy/archive/refs/tags/v2.0.1.zip)

## 이용 방법
- readme.md를 읽으신 후, 원하는 학습단원부터 진행해나가시면 됩니다.
- 각 디렉토리에 있는 학습 단원 안에는 `initial`과 `complete`가 있습니다.
- `initial`의 설명을 보고, 모르는 것은 찾아보는 연습을 해보시는 것을 추천드립니다.
- 웬만해서 다 하기 전까지는 최대한 `complete`를 참고하는 것을 지양하는 바입니다.
- 각 `*.py` 에는 하나의 `class`가 존재하고, 그 안에는 여러 `unittest`메서드가 존재합니다.
- 각 메서드에서 테스트를 실행하여 통과를 목표로 삼으시면 될 거 같습니다.
#### v2.0 업데이트 사항
`initial` -> `test`
`complete` -> `solution`

## Pycharm 설정
- Settings - Editor - TODO: 새로운 패턴 추가 `\bhint\b.*`
- `\bhint\b.*` 세부설정(더블클릭): Use color scheme TODO default colors 비활성화
-  ㄴ ForeGround: 1E1F22
-  ㄴ Background: 비활성화
-  ㄴ Error stripe mark: 비활성화
-  ㄴ Effects: 6B7077, Bordered

### 지난 버전
[v1.2](https://github.com/kangdora/EduPy/archive/refs/tags/v1.2.0.zip)

[v1.1](https://github.com/kangdora/EduPy/archive/refs/tags/v1.1.0.zip)

[V1.0](https://github.com/kangdora/EduPy/archive/refs/tags/v1.0.zip)
