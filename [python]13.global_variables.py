# 전역변수와 지역변수

def add_two_num(a, b):
    print("덧셈 중")
    result = a+b
    return result # 지역변수

result = 0 # 전역변수
add_two_num(10, 13)
print(result)

# 매개변수와 인수

def add_two_num(a, b): # 매개변수
    print("덧셈 중")
    result = a+b
    return result

a = 10
b = 13

value = add_two_num(a, b) # 인수
print(value)