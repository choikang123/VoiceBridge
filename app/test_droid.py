import cv2

def test_droidcam_stream():
    # DroidCam 스트림 URL 설정
    stream_url = "http://10.50.97.47:4747/video"  # DroidCam의 비디오 스트림 URL
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print(f"스트림을 열 수 없습니다: {stream_url}")
        return

    print("DroidCam 스트림 테스트 중... 'q'를 눌러 종료합니다.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("DroidCam Stream", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_droidcam_stream()
