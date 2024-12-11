print('10자리 폭 왼쪽 정렬 "{:<10d}"'.format(123)) #문자열을 ''로 묶었을 때 그 안에 다시 ''사용시 오류
print('10자리 폭 오른쪽 정렬 {:>10d}'.format(123))
print('10자리 폭 가운데 정렬 "{:^10d}"'.format(123))

print('10자리 폭 왼쪽 정렬 채움문자 "{:*<10d}"'.format(456))

s = '-'.join('Merry Christmas') #공백도 한 문자로 인식
s = '-'.join('MerryChristmas')
print(s)

s = '-'.join(['010', '3523', '5933'])
print(s)

s = '010-3523-5933'
result = s.split('-') #구분 기호를 기준으로 잘라 리스트 저장
print(f'전화번호 마지막 4자리: {result[2]}')
print(f'010-****-{result[2]}')

s = '   starbucks         '
result = s.strip()
print(f'"{result}"')

s = '     star   b uck  s     '
result = s.replace(' ', '')
print(f'나 지금 어디~~게~~? {result}')

new_result = s. replace('b uck  s', '다방')
print(new_result)




