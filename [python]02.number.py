# 정수형
a = 154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

# 모두 정수형

# 실수형
b = 181.34
print(type(b))
b = -22.22
print(type(b))
b = 1e9
print(type(b), b)

# 컴퓨터는 실수를 정확하게 표기하지 못한다. : round 함수 이용
a = 0.3
b = 0.6

print(a+b, 0.9==(a+b))
print(round(a+b, 1), round(a+b, 1)==0.9)

# 복소수형
c = 1 + 4j
print(type(c))
print(c.real) # 1.0
print(c.imag) # 4.0
print(c.conjugate()) # (1-4j)
print(abs(c)) # 크기 : 루트(1 + 4*4 = 17) 4.123105625617661

# 예제
a = 5
b = 3.14
c = 3+4j

print(10*a + 3*b + c)
