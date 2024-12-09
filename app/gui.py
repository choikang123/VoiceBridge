import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from app.ocr import extract_text
from app.tts import text_to_speech
from app.camera import capture_image_for_ocr  # 카메라 기능 가져오기

def run_app():
    root = tk.Tk()  # Tkinter 메인 윈도우 초기화
    root.title("OCR 및 음성 변환 앱")
    root.geometry("700x500")
    root.configure(bg="#f4f4f9")

    selected_camera = tk.IntVar(value=0)  # 카메라 선택 변수 (root 이후에 생성)

    def select_image():
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All Files", "*.*")]
        )
        if filepath:
            print(f"선택된 파일: {filepath}")
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
            text = capture_image_for_ocr(camera_index=selected_camera.get())
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

    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5, relief="flat")
    style.configure("TLabel", font=("Helvetica", 14), background="#f4f4f9", foreground="#34495E")

    ttk.Label(root, text="카메라 선택:", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=5)
    ttk.Radiobutton(root, text="기본 카메라", variable=selected_camera, value=0).grid(row=0, column=1, padx=10, pady=5)
    ttk.Radiobutton(root, text="외부 카메라", variable=selected_camera, value=2).grid(row=0, column=2, padx=10, pady=5)

    btn_select = ttk.Button(root, text="이미지 업로드", command=select_image)
    btn_select.grid(row=1, column=0, pady=10, padx=10)

    btn_camera = ttk.Button(root, text="카메라로 캡처", command=capture_from_camera)
    btn_camera.grid(row=1, column=1, pady=10, padx=10)

    text_box = tk.Text(root, height=15, width=60, wrap=tk.WORD, font=("Courier", 12))
    text_box.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    btn_play = ttk.Button(root, text="소리 듣기", command=play_audio)
    btn_play.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()
