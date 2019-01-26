def test():
    print("함수 시작 부분")
    try:
        print("try 구문의 1번 지점")
        ㅔㅐㅔㅐㅔㅔㅐㅔㅐㅔㅐㅔㅐ
    except:
        print("except 구문 1번 지점")
        return
        print("except 구문 2번 지점")
    finally:
        print("finally 구문 지점")
    print("함수 끝 부분")
test()






# try:
#     raise NotADirectoryError("메시지")
# except NotADirectoryError as error:
#     print(error)






# # 변수를 선언합니다.
# list_number = [52, 273, 32, 72, 100]
# # try except 구문으로 예외를 처리합니다.
# try:
#     # 숫자를 입력 받습니다.
#     number_input_a = int(input("정수 입력> "))
#     # 리스트의 요소를 출력합니다.
#     print("{}번째 요소: {}".format(number_input_a, list_number [number_input_a]))
# except IndexError as exception:
#     print("5 미만의 값을 입력해주세요.")
# except ValueError as exception:
#     print("정수를 입력해주세요.")
# except Exception as exception:
#     print("예상하지 못한 예외가 발생했습니다.")



# try:
#     # 숫자로 변환합니다.
#     number_input_a = int(input("정수 입력> "))
#     # 출력합니다.
#     print("원의 반지름:", number_input_a)
#     print("원의 둘레:", 2 * 3.14 * number_input_a)
#     print("원의 넓이:", 3.14 * number_input_a * number_input_a)
# except Exception as e:
#     print(type(e))
#     print(e)





# # 변수를 선언합니다.
# list_input_a = ["52", "273", "32", "스파이", "103"]
# # 반복을 적용합니다.
# list_number = []
# for item in list_input_a:
#     #숫자로 변환해서 리스트에 추가합니다.
#     try:
#         float(item) # 예외가 발생하면 알아서 다음으로 진행 안 되겠지?
#         list_number.append(item) # 예외 없이 통과했으면 리스트에 넣어줘
#     except:
#         pass
# # 출력합니다.
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))






# try + except 구문 조합
# try + except + else 구문 조합
# try + except + finally 구문 조합
# try + except + else + finally 구문 조합
# try + finally 구문 조합





# try:
#     input_a = input("숫자 입력> ")
#     number_input_a = int(input_a)
#     print(number_input_a * number_input_a)
# except:
#     print("예외가 발생했습니다")
# else:
#     print("예외가 발생하지 않았습니다")
# finally:
#     print("반드시 실행되는 코드입니다.")




# try:
#     <예외가 발생할 가능성이 있는 코드>
# except:
#     <예외가 발생했을 때 실행할 코드>
# else:
#     <예외가 발생하지 않았을 때 실행할 코드>
# finally:
#     <무조건적으로 실행할 코드>




# try:
#     input_a = input("정수 입력> ")
#     number_input_a = int(input_a)
#     list_a = [1, 2, 3, 4, 5, 6, 7, 8]
#     print(list_a[number_input_a])
# except:
#     print("뭔지 모르겠지만 예외가 떴다")








# input_a = input("정수 입력> ")
# if input_a.isdigit():
#    number_input_a = int(input_a)
#    list_a = [1, 2, 3, 4, 5, 6, 7, 8]
#    if number_input_a < len(list_a):
#         print(list_a[number_input_a])
#    else:
#         print("리스트의 범위를 넘습니다")
# else:
#     print("너 때문에 프로그램을 종료한다")



# while True:
#     input_a = input("정수 입력> ")
#     if input_a.isdigit():
#         number_input_a = int(input_a)
#         print("원의 반지름:", number_input_a)
#         print("원의 둘레:", 2 * 3.14 * number_input_a)
#         print("원의 넓이:", 3.14 * number_input_a * number_input_a)
#         break
#     else:
#         print("정수를 입력해달라고 했잖아요?!")





# # 숫자를 입력 받습니다.
# number_input_a = int(input("정수 입력> "))

# # 출력합니다.
# print("원의 반지름:", number_input_a)
# print("원의 둘레:", 2 * 3.14 * number_input_a)
# print("원의 넓이:", 3.14 * number_input_a * number_input_a)




# 예외 처리

# 기본 예외 처리
# 예외 → 실행 중에 발생하는 오류
# 실행 중에 발생하는 오류를 미리 처리하는 것 → 예외 처리
# 기본 예외 처리: if 기본적인 방법 -> 예외 처리
# 고급 예외 처리: try except -> 예외 처리