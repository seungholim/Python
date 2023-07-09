# Class

# 클래스-붕어빵 틀 만들기
class FishBread:
    # 클래스 변수
    banjook = "밀가루"

    # 매소드 만들기
    # 붕어빵 굽기
    def make_FB(self, ingredient, price):
        self.ingredient = ingredient
        self.price = price
    
    # 붕어빵 살펴보기
    def see_FB(self):
        print(self.ingredient, self.price)

    # 클래스 메소드
    def see_banjook(cls): #cls를 매개변수로 받는다.
        print(cls.banjook)

# 객체(인스턴스)-붕어빵 만들기
a = FishBread()
b = FishBread()
print(type(a))

a.see_banjook()
b.see_banjook()
FishBread.banjook = "콩가루"
a.see_banjook()
b.see_banjook()

a.make_FB("팥", 400)
b.make_FB("슈크림", 500)

a.see_FB()
b.see_FB()