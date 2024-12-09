# project/app/ocr.py

import pytesseract
from PIL import Image

def extract_text(image_path=None, frame=None):
    """
    Tesseract OCR을 사용하여 이미지에서 한글과 영어 텍스트를 추출합니다.

    :param image_path: 이미지 파일 경로
    :param frame: 프레임 데이터 (numpy 배열)
    :return: 추출된 텍스트 (문자열)
    """
    if frame is not None:
        # 프레임이 제공된 경우, PIL 이미지로 변환
        image = Image.fromarray(frame)
    elif image_path is not None:
        # 이미지 경로가 제공된 경우, 이미지 파일 열기
        image = Image.open(image_path)
    else:
        raise ValueError("이미지 경로나 프레임 데이터 중 하나는 반드시 제공해야 합니다.")

    # Tesseract를 사용하여 이미지에서 텍스트 추출
    try:
        text = pytesseract.image_to_string(image, lang="kor+eng")  # 한글+영어 추출
    except Exception as e:
        raise RuntimeError(f"Tesseract OCR 처리 중 오류 발생: {e}")

    return text
