#09String.py

text = input("Insert Message in English : ")
print(text.upper(), end="")
print(text.lower(), end="\tAAA")
print(text.capitalize())

for c in text:
    print(c)

# 대문자로 입력된 것은 소문자로, 소문자-> 대문자로 출력하기
# Hello World
# hELLO wORLD

print("-" * 80)
for c in text:
    if c.isupper():
        print(c.lower() , end="")
    else:
        print(c.upper(), end="")

print("-" * 80)
rText = str()
for c in text:
    if c.isupper():
        rText += c.lower()
    else:
        rText += c.upper()
print("rText = ", rText)