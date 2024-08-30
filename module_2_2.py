from time import process_time
#1-й вариант решения задачи:
first = 20
second = 20
third = 20
if first == second and second == third and first == third:
    print(3)
elif second==third and third==second:
    print(2)
else:
    print(0)

first = 10
second = 20
third = 20
if first == second and second == third and first == third:
    print(3)
elif second==third and third==second:
    print(2)
else:
    print(0)

first = 10
second = 20
third = 30
if first == second and second == third and first == third:
    print(3)
elif second==third and third==second:
    print(2)
else:
    print(0)

#2-й вариант решения задачи:
first = 10 #2 этап: 30; 3этап: 20 --> 10
second = 20 #2 Этап: 30; 3этап: 20 --> 20
third = 30 #2 этап:30; 3этап: 30 --> 30

while first != second and second != third and first != third:
        second = second + first
        first = second + third - third
        if first == second and second == third and first == third:
            print(3)
            while second == third and third == second:
                first = second - 10
                second = second - 10
            if first == second and second == first:
                print(2)
if first != second and second != third and first != third:
    print(0)
    while first != second and second != third and first != third:
        first = first - 10
print(0)