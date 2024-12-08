import os
from gtts import gTTS

def text_to_speech(text, lang='ko'):
    # 프로젝트 루트를 기준으로 경로 설정
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # app 폴더의 상위 폴더
    output_path = os.path.join(project_root, 'data', 'output.mp3')  # data 폴더에 저장

    tts = gTTS(text=text, lang=lang)
    tts.save(output_path)  # 파일 저장

    # 파일 재생
    os.system(f'start {output_path}')  # Windows 환경
