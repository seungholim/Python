# 리스트
# 리스트_이름 = [요소1, 요소2, 요소3, ...]

# 해달 프렌즈
Haedal_character = ["해달이", "시라용", "아리", "메기", "사스미"]

# 빈 리스트
my_list = []
print(my_list)

# 파이썬 리스트 특징 : 요소들의 자료형 통일하지 않아도 됨
my_list = [1, 2, "해달이", True, ['a', 'b', 'c']]
print(my_list)

# 리스트 컴프리핸션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

#1부터 9까지 수의 제곱을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]

print(array)

# 리스트 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0]) # 1
print(a[5]) # 6
print(a[9]) # 10

# 음수 인덱싱
print(a[-1]) # 10
print(a[-5]) # 6

# 리스트 슬라이싱
print(a[0:3])
print(a[:3])
print(a[7:])
print(a[:])
print(a[-4:-2])

# 리스트 수정
a[0] = 100
print(a)

# 리스트 삭제
del a[0]
print(a)
del a[3:]
print(a)

# 리스트 길이를 구하는 len()
print(len(a))

# 리스트의 값을 추가해주는 append()
mylist = ['a', 'b', 'c', 'd']
mylist.append('e')
print(mylist)

mylist = [4, 2, 3, 1]
mylist.sort()
print(mylist)

# 리스트 뒤집기
mylist.sort(reverse=True)
print(mylist)

# insert()
mylist.insert(3, 5)
print(mylist)

# remove()
mylist.remove(5)
print(mylist)

# count()
mylist.append(5)
print(mylist.count(5))
