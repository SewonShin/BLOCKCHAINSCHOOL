from flask import Flask

app = Flask[__name__]

@app.route("/")
def hello():
    return "Hello World!"






# # 모듈을 읽어 들입니다.
# from math import sin, cos, tan, floor, ceil

# # sin, cos, tan을 구합니다.
# print("sin(1):", sin(1))
# print("cos(1):", cos(1))
# print("tan(1):", tan(1))

# # 내림과 울림을 구합니다.
# print("floor(2.5):", floor(2.5))
# print("ceil(2.5):", ceil(2.5))

#제어 정방향
#우리가 만든 코드 → 모듈[다른 사람이 만든 것]:라이브러리
#제어 역방향
#우리가 만든 코드 ← 모듈[다른 사람이 만든 것]:프레임워크





# 조건문 반복문 함수: 재귀함수
# 모듈: os 모듈
# import os

# def read_folder(original_path):
#     for path in os.listdir(original_path):
#         if os.path.isdir(path):
#             read_folder(original_path + "/" + path)
#         else:
#             print(path)

# read_folder(".")







# import os
# for path in os.listdir("."):
#     if os.path.isdir(path):
#         print(path, "은 디렉터리입니다")
#     else:
#         print(path, "은 파일입니다")







# import os
# print(os.listdir("."))
# # os.path.isdir()







# from urllib import request

# target = request.urlopen("https://google.com")
# output = target.read()
# print(output)



# import time

# print("지금부터 5초 동안 정지합니다!")
# time.sleep(5)
# print("프로그램을 종료합니다.")





# from datetime import datetime
# now = datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()








# import os

# os.getcwd()
# os.listdir()
# os.mkdir("")
# os.rmdir("")
# os.rename()
# os.remove("") # os.unlink()
# os.system()




#import os
#print(os.name)





# import sys

# print(sys.version)
# print(sys.copyright)
# print(sys.getwindowsversion())




# import sys

# print(sys.argv)

# 일반적인 프로그래밍 언어
# 스칼라: 하나의 값만을 가지는 것 - 문자열, 숫자, 불리언
# 벡터: 여러 개의 값을 가질 수 있는 것 - 리스트, 딕셔너리

# 수학과 관련된 프로그래밍 언어 - 선형대수
# 스칼라: 하나의 값만을 가지는 것
# 벡터: 스칼라가 모인 것
# 텐서: (정의가 엄청나게 다양) 벡터가 모인 것

# 0차 텐서 = 스칼라
# 1차 텐서 = 벡터
# 2차 텐서 이상 => 프로그래밍 언어에서 말하는 텐서 