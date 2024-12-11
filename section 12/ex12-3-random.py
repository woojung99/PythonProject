import random

for i in range(20):
    r = random.randint(1, 10)
    print(r)
    if r == 1 or r == 10:
        break

#결론! randint는 양끝값 포함

print(random.randrange(10)) # 0~9
print(random.randrange(1, 10)) # 1~9
print(random.randrange(1, 10, 3)) # 1, 4, 7

print(random.random())

if random.random() < 0.5:
        print('집가자')
else:
        print('안돼.. 더 해')

seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
print(random.choice(seasons))

my_list = [1, 2, 3, 4, 5]
print(random.shuffle(my_list))
print(my_list)



