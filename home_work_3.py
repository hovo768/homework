

# 1


def translate_ten(give_number):
    names = {'oen': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'читири',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    return names.get(give_number)

print(translate_ten('ten'))


#2

def translate_ten(give_number):
    names = {'oen': 'один',
            'two': 'два',
            'three': 'три',
            'four': 'читири',
            'five': 'пять',
            'six': 'шесть',
            'seven': 'семь',
            'eight': 'восемь',
            'nine': 'девять',
            'ten': 'десять'}
    if give_number[0] == give_number[0].upper():
        give_number = give_number.lower()
        return names[give_number].capitalize()
    else:
        return names.get(give_number)
print(translate_ten('five'))

#3
'''3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
>>>  thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"], 
    "М": ["Мария"], "П": ["Петр"]
}
Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?'''

def thesaurus(*names):
    out_dict = {}
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict

print(thesaurus('arsen','xoren','antuan','xelar'))


#5
import  random
names = ['кот борис', 'Аркади','Месси', 'Марвин']
times = ['сейчас', 'завто утром', 'вчера', 'вчерком']
doing = ['пилсосит', 'Варует карандаш','шалит', 'борется']

first =random.choices(names)
second = random.choices(times)
thred = random.choices(doing)

def get_jokes(num):
    jokes = []
    for i in range(num):
        for one, two, three in zip(first,second,thred):
            name = one,two,three
        jokes.append(f'{name}')
    return jokes

print(get_jokes(1))
print(get_jokes(2))
