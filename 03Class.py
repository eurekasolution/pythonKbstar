# 03Class.py

var1 = "I am Python"
var2 = "I am Python"

print( id(var1) )
print( id(var2) )
print(var1 == var2)
print(var1 is var2)

var2 = "Hello Python"
print( id(var1) )
print( id(var2) )
print(var1 == var2)
print(var1 is var2)

var2 = 12
print("type of var1 = ", type(var1))
print("type of var2 = ", type(var2))

var1 = var1.replace("Python", "파이썬")
print("var1 = ", var1)

# data type의 종류 : 숫자형, 논리형 , 문자열 ..
# 숫자형 타입에 사용하는 연산자 : +, -, *, /
#       5//2 (floor), **
# https://docs.python.org/3/library/

# 논리형 연산자.
# <, <=, >, >=, ==, !=, is, is not
# p -> q   : ~p or q  : ~q -> ~p :

# 문자열형 데이터 타입 (str)
# 다음과 같이 출력하시오.
# 파이썬의 문자열은 "큰따옴표"도 되고 '작은 따옴표'도 됩니다. \를 사용하라
test = "파이썬의 문자열은 \"큰따옴표\"도 되고 \'작은 따옴표\'도 됩니다. \\ backslash"
print(test)