import pytesseract
from PIL import Image
from translate import Translator

# 이미지 파일 불러오기
image_path = 'rxo.jpeg'
image = Image.open(image_path)

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(image, lang='eng')

# 추출된 텍스트 출력
print()
print("Extracted Text (English):")
print()
print(text)

# 번역
translator = Translator(to_lang='ko', from_lang='en')
translation = translator.translate(text)

# 번역된 텍스트 출력
print("\nTranslated Text (Korean):")
print()
print(translation)
