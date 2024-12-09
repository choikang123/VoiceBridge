import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.ocr import extract_text
from app.tts import text_to_speech
from app.camera import capture_image_for_ocr

def run_app():
    def select_image():
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All Files", "*.*")]
        )
        if not filepath:
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', "파일이 선택되지 않았습니다.")
            return

        print(f"선택된 파일: {filepath}")  # 디버깅용 출력
        try:
            text = extract_text(image_path=filepath)
            print(f"추출된 텍스트: {text}")

            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', text)
        except Exception as e:
            print(f"OCR 처리 중 오류 발생: {e}")
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', f"오류 발생: {e}")

    def play_audio():
        text = text_box.get('1.0', tk.END).strip()
        if text:
            text_to_speech(text)

    def capture_from_camera():
        try:
            text = capture_image_for_ocr()  # 카메라로 이미지 캡처 및 OCR 처리
            if text:
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', text)
            else:
                text_box.delete('1.0', tk.END)
                text_box.insert('1.0', "캡처가 취소되었습니다.")
        except Exception as e:
            print(f"오류: {e}")
            text_box.delete('1.0', tk.END)
            text_box.insert('1.0', f"카메라 처리 중 오류 발생: {e}")

    root = tk.Tk()
    root.title("OCR 및 음성 변환 앱")
    root.geometry("700x500")
    root.configure(bg="#f4f4f9")

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5, relief="flat")
    style.configure("TLabel", font=("Helvetica", 14), background="#f4f4f9", foreground="#34495E")

    ttk.Label(root, text="OCR 및 음성 변환 앱", font=("Helvetica", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    btn_select = ttk.Button(root, text="이미지 업로드", command=select_image)
    btn_select.grid(row=1, column=0, pady=10, padx=10)

    btn_camera = ttk.Button(root, text="카메라로 캡처", command=capture_from_camera)
    btn_camera.grid(row=1, column=1, pady=10, padx=10)

    text_box = tk.Text(root, height=15, width=60, wrap=tk.WORD, font=("Courier", 12))
    text_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    btn_play = ttk.Button(root, text="소리 듣기", command=play_audio)
    btn_play.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
