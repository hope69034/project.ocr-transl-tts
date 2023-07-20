import cv2
import pytesseract


#테서렉트 설치파일 다운 https://github.com/UB-Mannheim/tesseract/wiki

# Tesseract OCR 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract OCR의 설치 경로로 변경해야 할 수 있습니다.
#C:\Program Files\Tesseract-OCR 로 시스템변수등록하면필요없다

# 비디오 캡처 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 나타냅니다. 다른 카메라를 사용하려면 해당 장치 인덱스를 사용하세요.

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
    # 화면에 인식된 문자 출력
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('OCR', frame)

    # q 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 시 자원 해제
cap.release()
cv2.destroyAllWindows()
