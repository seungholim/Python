# 튜플
# () 소괄호 사용
# 한번 선언된 값을 변경할 수 없다.

a = (1, 2, 3, 4)
print(a)

# a[1] = 7 # 에러

# 사전
# 키와 값을 쌍으로 가지는 자료형

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)
print(data['사과'])

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 답은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list, value_list)

for key in key_list:
    print(data[key])

# 집합
# 중복을 허용하지 않는다.
# 순서가 없다
# 중괄호{} 사용

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합
