import cv2
import pytesseract

import pygame
import os 
from gtts import gTTS
from translate import Translator
def translate_english_to_korean(text):
    translator = Translator(to_lang='ko', from_lang='en')
    translation = translator.translate(text)
    return translation

global file_name
file_name='./sound/sample.mp3' # mp3로 ########



def filename_change():
  global file_name  
  global count 
  count=0
  while os.path.exists(file_name):
      count += 1
      file_name = f'./sound/sample{count}.mp3' 
 
# Tesseract OCR 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract OCR의 설치 경로로 변경해야 할 수 있습니다.

# 비디오 캡처 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 나타냅니다. 다른 카메라를 사용하려면 해당 장치 인덱스를 사용하세요.
   

def main():
    try: 
        while True:
            # 프레임 읽기
            ret, frame = cap.read()
            if not ret:
                break
            # 이미지 전처리
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 필요한 전처리 작업을 수행할 수 있습니다. 예: 가우시안 블러, 이진화 등

            # 이미지에서 문자 인식
            text = pytesseract.image_to_string(gray)
            #text = pytesseract.image_to_string(gray, lang='eng')
 
            #번역
            #text = translate_english_to_korean(text) # Translate
            #print(text)
            tts_en=gTTS(text=text, lang='en') #error
            filename_change()
            tts_en.save(file_name)  
            #playsound(file_name)
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue
            # Close the audio file
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()

            # 화면에 인식된 문자 출력
            cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('OCR', frame)
            # q 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # 종료 시 자원 해제
        cap.release()
        cv2.destroyAllWindows()
    except:
        main()
 



 
main()