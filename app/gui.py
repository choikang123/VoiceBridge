import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import filedialog
from app.ocr import extract_text
from app.tts import text_to_speech
from app.performance import visualize_performance
from app.camera import capture_image_for_ocr
import time

def run_app():
    ocr_confidences = []  # OCR 신뢰도 저장
    tts_durations = []    # TTS 처리 시간 저장

    # 기본 root 초기화
    root = tk.Tk()
    root.title("시각 장애인을 위한 텍스트 추출 프로그램")
    root.geometry("700x500")
    root.configure(bg="#f4f4f9")

    # 한글 폰트 설정
    default_font = Font(family="맑은 고딕", size=12)  # Windows용 폰트
    root.option_add("*Font", default_font)  # 기본 폰트 설정

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

    def show_performance():
        if ocr_confidences:
            visualize_performance(
                scores=ocr_confidences,
                labels=[f"Sample {i+1}" for i in range(len(ocr_confidences))],
                title="OCR 성능 지표 (Gaussian 기반 신뢰 구간 포함)",
                ylabel="Confidence (%)"
            )
        if tts_durations:
            visualize_performance(
                scores=tts_durations,
                labels=[f"TTS {i+1}" for i in range(len(tts_durations))],
                title="TTS 처리 시간",
                ylabel="Processing Time (s)"
            )


    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5, relief="flat")
    style.configure("TLabel", font=("Helvetica", 14), background="#f4f4f9", foreground="#34495E")

    ttk.Label(root, text="OCR 및 음성 변환 앱", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

    btn_select = ttk.Button(root, text="이미지 업로드", command=select_image)
    btn_select.grid(row=1, column=0, pady=10, padx=10)

    btn_camera = ttk.Button(root, text="카메라로 캡처", command=capture_from_camera)
    btn_camera.grid(row=1, column=1, pady=10, padx=10)

    btn_performance = ttk.Button(root, text="성능 시각화", command=show_performance)
    btn_performance.grid(row=1, column=2, pady=10, padx=10)

    text_box = tk.Text(root, height=15, width=60, wrap=tk.WORD, font=("Courier", 12))
    text_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    btn_play = ttk.Button(root, text="소리 듣기", command=play_audio)
    btn_play.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()
