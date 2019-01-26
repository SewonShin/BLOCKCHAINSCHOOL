


# 범위 만들기
## 0부터 (<숫자> - 1)까지의 정수로 범위를 만듭니다.
range(<숫자1>)
## <숫자1>부터 (<숫자2> - 1)까지의 정수로 범위를 만듭니다.
range(<숫자1>, <숫자2>)
## <숫자1>부터 <숫자3> 만큼의 차이를 가진 (<숫자2> - 1)까지의 정수로 범위를 만듭니다.
range(<숫자1>, <숫자2>, <숫자3>)

# 범위와 반복문
for <범위 내부의 숫자를 담을 변수> in <범위>:
    <코드>



# # 딕셔너리 생성
# dict_a = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"
# }

# for key in dict_a:
#     print(key)
#     print(dict_a[key])
#     print("-" * 10)




# # 딕셔너리 생성
# dict_a = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient":["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀"
# }
# name_value = dict_a.get("name")
# if name_value != None:
#     print(name_value)
# else:
#     print("키가 존재하지 않습니다")


  
# # 딕셔너리 생성
# dict_a = {
#     "name": "7D 건조 망고",
#     "type": "당절임",
#     "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
#     "origin": "필리핀",
# }
# print(dict_a["name"])
# print(dict_a["type"])
# print(dict_a["ingredient"])
# print(dict_a["ingredient"][0])
# print(dict_a["ingredient"][1])


# # 딕셔너리
# (일반적으로) 문자열을 기반으로 값을 저장하는 것
# {
#     <키>: <값>,
#     <키>: <값>,
#     ...
#     <키>: <값>
# }

# 예) 리스트: list_a[1] → 인덱스
# 예) 딕셔너리: dict_a["name"] → 키

# # 딕셔너리 처리
# - 추가: dict_a["new_name"] = 10 # 그냥 때려 넣으면 OK
# - 제거: del dict_a["name"]
# - 확인: key in dict_a