# this is to convert a binary number to decimal number

import re

while True:
    target = input("please input a binary number:")
    if not re.match("^[0-1]*$", target):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        break
ans = 0
numlevel = len(target)
for index in range(0, numlevel):
    ans += int(target[numlevel - index - 1]) * 2**index
print(ans)
print(bin(ans))

# this is to convert a decimal number to binary
# 用2辗转相除至结果为1
# 将余数和最后的1从下向上倒序写 就是结果 （逆序）
# 例如302
# 302/2 = 151 余0
# 151/2 = 75 余1
# 75/2 = 37 余1
# 37/2 = 18 余1
# 18/2 = 9 余0
# 9/2 = 4 余1
# 4/2 = 2 余0
# 2/2 = 1 余0
# 故二进制为100101110

import re

while True:
    target = input("please input a decimal number:")
    if not re.match("^[0-9]*$", target):
        print("Error! Only digits 0 and 1 allowed!")
        continue
    else:
        break
int_target = int(target)
biList = []
while True:
    biList.append(int_target % 2)
    int_target = int_target // 2
    if int_target == 1:
        biList.append(int_target % 2)  # 要么就在创建list的时候把int变成str
        break
biList.reverse()
binumber = int(''.join(str(i) for i in biList))  # 要注意join必须是string,不能是int
print('The binary number of', target, "is", binumber)


# MIT example, a different way of writing

num = 19
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''  # 定义一个空字符也很关键!
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result  # 核心写法: 将result定义为string, 拆解字符为'10011' = '1001' + '1'
                                    # 1和0来自于余数,但是每一步都是被推后
    num = num // 2                  # 将num除以2取整后,再次循环,最终将'10011'拆解为'1'+'0'+'0'+'1'+'1'
if isNeg:
    result = '-' + result
print('\nConvert to binary number:', result)