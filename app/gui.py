import tkinter as tk
from tkinter import filedialog
from app.ocr import extract_text
from app.tts import text_to_speech

def run_app():
    def select_image():
        filepath = filedialog.askopenfilename() # 파일 탐색기를 열어서 창을 열고 이미지 선택해주기
        if filepath:
            text = extract_text(filepath) # 파일 주소를 가져와서 선택된 이미지에서 텍스트를 호출
            text_box.insert('1.0', text) # 추출된 문자를 첫줄 부터 내용 삽입

    def play_audio():
        text = text_box.get('1.0', tk.END).strip() # 텍스트 상자의 내용 가져와서 양끝 공백 제거라고
        if text:
            text_to_speech(text) # 텍스트를 음성으로 반환하고 재생

    root = tk.Tk() # tinker를 이용해서 gui 생성
    root.title("OCR 및 음성 변환 앱") # 이건 제목이고
    root.geometry("400x300") # 이건 창의 크기 임시로 일단 지정해두기

    btn_select = tk.Button(root, text="이미지 선택", command=select_image) # 버튼 클릭시 select_image 실행
    btn_select.pack(pady=10) 

    text_box = tk.Text(root, height=8, width=40)
    text_box.pack(pady=10)

    btn_play = tk.Button(root, text="소리 듣기", command=play_audio)
    btn_play.pack(pady=10)

    root.mainloop()
