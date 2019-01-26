# 바이너리 데이터
# = 큰 의미: 컴퓨터 내부에 있는 모든 파일
# = 작은 의미: 텍스트 데이터가 아닌 모든 파일
# 모듈을 읽어 들입니다.
from urllib import request
# urlopen() 함수로 구글의 메인 페이지를 읽습니다
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)
#write binary[바이너리 쓰기] 모드로
file = open("logo_hanbit.png", "wb")
file.write(output)





# 텍스트 데이터 다루는 방법 = 글자가 적혀있는 파일
# file = open("test.py", "r")
# textdata = file.read()
# file.close()
# print(type(textdata))

# 바이너리 데이터
# file = open("test.py", "rb")
# textdata = file.read()
# file.close()
# print(type(textdata))
# print(textdata)