import cv2
from app.ocr import extract_text

def capture_image_for_ocr():
    cap = cv2.VideoCapture(0)  # 기본 카메라 사용
    if not cap.isOpened():
        raise Exception("카메라를 열 수 없습니다.")

    print("카메라가 열렸습니다. 's'를 눌러 텍스트를 추출하고, 'q'를 눌러 종료하세요.")

    while True:
        ret, frame = cap.read()
        if not ret:
            raise Exception("프레임을 읽을 수 없습니다.")

        cv2.imshow("카메라 피드", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # 's'를 누르면 텍스트 추출
            print("텍스트 추출 중...")
            text = extract_text(frame=frame)
            print(f"추출된 텍스트: {text}")
            cap.release()
            cv2.destroyAllWindows()
            return text
        elif key == ord('q'):  # 'q'를 누르면 종료
            print("카메라 종료")
            cap.release()
            cv2.destroyAllWindows()
            return None
