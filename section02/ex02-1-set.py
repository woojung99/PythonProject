#11/21
#4. 세트 제거 메소드
water_type = {'꼬부기', '잉어킹', '라프라스'}
water_type.remove('잉어킹') # 값이 없으면 에러 발생
print('remove 후:', water_type)

water_type.discard('없는 포켓몬') # 값이 없어도 에러 없이 실행
print('discard 후:', water_type)

water_type.pop() # (세트의 경우) 임의 제거, 값이 없으면 에러 발생
print('pop 후:', water_type)

new_type = {'메가이브이', '뮤'}
new_type.clear() # 전체 제거
print('clear 후:', new_type)

