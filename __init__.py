print('----------------------------------')
print('-계산기                           -')
print('-1 더하기                         -')
print('-2 빼기                           -')
print('-3 곱하기                         -')
print('-4 나누기                         -')
print('----------------------------------')

n = int(input())

if n == 1:
    print('첫번째 숫자를 입력 해 주세요')
    a = int(input())
    print('두번째 숫자를 입력 해 주세요')
    b = int(input())
    print('두수의 합은 %s 입니다' %(a+b))
elif n == 2:
    print('첫번째 숫자를 입력 해 주세요')
    a = int(input())
    print('두번째 숫자를 입력 해 주세요')
    b = int(input())
    print('두수의 차는 %s 입니다' %(a-b))
elif n == 3:
    print('첫번째 숫자를 입력 해 주세요')
    a = int(input())
    print('두번째 숫자를 입력 해 주세요')
    b = int(input())
    print('두수의 곱은 %s 입니다' %a*b)
elif n == 4:
    print('첫번째 숫자를 입력 해 주세요')
    a = int(input())
    print('두번째 숫자를 입력 해 주세요')
    b = int(input())
    print('첫번째수 나누기 두번째수는 %s 입니다'%(a/b))
else :
    print('다시 입력 해 주세요')