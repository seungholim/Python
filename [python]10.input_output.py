# 사용자에게 입력받는 input
# myinput = input("당신의 나이는 몇살입니까?")
# print(myinput)

# 속도가 빠른 입력 함수
# rstrip() : 입력 받은 문자열 마지막 엔터 삭제
import sys
data = sys.stdin.readline().rstrip()
print(data)

# String interpolation
name = "해달"
print("안녕 나는 %s" % name)
print("안녕 나는 " + name)
print("안녕 나는", name)
print("안녕 나는 {}".format(name))
print(f"안녕 나는 {name}")

# print 옵션
# print() sep 옵션
print('a', 'b', 'c', 'd')
print('a', 'b', 'c', 'd', sep='*')

# print() end 옵션
print("안녕 나는 해달") # end = "\n"
print("만나서 반가워")
print("안녕 나는 해달", end="!@#$%")
print("만나서 반가워")

# 입출력
# name = input("이름을 입력해주세요: ")
# age = input("나이를 입력해주세요: ")
# print(f"{name}님의 나이는 {age}세 입니다.")
# age = int(age) + 10
# print(f"{name}님의 10년 뒤 나이는 {age}세 입니다.")

# 간단한 파일 출력
f = open('haedal.txt', 'w')
f.write("Hello Haedal!\n")
f.write("Good Morning!")

print("쓰기 종료")

f.close()

# for문을 활용한 파일 출력
f = open('haedal_for.txt', 'w')

for i in range(100):
    f.write(f"Hello Haedal! {i}\n")

print("쓰기 종료")

f.close()

# 간단한 파일 읽기
print('\n# read()함수')
f = open('haedal.txt', 'r')
a = f.read()
print(a)
f.close()

print('# readlines() 함수')
f = open('haedal.txt', 'r')
b = f.readlines() # 한 줄 씩 읽어서 list에 넣는다.
print(b)
f.close()

print('# readline() 함수')
f = open('haedal.txt', 'r')
c = f.readline() # list에 넣는다.
print(c)
f.close()