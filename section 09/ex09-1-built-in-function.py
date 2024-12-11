'''
내장함수:
    파이썬에서 제공해 주는 볃도의 import 없이
    사용할 수 있는 함수
'''

# 예제1: 리스트와 관련된 내장 함수들
number = [1, -5, 2, 3, -8, 3, 9, -3, 4, 7, -1]
print('1. 합계:', sum(number))
print('2. 최댓값:', max(number))
print('3. 최솟값:', min(number))
print('4-1. 정렬된 리스트:', sorted(number))
print('4-2. 역정렬된 리스트:', sorted(number, reverse = True))
print('5-1. 절댓값 맵핑:', list(map(abs, number))) # map(적용할 함수, 반복 가능한 객체)
print('5-2. 절댓값 함수:', abs(number[1]))
print('6. 리스트 길이:', len(number))






