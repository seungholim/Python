# 함수 정의

# def 함수명(매개변수):
#     명령어1
#     명령어2
#     ...
#     return 결과

# docstring
def hello_docstring():
    '''
    여기는 함수의 문서화 내용입니다.
    '''
    print("Hello DocString")

# 함수의 공식 설명을 출력해보자
# help(hello_docstring)
# print(hello_docstring.__doc__)
hello_docstring()

print(print.__doc__)
print(input.__doc__)

# 간단한 덧셈 함수
def add_two_num(a, b):
    print("덧셈 중")
    result = a+b
    return result

value = add_two_num(10, 13)
print(value)

# return이 발생하면 함수가 종료
def return_example(a, b):
    if a>b :
        print("해달이")
        return
    else:
        print("부기")
    print("아리")

return_example(10, 20)
return_example(30, 20)


# 인수의 순서를 바꿔보기
def add_two_num(a, b):
    print("덧셈 중")
    print(a, b)
    result = a+b
    return result

value = add_two_num(b = 10, a = 13) # 매개변수를 지칭해주면 순서에 상관없이 넣을 수 있다.

# 매개변수에 기본값을 넣어주자
def add_two_num(a=100, b=30):
    print("덧셈 중")
    result = a+b
    return result

value1 = add_two_num(10, 13)
value2 = add_two_num(10)
value3 = add_two_num(b=10)
value4 = add_two_num()

print(value1, value2, value3, value4)

# 가장 뒤의 변수부터 기본값 지정
# def add_two_num(a=100, b): # 불가능
#     ...
# def add_two_num(a, b=30): # 가능
#     ...

# 여러 값을 받는 함수
def people_num(*args):
    print("공부하는 학생 수는? : ", end='') # end='\n'를 ''로 번경
    result = len(args)
    return result

value = people_num("해달이", "사스미", "시라용", "부기", "메기")
print(value, '명')

# lambda 표현식
# 특정 기능을 수행하는 함수를 한줄로 작성 가능

def add(a, b):
    return a+b

# 일반적인 add 메서드 사용
print(add(3, 7))

# 람다 표현식 사용
print((lambda a, b: a+b)(3, 7))