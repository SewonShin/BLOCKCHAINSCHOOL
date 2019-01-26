class Test:
    def __init__(self):
        









# # 클래스 선언
# class Student:
#     count = 0
#     # 생성자
#     def __init__(self, name, korean, math, english, science):
#         Student.count += 1
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science

#     @classmethod
#     def count(cls):
#         print(Student.count)

# Student.count()

# a = Student()
# a.count()

# print(student_count)







# # 클래스 선언
# class Student:
#     # 생성자
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science
#     def get_average(self):
#         return self.get_sum() / 4
#     def __str__(self):
#         return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
#     def __eq__ (self, value):
#         print("eq 함수가 호출되었습니다")
#         return 0

# # 학생 리스트를 선언합니다.
# a = Student("윤인성", 87, 98, 88, 95)
# a == a




 


# # 클래스 선언
# class Student:
#     # 생성자
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science
#     def get_average(self):
#         return self.get_sum() / 4
#     def to_string(self):
#         return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())



# # 학생 리스트를 선언합니다.
# students = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 92, 98, 96, 98),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 98, 92, 96, 92),
#     Student("윤아린", 95, 98, 98, 98),
#     Student("윤명월", 64, 88, 92, 92),
#     Student("김미화", 82, 86, 98, 88),
#     Student("김연화", 88, 74, 78, 92),
#     Student("박아현", 97, 92, 88, 95),
#     Student("서준서", 45, 52, 72, 78)
# ]

# #학생 한 명씩 반복합니다.
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     #출력합니다.
#     print(student.to_string())







# # 딕셔너리를 리턴하는 함수를 선언합니다.
# def create_student(name, korean, math, english, science):
#     return {
#         "name": name,
#         "korea": korean,
#         "math": math,
#         "english": english,
#         "science": science
#     }

# # 학생을 처리하는 함수를 선언합니다.
# def student_get_sum(student):
#     return student["korean"] + student["math"] + student["english"] + student["science"]
# def student_get_average(student):
#     return student_get_sum / 4
# def student_to_string(student):
#     return "{}\t{}\t{}".format(student["name"]), student_get_sum(student), student_get_average(student))



# # 학생 리스트를 선언합니다.
# students = [
#     create_student("윤인성", 87, 98, 88, 95),
#     create_student("연하진", 92, 98, 96, 98),
#     create_student("구지연", 76, 96, 94, 90),
#     create_student("나선주", 98, 92, 96, 92),
#     create_student("윤아린", 95, 98, 98, 98),
#     create_student("윤명월", 64, 88, 92, 92),
#     create_student("김미화", 82, 86, 98, 88),
#     create_student("김연화", 88, 74, 78, 92),
#     create_student("박아현", 97, 92, 88, 95),
#     create_student("서준서", 45, 52, 72, 78)
# ]





# # 학생의 리스트를 선언합니다.
# students =[
#     {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95 },
#     {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98 },
#     {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90 },
#     {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92 },
#     {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98 },
#     {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92 },
#     {"name": "김미화", "korean": 82, "math": 86, "english": 98, "science": 88 },
#     {"name": "김연화", "korean": 88, "math": 74, "english": 78, "science": 92 },
#     {"name": "박아연", "korean": 97, "math": 92, "english": 88, "science": 95 },
#     {"name": "서준서", "korean": 45, "math": 52, "english": 72, "science": 78 }
# ]

# # 학생을 한 명씩 반복합니다.
# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     # 점수의 총점과 평균을 구합니다.
#     score_sum = student["korean"] + student["math"] +\
#         student["english"] + student["science"]
#     score_average = score_sum / 4
#     # 출력합니다.
#     print(student["name"], score_sum, score_average, sep="\t")





# import test_module as tm

# print("메인 파일입니다")
# print(__name__)

# clsimport test_module as tm

# print(tm.PI)
# input_num = tm.number_input()
# print(input_num)