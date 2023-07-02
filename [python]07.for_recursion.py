# for문

for i in range(1, 11):
    if(i%2 == 0):
        print(i, "은/는 짝수입니다.")
    else :
        print(i, "은/는 홀수입니다.")

# for문의 구조
# for i in 범위:
#    반복할 명령어

# for문 with list
mylist = ['해달이', '사스미', '메기']

for i in mylist:
    print(i)
print('반복 끝')

# print list with range
print(list(range(10)))
print(list(range(1,11)))
print(list(range(1,20,3)))
print(list(range(20,1,-3)))

# for문 with range
for i in range(1, 11):
    print(i, end=" ")
print('반복 끝')

# 이중 for문
for i in range(10):
    for j in range(1, 11):
        print(j, end=' ')
    print()
