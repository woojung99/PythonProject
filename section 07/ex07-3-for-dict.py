
eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}

for word in eng_dict: # word는 사전 내 키 값
    print(f'{word}의 뜻: {eng_dict[word]}')

eng_dict_keys = eng_dict.keys()
for k in eng_dict_keys:
    print(f'eng_dict의 key: {k}')

eng_dict_values = eng_dict.values()
print(eng_dict_values)
for v in eng_dict_values:
    print(f'eng_dict의 value: {v}')

