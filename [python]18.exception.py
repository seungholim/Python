# # # 예외처리
# # print("program start")

# # try:
# #     arr = ['b', 'l', 'o', 'g']
# #     print(arr[8]) #error
# #     print('==mid')
# # except:
# #     print("==error! but still alive")
    
# # print("program end")

# # try + finally : finally는 에러 발생 여부와 상관없이 무조건 실행
# # print("program start")

# # try:
# #     arr = ['b', 'l', 'o', 'g']
# #     print(arr[8]) #error
# #     print('==mid')
# # finally:
# #     print("finally") # 무조건 출력
    
# # print("program end")

# # try + except + finally
# # print("program start")

# # try:
# #     arr = ['b', 'l', 'o', 'g']
# #     print(arr[8]) #error
# #     print('==mid')
# # except:
# #     print("error!") # finally보다 먼저 들름
# # finally:
# #     print("finally") # 무조건 출력
    
# # print("program end")

# # # try + except + else + finally
# print("program start")

# try:
#     arr = ['b', 'l', 'o', 'g']
#     # print(arr[0]) #not error
#     print(arr[8]) #error
#     print('==mid')
# except:
#     print("error!") # 오류 처리시 error -> finally
# else:
#     print("else") # 정상 처리시 else -> finally
# finally:
#     print("finally") # 무조건 출력
    
# print("program end")

# # try + except + else
# print("program start")

# try:
#     arr = ['b', 'l', 'o', 'g']
#     print(arr[8]) #error
#     print('==mid')
# except IndexError:
#     print("Index error!")
# except:
#     print("another error!")
# else:
#     print("else") # except 없이는 작성 불가
    
# print("program end")

# raise : 의도된 오류 발생

# a = int(input("1~5까지 숫자 입력 : "))

# # 범위 밖이면 에러 발생
# if a < 1 or a > 5 :
#     raise ValueError #에러 종류

# print(f"입력한 a는 {a}입니다.")

# # 에러 메세지
a = int(input("1~5까지 숫자 입력 : "))

if a < 1 or a > 5 :
    raise Exception("에러에러에러!!")
    
    # ValueError : 잘못된 값이 들어왔을 때
    # IndexError : 범위 초과
    # SyntaxError : 파이썬 문법에 맞지 않을 때
    # NameError : 변수 이름을 찾을 수 없을 때
    # ZeroDivisionError : 0으로 나눌 때

print(f"입력한 a는 {a}입니다.")