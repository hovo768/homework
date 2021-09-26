#1
a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a),type(b),type(c),type(d))


# 4.0
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
new_str = ','.join(my_list)
igor_str =f'Привет {new_str[20:25]}!!'
marina_str = f'Привет {new_str.title()[44:50]}!!'
nikloay_str = f'Привет {new_str.title()[74:81]}!!'
aelita_str = f'Привет {new_str.title()[91:]}!!'
print(igor_str)
print(marina_str)
print(nikloay_str)
print(aelita_str)

#4.1
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for new_list in my_list:
    print('Hello', new_list.split()[-1].capitalize(),'!!')

#5

#part 1
prices = [22,12,32,11.3,56,43,30,43,21.2,34.5,33,29]
for price in prices:
    rub = int(price)
    kp = (price - rub)*100
    all = f'{rub} руб {kp:.0f} ккоп.'
    print(all)

#part 2
prices = [22,12,32,11.3,56,43,30,43,21.2,34.5,33,29]
prices.sort()
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    all = f'{rub} руб {kop:.0f} копп'
    print(all)


#part 3
prices = [22,12,32,11.3,56,43,30,43,21.2,34.5,33,29]
prices.sort()
prices.reverse()
for price in prices:
    rub = int(price)
    kop = (price - rub) * 100
    all = f'{rub} руб {kop:.0f} копп'
    print(all)


#part 4
prices = [22,12,32,11.3,56,43,30,43,21.2,34.5,33,29]
prices.sort()
prices.reverse()
prices_2 = prices[:5]
for price in prices_2:
    rub = int(price)
    kop = (price - rub) *100
    print(f'{rub} руб {kop} копп')

#2

my_list = ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)
