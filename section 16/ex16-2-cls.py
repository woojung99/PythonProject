'''
클래스 변수:
    클래스를 기반으로 만든 모든 인스턴스(객체)가 공유할 수 있는 변수

인스턴스 변수 (멤버 변수):
    해당 인스턴스만 사용하는 값

클래스 메서드:
    인스턴스가 없어도 클래스를 이용해 호출할 수 있다.
    cls 키워드를 이용해 클래스를 메서드 안에서 클래스 변수 접근 가능
'''

class Bag:
    count = 0 # 클래스 변수/ 객체 생성 없이도 사용 가능

    def __init__(self):
        Bag.count += 1

    @classmethod # @표시 데코레이터
    def sell(cls):
        cls.count -= 1 # 클래스 변수인 count에 -1

    @classmethod
    def remain_bag(cls):
        return cls.count

    @staticmethod
    def slogan():
        print('명품 주인을 찾습니다')






