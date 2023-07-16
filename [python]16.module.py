# import module

from module import Friends # module에서 원하는 함수만 들고옴 / module.Friends로 쓸 필요 없음
from module import add_to_N as aN # 별칭 갸능

ho = Friends('Ho', 5)
ho.hello()

print(aN(10))
