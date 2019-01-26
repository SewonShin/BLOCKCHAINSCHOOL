tti = ["원숭이", "닭", "개", "돼지",
        "쥐", "소", "범", "토끼",
        "용", "뱀", "말", "양"]

str_input = input("태어난 해를 입력해주세요> ")
birth_year = int(str_input) % 12
print(tti[birth_year], "띠입니다.")





# # 리스트를 선언합니다.
# array = [273, 32, 103, 57, 52]
# # 리스트에 반복문을 적용합니다.
# for element in array:
#     if element > 100:
#         # 출력합니다.
#         print(element)



# # 리스트를 선언합니다.
# array = [273, 32, 103, 57, 52]

# # 리스트에 반복문을 적용합니다.
# for element in array:
#     # 출력합니다.
#     print(element)


# list_a = [1, 2, 3]

# # in 연산자
# print(1 in list_a)
# print("안녕" in "안녕하세요")


# list_a = [1, 2, 3]
# # 리스트의 요소 제거하기
# # del <리스트>[<인덱스>]
# list_a.pop(-2) # [1, 3]
# del list_a[-1] # [1]
# print(list_a)



# list_a = [1, 2, 3]
# # 리스트 요소 제거하기
# # del <리스트>[<인덱스>]
# del list_a[2]
# del list_a[0]
# print(list_a)



# list_a = [1, 2, 3]
# # 리스트의 요소 제거하기
# # <리스트>.pop(<인덱스>)
# # del <리스트>[<인덱스>]
# # 리스트의 요소 모두 제거하기
# # <리스트>.clear()
# list_a.pop(0) # list_a = [2, 3]
# print(list_a)
# list_a.pop()  # list_a = [2]
# print(list_a)
# list_a.clear()# list_a = []
# print(list_a)



# list_a = [1, 2, 3]
# # 리스트에 요소 추가하기
# # <리스트>.append(<요소>) 
# # <리스트>.insert(<위치>, <요소>)
# # <리스트>.extend(<리스트>)
# list_a.append(4) # list_a = [1, 2, 3, 4]
# print(list_a)
# list_a.insert(0, 0) # list_a = [0, 1, 2, 3, 4]
# print(list_a)
# list_a.insert(1, 10) # list_a = [0, 10, 1, 2, 3, 4]
# print(list_a)
# list_a.extend([1, 2, 3, 4]) # list_a = [0, 10, 1, 2, 3, 4, 1, 2, 3, 4]
# print(list_a)
# list_a.append([1, 2, 3, 4]) # list_a = [0, 10, 1, 2, 3, 4, 1, 2, 3, 4, [1, 2, 3, 4]]
# print(list_a)

# # 생성하기
# list_a = []
# list_b = [1, 2, 3, 4, 5, 6]
# list_c = [1, "반복문", 3, True]
# list_d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # 접근 연산자
# print(list_c[1])        # "반복문"
# print(list_c[1][0])     # "반"
# print(list_d)
# print(list_d[1])        # [4, 5, 6]
# print(list_d[1][1])     # 5





# #생성하기
# list_a = []
# list_b = [1, 2, 3, 4, 5, 6]
# list_c = [1, "반복문", 3, True]

# #접근 연산자
# print(list_b[0])
# print(list_b[1])
# print(list_b[-1])
# print(list_b[-2])
# # 결합/연결 연산자
# print(list_b + list_c) # [1, 2, 3, 4, 5, 6, 1, "반복문", 3, True]
# # 반복 연산자
# print(list_b * 3) # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, ]




# #리스트
# 여러가지 자료를 저장할 수 있는 자료

# #생성 방법
# [<요소(element)>, <요소>, <요소>...]
# 예) [1, 2, 3, 4, 5]

# # 사용 방법
# 1. 요소에 접근하기: 리스트[인덱스] → 0부터 시작!
# 2. 리스트 결합하기: 리스트 + 리스트 → {1, 2} + {3, 4}
# 3. 리스트 반복하기: 리스트 * 숫자 → {1, 2} * 2
# ※ 문자열과 비슷해요!