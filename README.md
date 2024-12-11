 # 📚 시각 장애인과 시각에 문제가 있는 분들을 위한 텍스트 추출 및 음성 변환 프로그램

이 프로그램은 시각 장애인 또는 텍스트 정보를 음성으로 변환하여 편리하게 접근하고자 하는 사용자를 위해 개발되었습니다.  
이미지를 통해 텍스트를 추출하고, 텍스트를 음성으로 변환하며, OCR 및 음성 변환 성능을 시각화하는 기능을 제공합니다.

---

## 주요 기능

1. **이미지에서 텍스트 추출 (OCR)**:
   - 업로드된 이미지 또는 실시간 카메라 피드에서 텍스트를 추출합니다.
   - 추출된 텍스트와 OCR 신뢰도를 제공하여 결과의 품질을 평가합니다.

2. **텍스트 음성 변환 (TTS)**:
   - 추출된 텍스트를 음성으로 변환하여 읽어줍니다.
   - TTS 처리 시간을 측정하여 성능 데이터를 제공합니다.

3. **카메라를 통한 텍스트 캡처**:
   - 실시간 카메라 피드에서 텍스트를 추출합니다.
   - `s` 키를 눌러 텍스트를 추출하거나, `q` 키를 눌러 카메라를 종료합니다.

4. **성능 시각화**:
   - OCR 신뢰도 및 TTS 처리 시간 데이터를 시각화합니다.
   - OCR 시각화: Gaussian 기반 신뢰 구간과 평균선을 제공합니다.
   - TTS 시각화: 처리 시간의 평균, 표준 편차, 최대/최소 값을 강조하여 표시합니다.

---
## 프로젝트 구조
```
project/
├── main.py              # 프로젝트 메인 실행 파일
├── app/                 # 주요 앱 기능 코드가 포함된 디렉토리
│   ├── __init__.py      # Python 패키지 초기화 파일
│   ├── gui.py           # GUI 인터페이스 코드
│   ├── ocr.py           # OCR(텍스트 추출) 관련 코드
│   ├── performance.py   # 성능 시각화 관련 코드 (OCR, TTS)
│   ├── tts.py           # 텍스트 음성 변환(TTS) 관련 코드
│   ├── camera.py        # 카메라로 이미지 캡처 후 OCR 수행
├── data/                # 프로젝트 실행 중 생성 및 사용되는 데이터 파일
│   ├── captured_image.jpg  # 카메라로 캡처된 이미지
│   ├── output.mp3          # TTS로 생성된 음성 파일
│   ├── test_image1.png     # OCR 테스트용 샘플 이미지 1
│   ├── test_image2.png     # OCR 테스트용 샘플 이미지 2
├── requirements.txt     # 프로젝트 실행에 필요한 패키지 목록
├── README.md            # 프로젝트 설명 파일 (사용 방법, 설치 가이드 등)
├── LICENSE              # 프로젝트의 라이센스 정보를 포함
```
---
## ⚙️ 작동 원리

1. **이미지 업로드**:
   - 사용자가 로컬 이미지 파일을 선택하여 OCR을 수행합니다.
   
2. **카메라 캡처**:
   - 실시간 카메라 피드에서 텍스트를 추출합니다.

3. **텍스트 음성 변환**:
   - 추출된 텍스트를 TTS 엔진을 통해 음성으로 변환하고, MP3 파일로 저장한 후 재생합니다.

4. **성능 시각화**:
   - OCR 신뢰도와 TTS 처리 시간을 각각 독립적으로 시각화합니다.

---

## 📦 설치 및 실행 방법

### 1. 사전 설치 라이브러리
이 프로그램은 Python 3.9 이상에서 동작을 권장합니다. 다음 라이브러리를 설치해야 합니다:

- `pytesseract` (OCR 수행)
- `Pillow` (이미지 처리)
- `gTTS` (음성 변환)
- `matplotlib` (시각화)
- `numpy` (수학 계산)
- `tkinter` (GUI)
- `opencv-python` (카메라 처리)

다음 명령어를 통해 필요한 라이브러리를 설치하세요:

```bash
pip install pytesseract Pillow gTTS matplotlib numpy opencv-python
```
---

## 2. 사전 준비

### Tesseract OCR 엔진 설치:

Tesseract OCR 엔진은 Python 패키지(pytesseract)와 별도로 설치가 필요합니다.

**Windows**:
- Tesseract 설치 파일을 [공식 다운로드 페이지](https://github.com/tesseract-ocr/tesseract)에서 받아 설치한 후, 환경 변수에 경로를 추가하세요.

**Linux/Mac**:
```bash
sudo apt install tesseract-ocr
```

프로젝트 디렉토리 구성:
다음 파일들을 프로젝트 디렉토리에 포함시켜야 합니다:

- gui.py (프로그램 메인 GUI)
- ocr.py (OCR 관련 기능)
- tts.py (텍스트 음성 변환 기능)
- performance.py (시각화 기능)
- camera.py (카메라 텍스트 캡처 기능)
- main.py (프로그램 실행 파일)

## 3. 프로그램 실행
Python 스크립트를 실행하여 프로그램을 시작하세요:
```bash
python main.py
```

## 🌟 프로그램 사용 방법

### 초기 화면
<img src="https://github.com/user-attachments/assets/d6261bbe-8637-4a3d-a388-3b4f517ec353" alt="초기화면" width="850" height="550">

**1. 이미지 업로드**

- `"이미지 업로드"` 버튼을 클릭하여 텍스트를 추출할 이미지를 선택합니다.

**2. 카메라 캡처**

- `"카메라로 캡처"` 버튼을 클릭하여 실시간으로 텍스트를 추출합니다.
- `s` 키를 눌러 텍스트를 추출하고, `q` 키를 눌러 카메라를 종료합니다.

**3. 텍스트 음성 변환**

- 추출된 텍스트를 음성으로 변환하려면 `"소리 듣기"` 버튼을 클릭합니다.

**4. 성능 시각화**

- `"OCR 성능 시각화"` 버튼을 클릭하여 OCR 신뢰도를 시각화합니다.
- `"TTS 성능 시각화"` 버튼을 클릭하여 TTS 처리 시간을 시각화합니다.

## 🌟 **프로그램 사용 주의 사항**
- 텍스트를 추출한 후 소리 듣기를 누르고 tts로 음성을 변화하는데 시간이 걸릴 수 있습니다.
- 성능 시각화를 누르기 전 텍스트 추출과 소리듣기가 완성된 후 각각의 데이터가 생성되기 때문에 <br>성능을 확인하기 위해서는 앞서 텍스트를 추출하고 소리 듣기를 눌러주세요!

---
## 📈 출력 결과
### 1. 이미지 업로드
  - 이미지에서 추출된 텍스트와 OCR 신뢰도가 텍스트 박스 안과 콘솔 창에 표시됩니다.
  - ![이미지 업로드 후 텍스트 추출 화면](https://github.com/user-attachments/assets/df007b6a-c9b2-445e-ad62-d718b98e5a74)
  - ![텍스트 추출 터미널 확인](https://github.com/user-attachments/assets/2a8e8ff5-9618-4cb0-a849-82e6ef4a743f)
---

### 2. TTS 소리듣기
   - 추출된 텍스트를 TTS를 통해 음성 변환하여 들을 수 있으며, 음성 변환에 소요된 처리 시간이 콘솔에 출력됩니다.
   -  ![TTS 소리듣기](https://github.com/user-attachments/assets/ad350c1b-f788-487c-984a-e3c976aba036)
   -  ![신뢰도 TTS 처리시간 터미널 표시 확인](https://github.com/user-attachments/assets/fad916bd-22bd-479e-a3b7-e8f68278c1fe)
---

### 3. OCR 성능 시각화
  - 추출된 텍스트의 평균 신뢰도와 Gaussian 신뢰 구간이 포함된 막대 그래프가 표시됩니다.<br> `(data 폴더 안에 test_image1과 test image2를 예시로 이용하였습니다)`
  - ![ocr 성능 지표](https://github.com/user-attachments/assets/b3325558-e00c-42b8-9eee-064a99696fae)
---

### 4. TTS 성능 시각화
  - TTS로 음성 변환시 소요된 처리 시간의 `평균, 표준 편차, 최대/최소` 값이 포함된 막대 그래프가 표시됩니다.<br> `(data 폴더 안에 test_image1과 test image2를 예시로 이용하였습니다)`
  - ![TTS 처리시간](https://github.com/user-attachments/assets/dd0c1af1-0e81-42fb-81ff-fed4b405efbe)
---
## 🛠️ 참고 사항및 참고자료
1. **Tesseract OCR** 엔진이 설치되어 있어야 합니다.
2. **OCR 신뢰도**는 입력 이미지의 품질에 따라 다를 수 있습니다.
3. **TTS**는 인터넷 연결이 필요합니다 (Google TTS 사용).
4. **OpenAI GPT (ChatGPT)**:
   - 코딩 도움, 아이디어 정리 및 문서 작성 과정에서 사용하였습니다.
5. **참고 자료**:
   - Tesseract OCR: https://github.com/tesseract-ocr/tesseract
   - OpenCV: https://opencv.org/
   - Google TTS: https://pypi.org/project/gTTS/
   - https://wikidocs.net/132610
   - https://github.com/UB-Mannheim/tesseract/wiki
   - https://mj-thump-thump-story.tistory.com/entry/OCR-Tesseract-Windows-%ED%99%98%EA%B2%BD%EC%97%90-%EC%85%8B%EC%97%85
6. **라이브러리 공식 문서**:
   - Matplotlib: https://matplotlib.org/stable/contents.html
   - NumPy: https://numpy.org/doc/
---

## 라이센스
- 이 프로젝트는 MIT 라이센스에 따라 라이센스가 부여됩니다. 자세한 정보는 LICENSE 파일을 참조하세요.
---

## 📜 사용자에게 주는 가치와 한계점 그리고 소감
이 프로젝트를 처음 구상할 때, 세상을 흐릿하게 보거나 사물을 구별하기 어려운 시각적 어려움을 가진 분들이 텍스트가 포함된 이미지를 보더라도 내용을 이해하지 못해 겪는 어려움을 떠올렸고 도움을 드릴 수 있는 방법이 무엇이 있을지 고민하던 중
이러한 분들이 하나의 프로그램을 통해 텍스트를 쉽게 인식하고, 음성으로 내용을 전달받을 수 있도록 돕고자 이 프로젝트를 시작했습니다.<br>
프로그램을 개발하면서 여러 가지 보완해야 할 점들도 발견하였는데, 가장 큰 한계는 시각장애인 분들이 혼자서 이 프로그램을 실행하기 어렵다는 점이였습니다.
결국에 이 프로그램을 사용하려면 초기 설정과 실행 과정에서 다른 사람의 도움이 필연적으로 생길 수 밖에 없다는 점이 현실적인 한계로 다가왔습니다.
또한, 텍스트 추출 과정에서 사용된 Tesseract OCR의 성능은 이미지 품질과 OCR 알고리즘에 따라 달라지는데,보다 높은 정확도를 위해 Google OCR과 같은 고성능 도구를 사용했다면 더 정확한 결과를 시각장애인분들이 얻을 수 있었지 않았을까하는 아쉬움이 남았습니다.
이 부분은 향후 프로젝트의 업그레이드 방향으로 아이디어를 보완해서 수정하고자 합니다.





