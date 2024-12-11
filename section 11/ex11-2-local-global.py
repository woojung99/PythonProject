gVar = '전역'

def global_and_local():
    lVar = '지역'
    #global gVar
    gVar = '뉴 전역'
    print(f'{lVar} 변수입니다슬기')
    print(f'{gVar} 변수입니다람쥐') #여기엔 '뉴 전역'으로 나오지만

global_and_local()
print(gVar) #여긴 여전히 '전역"