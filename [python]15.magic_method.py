# Magic Method
# 함부로 수정할 수 없는 변수 연산

class FishBread:
    def __init__(self, ingredient, price):
        self.__ingredient = ingredient # 변수들 앞에 언더바를 2개 넣어준다
        self.__price = price
    
    def __str__(self):
        return '{} 붕어빵, 가격 {}원'.format(self.__ingredient, self.__price)

    def __add__(self, other): # +연산자에 덮어쓰기
        return self.__price + other.__price

a = FishBread("팥", 400) # __init__
b = FishBread("슈크림", 500) # __init__

print(a) # __str__
print(b) # __str__

print('붕어빵 a,b 합쳐 %d원' % (a+b)) # __add__
