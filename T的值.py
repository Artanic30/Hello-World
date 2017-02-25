import sys
import os

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
#求T的累加值
t = 0
while (t >= 0):
    x = input('t的值（输入0结束）:')#输入t的值
    if (isNum(x)):
        x = int(x)
    else:
        answer = input("输入值有误，是否重启程序 ? ")
        if answer.strip() in "是 是的 好 好的 yes Yes".split():
            restart_program()
    if (x == 0):#结束命令
        print('程序结束')
        break
    t = t + x
print(t)






