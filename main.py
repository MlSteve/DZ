tasks = int(input('Введите кол-во задач: '))
# student_1 = set(filter(lambda x : x.isdigit(),input()))
# student_2 = set(filter(lambda x : x.isdigit(),input()))
student_1 = set(input().replace(' ','').replace(']','').replace('[','').split(','))
student_2 = set(input().replace(' ','').replace(']','').replace('[','').split(','))
print(tasks - len(student_1.union(student_2)))



