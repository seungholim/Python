### 목차

---

[1. 변수](#변수)  
   - [변수 이름 규칙](#변수-이름-규칙)
   - [PEP-8 : 파이썬 코딩 스타일 가이드](#코딩-스타일-가이드)
   - [숫자](#숫자)
      * [정수형](#정수형)
      * [실수형](#실수형)
      * [복소수형](#복소수형)
   - [불](#불)
   - [리스트](#리스트)
      * [빈 리스트 선언](#빈-리스트-선언)
      * [리스트 컴프리헨션](#리스트-컴프리헨션)
      * [2차원 리스트 초기화](#2차원-리스트-초기화)
      * [인덱스](#인덱스)
      * [슬라이싱](#슬라이싱)
      * [수정](#수정)
      * [리스트 관련 함수](#리스트-관련-함수)
         * 길이 len()
         * 요소 추가 append()
         * 정렬 sort()  
         * 뒤집기 reverse()
         * 요소 삽입 insert()
         * 요소 제거(by 값) remove()
         * 요소 제거(by 인덱스) del
         * 요소 개수 count()
   - [문자열](#문자열)
      * [엔터 인식](#엔터-인식)
      * [String Interpolation](#String-Interpolation)
      * [문자열 표기 방식](#문자열-표기-방식)
         * 문자열 옛날 방식
         * pyformat
         * f-string
      * [인덱싱](#인덱싱)
      * [슬라이싱](#슬라이싱)
      * [문자열 관련 함수](#문자열-관련-함수)
         * len()
         * min(), max()
         * lower(), upper()
         * split()
         * join()
   - [튜플](#튜플)
   - [사전](#사전)
      * [사전 자료형 관련 함수](#사전-자료형-관련-함수)
         * keys & values 
   - [집합](#집합)
      * [집합 자료형 연산](#집합-자료형-연산)
         * 합집합
         * 교집합
         * 차집합
      * [집합 자료형 함수](#집합-자료형-함수)
         * add
         * update
         * remove
    
[2. 반복문](#반복문)  
   - [for](#for)
   - [while](#while) 
   - [break](#break)
   - [continue](#continue)
    
[3. 조건문](#조건문)  
   - [if-elif-else](#if-elif-else)
   - [삼항 연산자](#삼항-연산자)
   
[4. 입출력](#입출력)  
   - [input()](#input)
   - [sys.stdin.readline().rstrip()](#입력-속도가-빠른-입력함수)
   - [print()](#print)
      * sep
      * end
   - [파일 출력](#파일-출력)
   - [파일 읽기](#파일-읽기)  
      * read()
      * readline()
      * readlines()
   
[5. 함수](#함수)  
   - [함수 정의](#함수-정의)
   - [Docstring](#Docstring)
   - [return](#return)
   - [매개변수와 인수](#매개변수와-인수)
   - [인수 순서 변경](#인수-순서-변경)
   - [매개변수 기본값 지정](#매개변수-기본값-지정)
   - [여러 값을 받는 함수](#여러-값을-받는-함수)  
   - [람다 표현식](#람다-표현식)
   
[6. 전역변수](#전역변수)  
   - [전역 변수와 지역 변수](#전역-변수와-지역-변수)
   - [함수 내에서 전역 변수 호출](#함수-내에서-전역-변수-호출)
   
[7. 클래스](#클래스)
   - [구성요소](#구성요소)
   - [객체(인스턴스)](#객체)
   - [Underbar Variable](#Underbar-Variable)
   - [Magic Method](#Magic-Method)
   
[8. 상속](#상속)  
[9. 모듈](#모듈)  
   - [모듈 불러오기](#모듈-불러오기)
   
[10. 패키지](#패키지)  
   - [구성요소](#구성요소)
   - [패키지 불러오기](#패키지-불러오기)

[11. 예외 처리](#예외-처리)  
   - [try-except](#try-except)
   - [finally](#finally)
   - [else](#else)
   - [raise](#raise)
      - [에러 메세지](#에러-메세지)
   - [주요 에러](#주요-에러)

---

## 변수
   - ### **변수 이름 규칙**  
     * 영문자(대, 소문자 구분), 숫자, 언더바, 한글 사용 가능
     * 첫 자리는 숫자 사용 불가
     * 예약어 사용 불가

   - ### **코딩 스타일 가이드**  
     [PEP-8](https://www.python.org/dev/peps/pep-0008/)  
     
     * 한 단어로 된 변수는 소문자로 적는다.
     
        ``` python
        age, good, name
        ```

     * 두 단어 이상의 변수는 언더바로 구분한다.
     
        ``` python
        my_name, my_friend_name
        ```
     
     * 예약어와 충돌하는 경우에는 뒤에 언더바를 붙인다.
     
        ``` python
        if_, true_
        ```
     
     * 상수의 경우 대문자와 언더바를 혼용하여 쓴다
     
        ``` python
        TOTAL, MAXX_NUM, AVG
        ```
     
     
   - ### **숫자**
   
     정수형, 실수형, 복소수형이 있다.  
     
       * #### **정수형**
       
       int형이라고도 불린다.
          ``` python
          a = 154
          a = 0
          a = -25
          ```
       
       * #### **실수형**
       
          지수 표현식(1.23e-2)으로도 입력 가능
          ``` python
          b = 181.84
          b = -22.22
          b = 1e9 # 지수표현식 : 10 x 10^9
          ```
       
          컴퓨터는 데이터를 2진수로 처리하기 때문에 실수를 정확하게 표현할 수 없다.  
          때문에 round()함수를 이용하여 처리한다.
          ```
          a = 0.3
          b = 0.6

          print(a+b, 0.9==(a+b))
          print(round(a+b, 1), round(a+b, 1)==0.9)

          # result :
          # 0.899999999999999 False
          # 0.9 True
          ```
       
       * #### **복소수형**
       
          ``` python
          c = 1+4j

          print(c.real) # 실수부 1.0
          print(c.imag) # 허수부 4.0
          print(c.conjugate()) # 켤레복소수 (1-4j)
          print(abs(c)) # 크기 : 루트(1 + 4*4 = 17) 4.123105625617661
          ```
       
   - ### **불**  
   
     True, False로 구분된다
     
     ``` python
     a = True
     b = False

     x = 1
     y = 2

     print(x>y) # False
     print(x<y) # True
     ```
   - ### **리스트**  
   
     파이썬 리스트는 요쇼들의 자료형이 동일하지 않아도 된다.
     
     ``` python
     # 해달 프렌즈
     Haedal_character = ["해달이", "시라용", "아리", "메기", "사스미"]

     # 파이썬 리스트 특징 : 요소들의 자료형 통일하지 않아도 됨
     my_list = [1, 2, "해달이", True, ['a', 'b', 'c']]
     print(my_list)
     ```
     
     * #### **빈 리스트 선언**
     
        ```python
        # 1
        my_list = []
        print(my_list)

        # 2
        a = list()
        print(a)

        # 3 기가 N이고 모든 값이 0인 list 선언
        n = 10
        b = [0] * n
        print(b)

        # result :
        # []
        # []
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ```
     
     * #### **리스트 컴프리헨션**
     
        리스트를 초기화하는 방법 중 하나  
        대괄호 안에 조건문과 반복문을 넣어 초기화 가능  
        ```python
        # 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
         array = [i for i in range(20) if i % 2 == 1]
         print(array)

        # result
        # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

        # 1부터 9까지 수의 제곱을 포함하는 리스트
         array = [i * i for i in range(1, 10)]
         print(array)

        # result
        # [1, 4, 9, 14, 25, 36, 49, 84, 81]
        ```
     
     * #### **2차원 리스트 초기화**
     
        리스트 컴프리헨션을 이용하여 2차원 리스트를 초기화할 수 있다.  
        ```
        # 2차원 리스트 초기화
         n = 3
         m = 3
         array = [[0] * m for _ in range(n)]

         print(array)

         # result
         # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        ```

        *단, 아래와 같은 방식으로 초기화하면 안된다.*  
        이 경우, 내부에 포함된 리스트들이 같은 레퍼런스로 인식되기 때문에  
        하나의 성분 값을 바꾸면 다른 리스트 역시 전부 바뀐다.
        ```
        # 잘못된 방법

         n = 3
         m = 3
         array = [[0] * m] * n

         a[1][1] = 5

         print(array)

         # result
         # [[0, 0, 0], [0, 5, 0], [0, 5, 0]] : 모두 바뀜!
        ```
     
     * #### **인덱스**
     
        자료의 처음 인덱스는 0부터 시작한다.  
        음수로 인덱싱 가능하며 이때는 0부터 시작하지 않고 -1부터 시작한다.

        ``` python
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        print(a[0]) # 1
        print(a[5]) # 6
        print(a[9]) # 10

        print(a[-1]) # 10
        print(a[-5]) # 6
        ```
     
     * #### **슬라이싱**
     
        리스트를 자를 때는 리스트이름[A:B]로 자른다.  
        A나 B는 생략 가능하며 생략 시 처음부터/마지막까지 라는 의미이다.  
        A부터 B 직전까지 잘린다.

        ``` python
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        print(a[0:3]) # [1, 2, 3]
        print(a[:3]) # [1, 2, 3]
        print(a[7:]) # [8, 9, 10]
        print(a[:]) # 전체
        print(a[-4:-2]) # [7, 8, 9]
        ```
     
     * #### **수정**
     
        리스트는 수정할 수 있다.

        ``` python
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        a[0] = 0

        # result : [0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ```
     * #### **리스트 관련 함수**

        * **리스트 길이 구하기 : len()**

           리스트의 길이를 반환한다.

           ``` python
           a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           print(len(a))

           # result : 10
           ```

        * **리스트 성분 추가 : append()**

           리스트의 끝에 data를 추가한다.

           ``` python
           a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           a.append(11)

           # result : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
           ```

        * **리스트 정렬 : sort()**

           리스트를 정렬한다.
           리스트를 내림차순으로 정렬할 경우에는 sort(reverse=True)로 할 수 있다.

           ``` python
           a = [4, 2, 3, 1]

           a.sort()

           # 결과 : [1, 2, 3, 4]

           a = [4, 2, 3, 1]
           a.sort(reverse=True)

           # result : [4, 3, 2, 1]
           ``` 

        * **reverse()**

           리스트를 뒤집어준다  
           ```python
           a.reverse()

           # result : [1, 2, 3, 4]
           ```

        * **insert()**

           insert(위치, 데이터)로 쓰이며 리스트[위치]에 성분을 삽입해준다.
           ``` python
           mylist = [4, 2, 3, 1]

            mylist.insert(3, 5)
            print(mylist)

            # result : [4, 3, 2, 5, 1]
           ```

        * **remove()**

           리스트(값)으로 쓰이며 리스트에서 *해당 값을 검색*해 제거해준다.
           ```python
           mylist = [1, 2, 5, 3, 4]
            mylist.remove(5)
            print(mylist)

            # result : [1, 2, 3, 4]    
           ```

        * **del**

           del list(index)로 쓰이며 *해당 인덱스의 값*을 삭제해준다.

           ``` python
           a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           del a[0]

           # result : [2, 3, 4, 5, 6, 7, 8, 9, 10]

           b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           del b[3:]

           # result : [1, 2, 3]
           ```

        * **count()**

           리스트 내에서 값의 개수를 검색해 준다.
           ```python
           mylist = [1, 2, 5, 3, 4]
            mylist.append(5)
            print(mylist.count(5))

            # result : 1
           ```
   
   - ### **문자열**  
   
     '나 " 혹은 '''나 """(docstring)를 통해 사용한다.  
     ``` python
     s2 = 'Hello, Haedal'
     S2 = "Hello, Haedal!"
     s6 = '''Hello, Haedal!'''
     S6 = """Hello, Haedal!"""
     ```
     
     * #### 엔터 인식
     
        엔터를 인식 시키는 방법으로는 

        * 이스케이프 코드를 활용
        * docstring(ex: ''' or """) 활용  

        이 있다.  

        ``` python
        # 이스케이프 코드
        # \n, \t, \\, \', \", 등

        longtext1 = """Hello, Haedal!
        My name us Haedal Programming"""
        longtext2 = """Hello, Haedal!\nMy name us Haedal Programming"""

        # result :

        # Hello, Haedal!
        # My name us Haedal Programming
        # Hello, Haedal!
        # My name us Haedal Programming
        ```
     
     * #### **String Interpolation**
     
     
         ``` python
         a = 123
         new_q = f'{a}'
         print(new_q)

         # result : 123
         ```
       
      * #### **문자열 표기 방식**
      
        문자열 표기 방식에는 문자열 옛날 방식, pyformat, f-string이 있다.  
         * 문자열 옛날 방식
         
         ``` python
         # 문자열 옛날 방식
         print(f'%s %s' % ('one', 'two')) 
         ```
         * pyformat
         ``` python
         # pyformat
         print('{} {}'. format('one', 'two'))
         ```
         * f-string
         ``` python
         # f-string
         a, b = 'one', 'two'
         print(f'{a} {b}')
         print(f'{b} {a}')
         ```
     
     * #### **인덱싱**
      ``` python
        # 문자열 인덱싱
        a = "Hello, Haedal!"
        print(a[1]) # e
        ```
        
     * #### **슬라이싱**
     
        문자열 역시 리스트이므로 리스트와 동일하다.  

        ``` python
        # 문자열 슬라이싱
        a = 'Hello, Haedal!'
        print(a[4:9])
        ```
        
     * #### **문자열 관련 함수**

        * **len()**

           문자열의 길이를 구한다. 

           ``` python
           a = "Hello, Haedal!"
           print(len(a))

           # result : 14
           ```

        * **문자열 내 최대, 최소 min(), max()**

           문자열 내에서 아스키 코드를 비교하여 최대, 최소 문자를 구하는 함수  

           ``` python
           a = '312'
           b = 'bac'
           c = "ㄱㄴㄷ"
           print(min(a), min(b), min(c))
           print(max(a), max(b), max(c))


           # result
           # 1 a ㄱ
           # 3 c e
           ```

        * **대소문자 변환 lower(), upper()**


           ``` python
           a = 'this Is AppLE'
           print(a.upper())
           print(a.lower())

           # result
           # THIS IS APPLE
           # this is apple
           ```

        * **문자열을 구분자에 따라 나누는 함수 split()**


           ``` python
           a = '안녕,나는,해달이야'
           print(a.split(sep=','))
           b = '안녕 나는 해달이야'
           print(b.split())

           # result
           # ["안녕", "나는", "해달이야"]
           # ["안녕", "나는", "해달이야"]
           ```

        * **여러 문자열 사이에 구분자를 넣어주는 join()**

           ``` python
           mylist = ['안녕', '나는', '해달']
           mystring = '_'.join(mylist)
           print(mystring)

           # result : 안녕_나는_해달
           ```
   - ### **튜플**
   
      대괄호[]를 쓰는 리스트와 다르게 소괄호()를 사용한다.  
      한 번 선언하면 값을 바꿀 수 없다.  
      ```python
      a = (1, 2, 3, 4)
      print(a)

      a[1] = 7 # 에러
      ```
   - ### **사전**  
   
      키와 값을 쌍으로 가지는 자료형
      ```python
      data = dict()
      data['사과'] = 'Apple'
      data['바나나'] = 'Banana'
      data['코코넛'] = 'Coconut'

      print(data)
      print(data['사과'])
      
      if '사과' in data:
         print("'사과'를 키로 가지는 데이터가 존재합니다.")
    
      # result :
      # {'사과':'Apple', '바나나': 'Banana', '코코넛' : 'Coconut'}
      # Apple
      ```
      
      * #### **사전 자료형 관련 함수**
      
         keys : 사전 자료형에서 key값만 가져온다
         values : 사전 자료형에서 value값만 가져온다
         
         ```python
         # 키 데이터만 답은 리스트
         key_list = data.keys()

         # 값 데이터만 담은 리스트
         value_list = data.values()
         print(key_list, value_list)

         for key in key_list:
             print(data[key])

         # result :
         # dict_keys(['사과', '바나나', '코코넛']) dict_values(['Apple', 'Banana', 'Coconut'])
         # Apple
         # Banana
         # Coconut
         ```
      
  - ### **집합**  
   
      집합자료형  
      중복을 허용하지 않으며 순서가 없다.  
      중괄호{}를 사용한다.
      
      ```python
      # set을 사용한 정의
      data = set({1, 1, 2, 3, 4, 4, 5})
      print(data)

      # 중괄호를 사용한 정의
      data = {1, 1, 2, 3, 4, 4, 5}
      print(data)
      
      # result :
      # {1, 2, 3, 4, 5}
      ```
      
      * #### **집합 자료형 연산**
      
         합집합, 교집합 차집합 연산이 있다.

         ```python
         a = set([1, 2, 3, 4, 5])
         b = set([3, 4, 5, 6, 7])

         print(a | b) # 합집합 : {1, 2, 3, 4, 5, 6, 7}
         print(a & b) # 교집합 : {3, 4, 5}
         print(a - b) # 차집합 : {1, 2, 6, 7}
         ```
      
      * #### **집합 자료형 함수**
      
         add(), update(), remove() 함수가 있다.
         ```python
         a = set([1, 2, 3, 4, 5])

         # 새 원소 1개 추가
         a.add(8)

         # 새 원소 여러개 추가
         a.update([10, 11])

         # 원소 삭제
         a.remove(1)
         ```
      

## 반복문
   - ### **for**  
   
      반복 횟수가 정해져있는 명령을 사용할 때 사용하는 반복문  

      ``` python
      # for문의 구조

        for i in 범위:
           반복할 명령어
      ```
   - ### **while**
   
      조건에 따라 반복 여부를 결정하는 반복문  

      ``` python
      # while문의 구조
        while 조건 :
          반복할 명령어

      # while 무한 루프
        it = 0
        while True:
            it += 1
            print(it, end= ' ')
            
      # result : 1 2 3 4 5 6 7 ....
      ```
      
   - ### **break**
   
      반복문을 탈출할 때 사용

      ``` python
      # while문의 구조
        while 조건 :
          반복할 명령어

      # while 무한 루프
        it = 0
        while True:
            it += 1
            if it == 2:
               break
            print(it, end =' ')
            
      # result : 1
      ```
      
   - ### **continue**
   
      continue에 걸리면 아래 내용은 전부 스킵하고 다음 루프로 넘어감  

      ``` python
      # while문의 구조
        while 조건 :
          반복할 명령어

      # while 무한 루프
        it = 0
        while True:
            it += 1
            
            if it == 2:
               continue
               
            print(it, end = ' ')
            
      # result : 1 3 4 5 6 7 ....
      ```
## 조건문
   - ### **if-elif-else**
   
      조건에 따라 분기가 갈라지는 조건문

      ``` python
      score = int(input("점수를 입력하세요 "))
      if score >= 70:
          result = "통과"
      elif score >= 60:
          result = "재시험"
      else:
          result = "과락"
      ```
      
   - ### **삼항 연산자**
   
      파이썬에서의 삼항 연산자

      ``` python
      [True] if [조건] else [False]
      ```
   
## 입출력  

   - ### **input**  
      사용자에게 입력받는 input()  
      ```python
      myinput = input("당신의 나이는 몇살입니까?")
      print(myinput)
      ```
   
   - ### **입력 속도가 빠른 입력함수**  
      sys.stdin.readline().rstrip()  
      속도가 빠른 입력함수로 데이터가 너무 많아 빠른 입력을 요할 때 사용  
      rstrip() : 입력 받은 문자열 마지막 엔터 삭제  

      ```python
      import sys
      data = sys.stdin.readline().rstrip()
      print(data)
      ```
   
   - ### **print**  
      
      ``` python
      name = "해달"
      print("안녕 나는 %s" % name) # 문자열 옛날 방식
      print("안녕 나는 " + name)
      print("안녕 나는", name)
      print("안녕 나는 {}".format(name)) #pyformat
      print(f"안녕 나는 {name}") #f-string

      # result :
      # 안녕 나는 해달
      # 안녕 나는 해달
      # 안녕 나는 해달
      # 안녕 나는 해달
      # 안녕 나는 해달
      ```
   
      * **sep**
      
         출력 데이터 간 연결 기호 지정  
         미표기시 ' '가 기본으로 지정된다.  
         ``` python
         print('a', 'b', 'c', 'd')
         print('a', 'b', 'c', 'd', sep='*')

         # result
         # a b c d
         # a*b*c*d
         ```
      * **end**
      
         출력 데이터 마지막 기호 지정  
         미표기시 \n이 기본으로 지정된다.  
         ``` python
         print("안녕 나는 해달") # end = "\n"
         print("만나서 반가워")
         print("안녕 나는 해달", end="!@#$%")
         print("만나서 반가워")

         # result
         # 안녕 나는 해달
         # 만나서 만가워
         # 안녕 나는 해달!@#$%만나서 반가워
         ```
   
   - ### **파일 출력**  
      write()  
      ``` python
      f = open('haedal.txt', 'w')
      f.write("Hello Haedal!\n")
      f.write("Good Morning!")

      print("쓰기 종료")

      f.close()

      # result : haedal.txt
      # Hello Haedal!
      # Good Morning!
      ```
   
   - ### **파일 읽기**
      read(), readlines(), readline()
      ```
      haedal.txt

      Hello Haedal!
      Good Morniung!
      ```
      ``` python
      # read() 함수 : 파일 끝까지 읽음
      f = open('haedal.txt', 'r')
      a = f.read()
      print(a)
      f.close()

      # result :
      # Hello Haedal!
      # Good Morning!

      # readlines() 함수 : 파일 끝까지 줄별로 읽어서 리스트 반환
      f = open('haedal.txt', 'r')
      b = f.readlines() # 한 줄 씩 읽어서 list에 넣는다.
      print(b)
      f.close()

      # result :
      # ['Hello Haedal!\n', 'Good Morning!']

      # readline() 함수 : 한 줄만 읽음
      f = open('haedal.txt', 'r')
      c = f.readline() # list에 넣는다.
      print(c)
      f.close()

      # result :
      # Hello Haedal!
      ```
   
## 함수  

   - ### **함수 정의**
      ```python
      def 함수명(매개변수):
         명령어1
         명령어2
         ...
         return 결과
      ```
   - ### **Docstring**  
   
      \`\`\`을 통해 함수의 공식 설명(docstring)을 작성할 수 있다.
      ```python
      def hello_docstring():
          '''
          여기는 함수의 문서화 내용입니다.
          '''
          print("Hello DocString!")

      help(hello_docstring)

      # result:
      # hello_docstring()
      #       여기는 함수의 문서화 내용입니다.

      print(hello_docstring.__doc__)

      # result:
      #       여기는 함수의 문서화 내용입니다.

      hello_docstring()

      # result:
      # Hello DocString!
      ```
   
   - ### **return**  
      return이 발생하면 함수는 종료된다
      ```python
      def return_example(a, b):
       if a>b :
           print("해달이")
           return
       else:
           print("부기")
       print("아리")

      return_example(10, 20)
      # result :
      # 부기
      # 아리

      return_example(30, 20)
      # result
      # 해달이
      ```
   
  - ### **매개변수와 인수**  
   
      매개변수 : 함수 내부로 전달 시 사용되는 변수
      인수 : 함수 호출 시 함수로 전달해주는 값
      ```python
      def add_two_num(a, b): # 매개변수
       print("덧셈 중")
       result = a+b
       return result

      a = 10
      b = 13

      value = add_two_num(a, b) # 인수
      print(value)
      ```
   
  - ### **인수 순서 변경**  
   
      매개변수를 지칭하면 순서에 상관없이 넣을 수 있다.
      ```python
      def add_two_num(a, b):
       print("덧셈 중")
       print(a, b)
       result = a+b
       return result

      value = add_two_num(b = 10, a = 13)
      ```
   
   - ### **매개변수 기본값 지정**  
   
      가장 뒤의 변수부터 기본값을 지정할 수 있다.  
      앞에 것 먼저 지정하는 것은 불가능  
      ```python
      def add_two_num(a=100, b=30):
       print("덧셈 중")
       result = a+b
       return result

      value1 = add_two_num(10, 13)
      value2 = add_two_num(10)
      value3 = add_two_num(b=10)
      value4 = add_two_num()

      print(value1, value2, value3, value4)

      # result 
      # 23
      # 40
      # 110
      # 130
      ```
   
   - ### **여러 값을 받는 함수**
   
      매개변수에 *args를 이용하여 여러 값을 받을 수 있다
      ``` python
      def people_num(*args):
       print("공부하는 학생 수는? : ", end='') # end='\n'를 ''로 번경
       result = len(args)
       return result

      value = people_num("해달이", "사스미", "시라용", "부기", "메기")
      print(value, '명')

      # 공부하는 학생 수는? : 5명
      ```
   
   - ### **람다 표현식**  
   
      특정 기능을 수행하는 함수를 한 줄로 작성 
      ```python
      def add(a, b):
          return a+b

      # 일반적인 add 메서드 사용
      print(add(3, 7))

      # 람다 표현식 사용
      print((lambda a, b: a+b)(3, 7))
      ```
   
## 전역변수  
   - ### **전역 변수와 지역 변수**
      ```python
      def add_two_num(a, b):
          print("덧셈 중")
          result = a+b
          return result # 지역변수

      result = 0 # 전역변수
      add_two_num(10, 13)
      ```
   - ### **함수 내에서 전역 변수 호출**  
   
      global을 적어주어야 한다.  
      ```python
      def add_two_num(a, b):
          print("덧셈 중")
          global result = a+b # 전역 변수 호출
          return result

      result = 0 # 전역변수
      add_two_num(10, 13)
      ```
   
## 클래스

  객체의 설계도
   
   - ### **구성요소**  
   
      * 클래스 변수
      * 클래스 매소드
   
      ```python
      class FishBread:
       # 클래스 변수
       banjook = "밀가루"

       # 매소드 만들기
       # 붕어빵 굽기
       def make_FB(self, ingredient, price):
           self.ingredient = ingredient
           self.price = price

       # 붕어빵 살펴보기
       def see_FB(self):
           print(self.ingredient, self.price)

       # 클래스 메소드
       def see_banjook(cls): #cls를 매개변수로 받는다.
           print(cls.banjook)
      ```
   
   - ### **객체**  
   
      인스턴스라고도 부른다.

      ``` python
      # 객체 생성
      a = FishBread()
      b = FishBread()
      print(type(a))

      # 클래스 속성을 바꾸면 생성된 객체의 속성도 바뀐다.
      a.see_banjook()
      b.see_banjook()
      FishBread.banjook = "콩가루"
      a.see_banjook()
      b.see_banjook()

      # result
      # 밀가루
      # 밀가루
      # 콩가루
      # 콩가루

      a.make_FB("팥", 400)
      b.make_FB("슈크림", 500)

      a.see_FB()
      b.see_FB()
      ```
   
   - ### **Underbar Variable**
   
      함부로 수정할 수 없는 변수  
      변수 앞에 언더바를 2개 넣어준다.

      ```python
      class FishBread:
       banjook = "밀가루"

       def make_FB(self, ingredient, price):
           self.__ingredient = ingredient # 변수들 앞에 언더바를 2개 넣어준다
           self.__price = price

       def see_FB(self):
           print(self.__ingredient, self.__price)

       def see_banjook(cls):
           print(cls.banjook)

      a = FishBread()
      a.make_FB("팥", 400)
      print(a.__ingredient, a.__price) #__ingredient라는 변수가 없다며 에러 발생 -> 접근 권한 X
      a.__price = 10
      a.see_FB()
      ```
   
   - ### **Magic Method**
   
      함부로 수정할 수 없는 변수 연산 방법

      ```python
      class FishBread:
       def __init__(self, ingredient, price): # 초기화 시
           self.__ingredient = ingredient # 변수들 앞에 언더바를 2개 넣어준다
           self.__price = price

       def __str__(self): # 문자열 호출 시
           return '{} 붕어빵, 가격 {}원'.format(self.__ingredient, self.__price)

       def __add__(self, other): # +연산자에 덮어쓰기
           return self.__price + other.__price

      a = FishBread("팥", 400) # __init__ : 초기화
      b = FishBread("슈크림", 500) # __init__

      print(a) # __str__ : print에서 문자열 호출
      print(b) # __str__

      print('붕어빵 a,b 합쳐 %d원' % (a+b)) # __add__ : + 
      ```
   
## 상속  
   부모 클래스의 변수, 메소드를 자식 클래스가 물려받는 것
   ```python
   class Student: # 부모 클래스
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "안녕하세요 저는 {}이고 학생입니다.".format(self.name)

   class EStudent(Student): # Student 상속
       def __str__(self): #Override
           return "안녕하세요 저는 {}이고 초등학생입니다.".format(self.name)

       def print_age(self):
           print('{}의 나이는 {}살입니다.'.format(self.name, self.age))

   class MStudent(Student): # Student 상속
       def __str__(self):
           return "안녕하세요 저는 {}이고 중학생입니다.".format(self.name)

   sasumi = Student('사스미', 4)
   haedal = EStudent('해달이', 1)
   boogie = MStudent('부기', 5)

   print(sasumi)
   print(haedal)
   print(boogie)

   haedal.print_age() : 자식 객체는 부모 클래스의 함수를 물려받음.
   # sasumi.print_age() : 부모 객체는 자식의 함수에 접근 불가
   
   # result :
   # 안녕하세요 저는 사스미이고 학생입니다.
   # 안녕하세요 저는 해달이이고 초등학생입니다.
   # 안녕하세요 저는 부기이고 중학생입니다.
   # 해달이의 나이는 1살입니다.
   ```
## 모듈  

   함수나 변수 클래스를 모아놓은 파일로 사용하고 싶은 함수나 변수를 불러와서 쉽게 사용할 수 있도록 만들어준다.
   ```python
   module.py
   
   class Friends:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):
        print(f'안녕 난 {self.name}야. 나이는 {self.age}살이야.')

   def add_to_N(n):
       result = 0
       for i in range(n):
           result += i
       return result

   if __name__ == '__main__': # 이 줄이 없다면 import시 module 실행되어 밑에 글 나옴
       print('여기는 모듈1')
       # module이 실행 시만 실행
   ```
   - ### **모듈 불러오기**   
   
      from ~ import ~ 로 모듈에서 원하는 함수만 들고올 수 있음 / module.불러온 함수처럼 앞에 module을 작성할 필요 없음  
      as를 통해 별칭 지정 가능  
      \_\_name\_\_ = \'\_\_main\_\_\'부분이 없으면 import 하는 순간 실행되나 이 부분이 있다면 모듈을 불러온 후 모듈 실행시만 
      ```python
      # import module

      from module import Friends # module에서 원하는 함수만 들고옴 / module.Friends로 쓸 필요 없음
      from module import add_to_N as aN # 별칭 갸능

      boogie = Friends('Boogie', 5)
      boogie.hello()

      print(aN(10))
      ```

## 패키지 
   - ### **구성요소**
   
      * __init__.py : 이 폴더가 패키지 디렉토리임을 알려주는 파일
      * LecPython.npy
         ```python
         def intro():
            print("파이썬 강의 모듈입니다.")
         ```
      
   - ### **패키지 불러오기**
   
      ```python
      from package.LecPython import intro
      import sys

      intro()
      print(sys.path)
      ```
      
## 예외 처리
   - ### **try-except**
      
      예외처리는 try-except문으로 처리한다.
      try문 내에 에러가 발생할 만한 코드를 넣고 에러가 발생 시 except 구문을 처리한다.
      
      ```python
      print("program start")

      try:
          arr = ['b', 'l', 'o', 'g']
          print(arr[8]) #error
          print('==mid')
      except:
          print("==error! but still alive")

      print("program end")
      
      # result :
      program start
      ==error! but still alive
      program end
      ```
   - ### **finally**
   
      finally문은 에러 발생 여부와 상관없이 무조건 실행된다.
      
      ```python
      print("program start")

      try:
          arr = ['b', 'l', 'o', 'g']
          print(arr[8]) #error
          print('==mid')
      finally:
          print("finally") # 무조건 출력

      print("program end")
      
      # result:
      program start
      finally
      Traceback (most recent call last):
        File "d:\GitHub\2021S_Python\Python_Basic\18_Exception_Handing.py", line 18, in <module>
          print(arr[8]) #error
      IndexError: list index out of range
      ```
   - ### **else**
      
      else는 try내의 코드가 정상 동작 시 다음 동작을 나타낸다.
      **try에서의 else문은 except문 없이 작성할 수 없다.
      
      정상 동작 시 : try -> else -> finally
      ```python
      print("program start")

      try:
          arr = ['b', 'l', 'o', 'g']
          print(arr[0]) #not error
          print('==mid')
      except:
          print("error!") # 오류 처리시 error -> finally
      else:
          print("else") # 정상 처리시 else -> finally
      finally:
          print("finally") # 무조건 출력

      print("program end")
      
      # result :
      program start
      b
      ==mid
      else
      finally
      program end
      ```
      
      에러 시 : try -> except -> finally
       ```python
      print("program start")

      try:
          arr = ['b', 'l', 'o', 'g']
          print(arr[8]) #error
          print('==mid')
      except:
          print("error!") # 오류 처리시 error -> finally
      else:
          print("else") # 정상 처리시 else -> finally
      finally:
          print("finally") # 무조건 출력

      print("program end")
      
      # result :
      program start
      error!
      finally
      program end
      ```
      
   - ### **특정 에러 처리**
   
      특정한 에러를 처리하기 위해서는 except 에러이름으로 except문을 작성한다.
      
      ```python
      print("program start")

      try:
          arr = ['b', 'l', 'o', 'g']
          print(arr[8]) #error
          print('==mid')
      except IndexError:
          print("Index error!")
      except:
          print("another error!")
      else:
          print("else") # except 없이는 작성 불가

      print("program end")
      
      # result
      program start
      Index error!
      program end
      ```
   
   - ### **raise**
   
      의도적으로 에러를 발생시킬 경우에는 raise문을 사용한다.
   
      ```python
      a = int(input("1~5까지 숫자 입력 : "))

      # 범위 밖이면 에러 발생
      if a < 1 or a > 5 :
          raise ValueError #에러 종류

      print(f"입력한 a는 {a}입니다.")
      
      # result :
      1~5까지 숫자 입력 : 8
      Traceback (most recent call last):
        File "d:\GitHub\2021S_Python\Python_Basic\18_Exception_Handing.py", line 78, in <module>
          raise ValueError #에러 종류
      ValueError
      ```
      
      - ### **에러 메세지**

         에러 메세지를 직접 작성하고자 할 경우 Exception 구문을 통해 작성한다.

         ```python
         a = int(input("1~5까지 숫자 입력 : "))

         if a < 1 or a > 5 :
             raise Exception("에러에러에러!!")

         print(f"입력한 a는 {a}입니다.")

         # result:
         1~5까지 숫자 입력 : 8
         Traceback (most recent call last):
           File "d:\GitHub\2021S_Python\Python_Basic\18_Exception_Handing.py", line 86, in <module>
             raise Exception("에러에러에러!!")
         Exception: 에러에러에러!!
         ```
      
  - ### **주요 에러**
       * ValueError : 잘못된 값이 들어왔을 때
       * IndexError : 범위 초과
       * SyntaxError : 파이썬 문법에 맞지 않을 때
       * NameError : 변수 이름을 찾을 수 없을 때
       * ZeroDivisionError : 0으로 나눌 때
