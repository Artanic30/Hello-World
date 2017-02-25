import os
import sys

# 判断是否为数字
def isNum(value):
    try:
        pass
    except TypeError:
        return False
    except ValueError:
        return False
    else:
        return True

# 错误重启
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# 求S的值和S的累加值
S = 0
n = 0
while S >= 0:
    V = input('V的值（输入0结束）：')  # 输入V的值
    t = input('t的值（输入0结束）：')  # 输入t的值
    if isNum(V) and isNum(t):  # 确定输入值是否为数字
        t = int(t)
        V = int(V)
    else:
        answer = input("输入值有误，是否重启程序 ? ")
        if answer.strip() in "是 是的 好 好的 yes Yes".split():
            restart_program()
    s = V * t
    n += 1
    S += s
    if s == 0:
        print('程序结束')
        break
    print('S%d的值为：' % n, s)
print('S的值为：', S)





