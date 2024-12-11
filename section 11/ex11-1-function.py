def welcome():
    print('Hello', end = '~~~')
    print('My name is woojung')
    print('Welcome to my python world')

print('프로그램 시작')
welcome()
print('프로그램 종료')

def introduce(name, age, job):
    print(f'내 이름은 {name}이고 {age}살이야.')
    print(f'직업은 {job}이고 싶은 취준생이야')


introduce('최우정', 27, '데이터분석가')
print('끝')

def sum_all(*args):
    return sum(args)

s = sum_all(1, 2, 3, 4, 5)
print(s)

def address():
    str = '우편번호 14207\n'
    str += '경기도 광명시 사성로'
    return str

result = address()
print(result)

def plus(num1=500, num2=200):
    return num1 + num2

result = plus(1000) #맨 앞 매개변수에 입력한 것. 두번째에만 입력하는 건 불가능/기본값 있어도 여기에 입력한 인자 우선.
print(result)



