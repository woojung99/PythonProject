'''
미리 만들어 놓은 converter module을 써보자!!!
'''
#방법 1) import converter: converter. 으로 불러옴
#방법 2: converter. 빼고 바로 함수명 가져와야함/일부만 가져오는 것도 가능
from converter import *

mile = kilometer_to_mile(5)
print(mile)

pound = gram_to_pound(5)
print(pound)

