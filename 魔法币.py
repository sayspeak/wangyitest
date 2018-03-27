print("输入一个期望值")
a = int(input())
result = ''
while a:
    if a % 2:
        a = (a - 1) // 2
        result = '1' + result
    else:
        a = (a - 2) // 2
        result = '2' + result
print(result)