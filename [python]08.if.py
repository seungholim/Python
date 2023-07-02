# 조건문 : 특정 조건을 만족할 때 명령어를 수행하자
# if, if-elif-else

# 시험 점수에 따른 과락 분류
score = int(input("점수를 입력하세요 "))
if score >= 70:
    result = "통과"
elif score >= 60:
    result = "재시험"
else:
    result = "과락"
    
print(result)
