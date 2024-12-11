import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import filedialog
from app.ocr import extract_text
from app.tts import text_to_speech
from app.performance import visualize_performance, visualize_tts_durations
from app.camera import capture_image_for_ocr
import time

def run_app():
    ocr_confidences = []  # OCR 신뢰도 저장
    tts_durations = []    # TTS 처리 시간 저장

    # 기본 root 초기화
    root = tk.Tk()
    root.title("시각 장애인과 시각에 문제가 있는 분들을 위한 프로그램")
    root.configure(bg="#f4f4f9")

    # 창 크기 설정
    window_width = 700
    window_height = 500

    # 화면 크기 가져오기
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 중앙 배치 계산
    x_coord = int((screen_width - window_width) / 2)
    y_coord = int((screen_height - window_height) / 2)

    # 창 위치 및 크기 설정
    root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

    # 한글 폰트 설정
    default_font = Font(family="맑은 고딕", size=12)  # Windows용 폰트
    root.option_add("*Font", default_font)  # 기본 폰트 설정

    # 메인 프레임 생성 (내부 위젯을 중앙 정렬하기 위해)
    main_frame = ttk.Frame(root)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")  # 프레임을 창 중앙에 배치

    def select_image():
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All Files", "*.*")]
        )
        if not filepath:
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', "파일이 선택되지 않았습니다.")
            return

        try:
            text, confidence = extract_text(image_path=filepath, return_confidence=True)
            print(f"추출된 텍스트: {text}, 신뢰도: {confidence:.2f}%")

            ocr_confidences.append(confidence)  # 신뢰도 저장
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', f"텍스트: {text}\n\n신뢰도: {confidence:.2f}%")
        except Exception as e:
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', f"오류 발생: {e}")

    def play_audio():
        text = text_box.get('1.0', tk.END).strip()
        if text:
            try:
                start_time = time.time()
                text_to_speech(text)
                duration = time.time() - start_time
                tts_durations.append(duration)  # 처리 시간 저장
                print(f"TTS 처리 시간: {duration:.2f}초")
            except Exception as e:
                print(f"TTS 오류: {e}")

    def capture_from_camera():
        try:
            text, confidence = capture_image_for_ocr()
            if text:
                ocr_confidences.append(confidence)  # 신뢰도 저장
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', f"텍스트: {text}\n\n신뢰도: {confidence:.2f}%")
            else:
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', "캡처가 취소되었습니다.")
        except Exception as e:
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', f"카메라 처리 중 오류 발생: {e}")

    def show_ocr_performance():
        if ocr_confidences:
            visualize_performance(
                scores=ocr_confidences,
                labels=[f"Sample {i+1}" for i in range(len(ocr_confidences))],
                title="OCR 성능 지표 (Gaussian 기반 신뢰 구간 포함)",
                ylabel="Confidence (%)"
            )

    def show_tts_performance():
        if tts_durations:
            visualize_tts_durations(
                durations=tts_durations,
                labels=[f"TTS {i+1}" for i in range(len(tts_durations))],
                title="TTS 처리 시간 분석",
                ylabel="Processing Time (s)"
            )

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5, relief="flat")
    style.configure("TLabel", font=("Helvetica", 14), background="#f4f4f9", foreground="#34495E")

    ttk.Label(main_frame, text="시각에 문제가 있는 분들을 돕기위해 만들어진 프로그램", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

    btn_select = ttk.Button(main_frame, text="이미지 업로드", command=select_image)
    btn_select.grid(row=1, column=0, pady=10, padx=10)

    btn_camera = ttk.Button(main_frame, text="카메라로 캡처", command=capture_from_camera)
    btn_camera.grid(row=1, column=1, pady=10, padx=10)

    btn_ocr_performance = ttk.Button(main_frame, text="OCR 성능 시각화", command=show_ocr_performance)
    btn_ocr_performance.grid(row=1, column=2, pady=10, padx=10)

    btn_tts_performance = ttk.Button(main_frame, text="TTS 성능 시각화", command=show_tts_performance)
    btn_tts_performance.grid(row=1, column=3, pady=10, padx=10)

    text_box = tk.Text(main_frame, height=15, width=60, wrap=tk.WORD, font=("Courier", 12))
    text_box.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    btn_play = ttk.Button(main_frame, text="소리 듣기", command=play_audio)
    btn_play.grid(row=3, column=0, columnspan=4, pady=10)

    root.mainloop()
