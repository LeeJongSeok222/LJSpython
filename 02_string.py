# 문자열은 " 나 " 모두 사용가능
from tkinter.font import names

name='Lee Jong-Seok'
content = "my content"

# 여러줄의 문자열을 변수에 담을때
multi = '''this is multi line string
this is second line'''

print('name:'+name)
print('content:'+content)
print('multi:'+multi)

# 문자열에 다른 타입의 데이터를 함께 출력할 경우...
age = 33

print('내이름은{0}이고, 나이는{1} 입니다.'.format(name,age))
print('내이름은'+name+'이고, 나이는'+str(age)+' 입니다.')
print(f'내이름은{name}이고, 나이는{age} 입니다.')

# 여러줄 일경우 한줄처리 or 한줄을 여러줄처럼 줄바꿈 하는거...
print('이것은 한줄이지만\n 여러줄 처럼 보이게 할겁니다.')
print('이것은 두줄이지만\
 한줄처럼 보이게 할겁니다.')