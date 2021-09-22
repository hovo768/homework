
#1
duration = int(input('введите время в секундах: '))
d = 84600
h = 3600
m = 60
days = duration // d
hours = (duration - (days * ( d ))) // h
minutes = ((duration - days * d) - (hours * h)) // m
seconds = duration % m
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')


#2
my_list = [x**3 for x in range(1, 1000, 2)]
final_number = 0
for num in my_list:
    check_sum = 0
    for check_number in str(num):
        check_sum += int(check_number)
    if check_sum % 7 == 0:
        final_number += num
print(final_number)

final_number = 0
for num in my_list:
    num += 17
    check_sum = 0
    for check_number in str(num):
        check_sum = check_sum + int(check_number)
    if check_sum % 7 == 0:
        final_number = final_number + num
print(final_number)


#3
indx = 1
while indx < 101:
    if indx == 1:
        print(indx, 'процент')
    elif indx == 2 or indx == 3 or indx == 4:
        print(indx, 'процента')
    else:
        print(indx, 'процентов')
    indx+=1