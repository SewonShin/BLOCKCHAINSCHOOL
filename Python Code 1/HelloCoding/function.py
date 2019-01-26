





# # 파일을 다룰 때
# file = open("function.py", mode="r", encoding="UTF-8")

# i = 0

# for line in file:
#     print(i, line, end="")
#     i += 1
# file.close()




# # # 파일을 다룰 때

# # 1. 파일 열기 - open()
# file = open("tuple.py", mode="a", encoding="UTF-8")
# # 읽을 때: "r"
# # 쓸 때: "w", 뒤에 붙여 쓸 때: "a"
# # 2. 파일 읽는 - file.read()
# # print(file.read())
# # 3. 파일 쓰는 - file.write()
# file.write("abcde1234")
# # 4. 파일 닫기 - file.close()
# file.close()






# dictionary = {
#     1: 1,
#     2: 1
# }

# # 함수를 선언합니다.
# def fibonacci(n):
#     if n in dictionary:
#         return dictionary[n]
#     # 피보나치 수를 구합니다.
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         output = fibonacci(n - 1) + fibonacci(n - 2)
#         dictionary[n] = output
#         return output
# # 함수를 호출합니다.
# print(fibonacci(30))







# # 변수를 선언합니다.
# counter = 0
# # 함수를 선언합니다.
# def fibonacci(n):
#     # 어떤 피보나치 수를 구하는지 출력합니다.
#     print("fibonacci({})를 구합니다.".format(n))
#     global counter
#     counter += 1
#     # 피보나치 수를 구합니다.
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# #함수를 호출합니다.
# fibonacci(10)
# print("---")
# print("fibonacci(20) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))


# # 함수를 선언합니다.
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# # 함수를 호출합니다.
# print("fibonacci(1):", fibonacci(1))
# print("fibonacci(2):", fibonacci(2))
# print("fibonacci(3):", fibonacci(3))
# print("fibonacci(4):", fibonacci(4))
# print("fibonacci(5):", fibonacci(5))






# # 함수를 선언합니다.
# def factorial(n):
#     # n이 1이라면 1을 리턴
#     if n == 1:
#         return 1
#     # n이 1이 아니라면 n * (n-1)!을 리턴
#     elif n > 1:
#         return n * factorial(n - 1)

# # 함수를 호출합니다.
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))
# print("3!:", factorial(4))
# print("3!:", factorial(5))






# factorial(n) = n * factorial(n - 1) (n >= 2 일 때)
# factorial(1) = 1

# factorial(4) = 4 * 6 = 24
# factorial(3) = 3 * 2 = 6
# factorial(2) = 2 * 1 = 2
# factorial(1) = 1 # 탈출할 구멍






# # 함수를 선언합니다.
# def factorial(n):
#     #변수를 선언합니다.
#     output = 1
#     # 반복문을 돌려 숫자를 더합니다.
#     for i in range(1, n + 1): # range(1, n + 1) : 0~n
#         output *= i
#     # 리턴합니다.
#     return output

# # 함수를 호출합니다.
# print("1!:", factorial(1))
# print("2!:", factorial(2))
# print("3!:", factorial(3))





# def factorial(n):

# n! = n * (n - 1) * (n - 2) "..." 1
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24






# # 재귀 - recursion[!] : 탈출할 수 있는 구멍...!
# def recursion_function(i):
#     print("안녕하세요")
#     if i < 10:
#         recursion_function(i + 1)

# recursion_function(0)







# # # custom_max(<리스트>)
# # # 리스트 내부에서 최대값

# def custom_max(input_list):
#     output = input_list[0]

#     for element in input_list:
#         if output < element:
#             output = element

#     return output

# print(custom_max([32, 32, 923, 2, 123]))








# def custom_max(input_list):
# def <함수>(<매개변수>):
#     <변수> = <초기값>
#     # <여러 가지 처리>
#     # <여러 가지 처리>
#     # <여러 가지 처리>
#     return <변수>




# # 함수를 선언합니다.
# def sum_all(start, end):
#     # 변수를 선언합니다.
#     output = 0
#     # 반복문을 돌려 숫자를 더합니다.
#     for i in range(start, end + 1):
#         output += i
#     # 리턴합니다.
#     return output
# # 함수를 호출합니다.
# print("0 to 100:", sum_all(0, 100))
# print("0 to 1000:", sum_all(0, 1000))
# print("50 to 100:", sum_all(50, 100))
# print("500 to 1000", sum_all(500, 1000))






# # 함수를 정의합니다.
# def return_test():
#     print("A 위치입니다.")
#     return 100 # 리턴합니다: 함수를 여기서 끝내고 돌아가주세요...!
#     print("B 위치입니다.")

# # 함수를 호출합니다.
# value = return_test()
# print(value)




# # 디폴트 매개 변수 [= 기본 매개 변수]
# def 함수_이름(a=10, b=20):
#     <문장>
# 함수_이름()
# 함수_이름(10)
# 함수_이름(10, 20)





# def print_n_times(n, *values):
#     # n번 반복합니다.
#     for i in range(n):
#         # values는 리스트처럼 활용합니다.
#         for value in values:
#             print(value)
#         #단순한 줄바꿈
#         print()

# # 함수를 호출합니다.
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")






# def print_n_times(value, n):
#     # value = "안녕하세요"
#     # n = 10
#     for i in range(n):
#         print(value)

# print_n_times("안녕하세요"10, 20, 30)






# # 매개 변수

# ## 가변 매개 변수
# def 함수_이름(a, b, c, d, e):
#     <문장>
# 함수_이름(1, 2, 3, 4, 5)

# # 매개 변수 오류: 매개 변수를 입력한 것보다 적거나 많이 넣으면 오류 발생

# # 가변 매개 변수
# def 함수_이름(a, b, c, d, *e): # * 기호를 사용
#     <문장>
# 함수_이름(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# # # 함수: function : 코드의 뭉치
# # def custom_function():
# #     print("안녕하세요")
# #     print("안녕하세요")
# #     print("안녕하세요")

# # custom_function()


# # 함수
# print()
# len()
# input()
# ## 용어 정리
# string = input("안녕하세요")
# - input(): 함수
# - "안녕하세요": 매개변수 → 괄호 안에 들어 있는 것
# - string: 리턴값 → 함수의 결과

# ## 함수 만들기
# def custom_function():
#     <문장>
#     <문장>

# def custom_function():
#     <문장>
#     <문장>
#     return <리턴하고 싶은 것>