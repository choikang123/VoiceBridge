# project/app/ocr.py

import pytesseract
from PIL import Image

def extract_text(image_path=None, frame=None, return_confidence=False):
    """
    Tesseract OCR을 사용하여 이미지에서 한글과 영어 텍스트를 추출합니다.
    신뢰도 값을 반환할지 선택할 수 있습니다.

    :param image_path: 이미지 파일 경로
    :param frame: 프레임 데이터 (numpy 배열)
    :param return_confidence: True이면 평균 신뢰도를 함께 반환
    :return: 추출된 텍스트 (문자열) 또는 (텍스트, 평균 신뢰도) 튜플
    """
    if frame is not None:
        # 프레임이 제공된 경우, PIL 이미지로 변환
        image = Image.fromarray(frame)
    elif image_path is not None:
        # 이미지 경로가 제공된 경우, 이미지 파일 열기
        image = Image.open(image_path)
    else:
        raise ValueError("이미지 경로나 프레임 데이터 중 하나는 반드시 제공해야 합니다.")

    try:
        # 기본 텍스트 추출
        text = pytesseract.image_to_string(image, lang="kor+eng")

        if return_confidence:
            # 신뢰도 계산
            result = pytesseract.image_to_data(image, lang="kor+eng", output_type=pytesseract.Output.DICT)
            confidences = [conf for conf in result["conf"] if conf != -1]
            average_confidence = sum(confidences) / len(confidences) if confidences else 0
            return text, average_confidence

        return text
    except Exception as e:
        raise RuntimeError(f"Tesseract OCR 처리 중 오류 발생: {e}")
