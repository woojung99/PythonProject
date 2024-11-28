'''
enumerate() 함수:
    list, tuple, string 등 자료형을 입력 받으면
    인덱스 값을 포함하는 enumerate 객체 반환
'''

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(month): # month = 인덱스, day = 값
    print(f'{month + 1}월 = {day}일')