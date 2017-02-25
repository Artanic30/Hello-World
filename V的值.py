import os
import sys

# 判断是否为数字
def isNum(value):
    try:
        x = int(value)
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

ΔT = input('请输入时间差（min）：')  # 时间差
R = input('R的值：')#
α = input('请输入半轴长α：')#
e = input('偏心率e：')#
if (isNum(ΔT) and isNum(R) and isNum(α) and isNum(e)):
    ΔT = int(ΔT)
    R = int(R)
    α = int(α)
    e = int(e)
else:
    answer = input("输入值有误，是否重新输入 ? ")
    if answer.strip() in "是 是的 好 好的 yes Yes".split():
        restart_program()
    else:
        print('再见')
        os._exit(0)
    C = 3 * 10 ** 8  # 光速
    G = 6.67408 * 10 ** -11  # 万有引力常量
    M = 5.965 * 10 ** 24  # 地球质量
    r = C / 2 * ΔT + R
    V = (G * M * (2 / r - 1 / α)) ** 0.5
    print('V的值为', V)

