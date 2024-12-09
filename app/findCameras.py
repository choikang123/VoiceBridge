import cv2

def test_camera(camera_index):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"카메라 {camera_index}를 열 수 없습니다.")
        return

    print(f"카메라 {camera_index}를 테스트 중... 'q'를 눌러 종료합니다.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"카메라 {camera_index}에서 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow(f"카메라 {camera_index}", frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    for i in range(3):  # 0번부터 2번까지 카메라 테스트
        test_camera(i)
