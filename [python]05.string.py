# 기본 문자열
s2 = 'Hello, Haedal'
print(s2)
S2 = "Hello, Haedal!"
print(S2)
s6 = '''Hello, Haedal!'''
print(s6)
S6 = """Hello, Haedal!"""
print(S6)

# 이스케이프 코드
# \n, \t, \\, \', \"

longtext1 = """Hello, Haedal!
My name us Haedal Programming"""
print(longtext1)
longtext2 = """Hello, Haedal!\nMy name us Haedal Programming"""
print(longtext2)

# String Interpolation
a = 123
new_q = f'{a}'
print(new_q)

# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two'))

# pyformat
print('{} {}'. format('one', 'two'))

# f-string
a, b = 'one', 'two'
print(f'{a} {b}')
print(f'{b} {a}')

# 예제 
name = "해달"
eng_name = "Haedal"

print("안녕하세요. {1}입니다. My name is {0}".format(eng_name, name))
print(f'안녕하세요. {name}입니다')

# 문자열 인덱싱
a = "Hello, Haedal!"
print(a[1]) # e

# 문자열 슬라이싱
a = 'Hello, Haedal!'
print(a[4:9])

# 문자열의 길이를 구하는 len()
print(len(a))

# 문자열에서 최대, 최소를 구하는 max(), min()
# 아스키코드
a = '312'
b = 'bac'
c = "ㄱㄴㄷ"
print(min(a), min(b), min(c))
print(max(a), max(b), max(c))

# 소문자, 대문자 변환 lower(), upper()
a = 'this Is AppLE'
print(a.upper())
print(a.lower())

# 문자열을 구분자에 따라 나누는 split()
a = '안녕,나는,해달이야'
print(a.split(sep=','))
b = '안녕 나는 해달이야'
print(b.split())

# 여러개의 문자열 사이에 구분자를 넣어주는 join()
mylist = ['안녕', '나는', '해달']
mystring = '_'.join(mylist)
print(mystring)
