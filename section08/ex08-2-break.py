i = 0
while i < 7:
    j = 0
    while j < i + 1:
        print('*', end = '')
        if j == 3:
            break #안쪽 while 문을 break
        j += 1
    print()
    i += 1




