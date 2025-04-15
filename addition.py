def add(a, b):
    return a + b


try:
    x = input('请输入第一个数：').strip()
    y = input('请输入第二个数：').strip()

    if not x or not y:
        print('错误：输入不能为空')
    else:
        x = float(x)
        y = float(y)
        if not (float('-inf') < x < float('inf')) or not (float('-inf') < y < float('inf')):
            print('错误：输入数值超出范围')
        else:
            print('结果是：', add(x, y))
except ValueError:
    print('错误：请输入有效的数字')
