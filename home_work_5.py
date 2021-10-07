from itertools import zip_longest
#2
gen_1 = (i for i in range(1,16,2))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
# print(next(gen_1))

#3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen_2 = ((tutors1, klasses1) for tutors1, klasses1 in zip_longest(tutors,klasses))
print(tuple(gen_2))

#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_list = [nums for i, nums in enumerate(src) if nums > src[i - 1] and i != 0]
print(num_list)

#5
src_2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [num for num in src_2 if src_2.count(num) == 1]
print(result)