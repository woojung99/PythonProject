'''세로편집모드 단축기
alt + shift + insert
'''

students = [
    {'이름':'John', '국어':98, '영어':85, '수학':95},
    {'이름':'Emily', '국어':92, '영어':88, '수학':96},
    {'이름':'Michael', '국어':98, '영어':98, '수학':92},
    {'이름':'Jessica', '국어':88, '영어':82, '수학':78}
]

for student in students:
    print(f'{student['이름']}', end = ' ')
    print(f'{student['국어']}', end = ' ')
    print(f'{student['영어']}', end = ' ')
    print(f'{student['수학']}', end = ' ')
    print()

nike = students[2]
for k, v in nike.items():
    print(f'{k}:{v}')


