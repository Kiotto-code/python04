from new_student import Student

# Student(name='Edward', surname='agle', active=True, login='Eagle', id='asd')
student = Student(name="Edward", surname="agle")
# student = Student(name="Edward", surname="agle", active=True)
# student=Student()
print(student)
# student = Student(name="Edward", surname="agle", active=False,
#                   id="trannxhndgtolvh")
# student = Student(name="Edward", surname="agle", active=False,
#                   login="Eagle")
# student = Student(name="Edward", surname="agle", active=False,
#                   id="trannxhndgtolvh")
# print(student)


# def main():
#     """main() docstring"""
#     student = Student(name="Edward", surname="agle")
#     print(student)

#     try:
#         student = Student(name="Edward", surname="agle", id="toto")
#         print(student)
#     except Exception as e:
#         print(e.__class__.__name__ + ":", e)


# if __name__ == "__main__":
#     main()