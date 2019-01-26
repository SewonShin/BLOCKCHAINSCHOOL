


# year = int(input("태어난 연도 입력> "))

# if year % 12 == 0:
#     print("원숭이")
# elif year % 12 == 1:
#     print("닭")
# elif year % 12 == 2:
#     print("개")
# elif year % 12 == 3:
#     print("돼지")
# elif year % 12 == 4:
#     print("쥐")
# elif year % 12 == 5:
#     print("소")
# elif year % 12 == 6:
#     print("범")
# elif year % 12 == 7:
#     print("토끼")
# elif year % 12 == 8:
#     print("용")
# elif year % 12 == 9:
#     print("뱀")
# elif year % 12 == 10:
#     print("말")
# else:
#     print("양")




# if x > 10:
#     if x < 20
#         print("조건에 맞습니다.")

# if x > 10 and x < 20:
#     print("조건에 맞습니다.")

# if 10 < x < 20:
#     print("조건에 맞습니다.")




# zero = 0
# if zero == 0:
#     #곧 개발하겠음
#     raise NotImplementedError
# else:
#     #곧 개발하겠음
#     raise NotImplementedError



# zero = 0
# if zero == 0:
#     pass
# else:
#     pass



# print("# if 조건문에 0 넣기")
# if 0:
#     print("0은 True로 변환됩니다")
# else:
#     print("0은 False로 변환됩니다")
# print()

# print("# if 조건문에 빈 문자열 넣기")
# if "":
#     print("빈 문자열은 True로 변환됩니다.")
# else:
#     print("빈 문자열은 False로 변환됩니다.")



# #elif 구문
# import datetime

# now = datetime.datetime.now()
# month = now.month

# # 봄 구분
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))
# # 여름 구분
# elif 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month))
# # 가을 구분
# elif 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다!".format(now.month))
# # 겨울 구분    
# else: 
#     print("이번 달은 {}월로 겨울입니다!".format(now.month))





# number = input("정수 입력> ")
# number = int(number)

# if number % 2 == 0:
#     # 참일 때 → 짝수
#     print("{}는 짝수입니다.".format(number))
# else:
#     # 거짓일 때 → 홀수
#     print("{}는 홀수입니다.".format(number))




# #홀수와 짝수 구분
# number = input("정수 입력> ")
# last_character = number[-1]

# if last_character in "02468":
#     print("짝수입니다...!")

# if last_character in "13579":
#     print("홀수입니다...!")



# # 홀수와 짝수 구분
# number = input("정수 입력> ")
# last_character = number[-1]
# last_number = int(last_character)

# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수입니다...!")

# if last_number == 1 \
#     or last_number == 3 \
#     or last_number == 5 \
#     or last_number == 7 \
#     or last_number == 9:
#     print("홀수입니다...!")




# import datetime
# now = datetime.datetime.now()
# if 3 <= now.month <= 5:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))
# if 6 <= now.month <= 8:
#     print("이번 달은 {}월로 여름입니다!".format(now.month))
# if 9 <= now.month <= 11:
#     print("이번 달은 {}월로 가을입니다!".format(now.month))
# if now.month == 12 or 1 <= now.month <= 2:
#     print("이번 달은 {}월로 봄입니다!".format(now.month))



# import datetime
# now = datetime.datetime.now()
# #오전 구분
# if now.hour < 12:
#     print("현재 시간은 {}시로 오전입니다!".format(now.hour))
# #오후 구분
# if now.hour >= 12:
#     print("현재 시간은 {}시로 오후입니다!".format(now.hour))



# # 입력을 받습니다.
# number = input("정수 입력> ")
# number = int(number)
# # 양수 조건
# if number > 0:
#     print("양수입니다")
# #음수 조건
# if number < 0:
#     print("음수입니다")
# # 0 조건
# if number == 0:
#     print("0입니다")