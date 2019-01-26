# # 리스트의 함수
# list_a = [52, 273, 103, 32, 57]

# # 최소값
# max_value = list_a[0]
# for element in list_a:
#     if element > max_value:
#         max_value = element

# # 출력합니다.
# # print("최소값:", min_value) # 32
# print("최대값:", max_value) # 273


# # 리스트의 함수
# list_a = [52, 273, 103, 32, 57]

# # 최소값과 최대값 구하기
# min_value = min(list_a)
# max_value = max(list_a)

# # 출력합니다.
# print("최소값:", min_value) # 32
# print("최대값:", max_value) # 273





# # 리스트를 선언합니다.
# array = ["사과", "자두", "초콜릿", "바나나", "체리"]
# output = [fruit for fruit in array if fruit != "초콜릿"]
# # 출력합니다.
# print(output)




# array = [i * i for i in range(0, 20, 2) if 100 < (i*i) < 300]
# # 출력합니다.
# print(array)




# #변수를 선언합니다.
# array = []
# # 반복문을 적용합니다.
# for i in range(0, 20, 2):
#     array.append(i * i)
# # 출력합니다.
# print(array)



# example_dictionary = {
#     "키A": "값A",
#     "키B": "값B",
#     "키C": "값C",
# }

# for key, element in example_dictionary.items():
#     print("{}는 {}입니다.".format(key, element))





# example_list = ["요소A", "요소B", "요소C"]
# for index, element in enumerate(example_list):
#     print("{}번째 요소는 {}입니다.".format(index, element))





# example_list = ["요소A", "요소B", "요소C"]
# for i in range(len(example_list)):
#     print("{}번째 요소는 {}입니다.".format(i, example_list[i]))




# example_list =["요소A", "요소B", "요소C"]
# i = 0
# for item in example_list:
#     print("{}번째 요소는 {}입니다.".format(i, item))
#     i += 1






# list_a = [1, 2, 3, 4, 5]

# for i in reversed(list_a):
#     print(i)




# # import textwrap

# # 변수를 선언합니다.
# number = int(input("정수 입력> "))

# # if 조건문으로 홀수 짝수를 구분합니다.
# if number % 2 == 0:
#     print(textwrap.dedent("""\
#         입력한 문자열은 {}입니다.
#         {}는 짝수입니다. \
#     """).format(number, number))
# else:
#    print(textwrap.dedent("""\
#         입력한 문자열은 {}입니다.
#         {}는 홀수입니다.\
#    """).format(number, number))



# 변수를 선언합니다.
#numbers = [5, 15, 6, 20, 7, 25]




# # 변수를 선언합니다.
# i = 0

# # 무한 반복합니다.
# while True:
#     # 몇 번째 반복인지 출력합니다.
#     print("{}번째 반복문입니다.".format(i))
#     i = i + 1
#     # 반복을 종료합니다.
#     input_text = input("> 종료하시겠습니까?(y): ")
#     if input_text in["y", "Y"]:
#         print("반복을 종료합니다.")
#         break




# import time

# now_after_5 = time.time() + 5
# output = 0
# while time.time() < now_after_5:
#     output += 1
# print("5초 동안 반복한 횟수:", output)




# i = 0
# while i < 10:
#     print("{}번째 반복입니다.".format((i))
#     i += 1