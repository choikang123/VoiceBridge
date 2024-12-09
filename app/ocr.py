from PIL import Image
import pytesseract
import cv2

def extract_text(image_path=None, frame=None):
    if frame is not None:
        processed_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    elif image_path is not None:
        processed_image = Image.open(image_path)
    else:
        raise ValueError("이미지 경로나 프레임 데이터가 필요합니다.")

    config = "--psm 6 --oem 3"
    raw_text = pytesseract.image_to_string(processed_image, lang="kor+eng", config=config)
    return raw_text
