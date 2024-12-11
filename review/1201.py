from os import remove

birth_year = 1999
current_year = 2024
print(f'현재 내 한국 나이는 {current_year - birth_year + 1} 입니다.')
print(f'현재 내 만 나이는 {current_year - birth_year} 입니다.')
age = current_year - birth_year
print(f'현재 나이의 2배: {age * 2}')
print(f'현재 나이의 제곱: {age ** 2}')

potions = 17
team_size = 4
per_member = potions // team_size
remainder = potions % team_size
print(f'팀원당 포션은 {per_member}이고 남는 포션은 {remainder:.1f}')

hp, mp = 100, 50
hp, mp = mp, hp
print(hp, mp)

exp = 0
for i in range(1, 11):
    exp += 5

print(f'반복문 이후 exp 값: {exp}')

a = 10
b = 0
print(f'not {a}: {not a}')
print(f'not {b}: {not b}')

print(not True)
print(not a < b)

a = 6
b = 5
print(f'a & b: {a & b}')
print(f'a | b: {a | b}')
print(f'a ^ b: {a ^ b}')
print(a << 1)
print(b >> 1)
print(a >> 1)

a = 20
b = 100
result = (a - b) if (a > b) else (b - a)
print(result)

age = 15
if age >= 20:
    print('성인입니다.')
elif age >= 13:
    print('청소년입니다.')
elif age >= 8:
    print('어린이입니다.')
else:
    print('영유아입니다.')

print('프로그램이 종료됩니다.')

import random
choices = ['가위', '바위', '보']
computer = random.choice(choices)






