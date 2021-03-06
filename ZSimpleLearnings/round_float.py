# round()如果只有一个数作为参数，不指定位数的时候，返回的是一个整数，而且是最靠近的整数（这点上类似四舍五入）。
# 但是当出现.5的时候，两边的距离都一样，round()取靠近的偶数，这就是为什么round(2.5) = 2。
# 当指定取舍的小数点位数的时候，一般情况也是使用四舍五入的规则，
# 但是碰到.5的这样情况，如果要取舍的位数前的小树是奇数，则直接舍弃，如果偶数这向上取舍。看下面的示例：

print(round(2.635, 2))
# >>> 2.63
print(round(2.645, 2))
# >>> 2.65
print(round(2.655, 2))
# >>> 2.65
print(round(2.665, 2))
# >>> 2.67
print(round(2.675, 2))
# >>> 2.67


# 使用格式化
# 效果和round（）是一样的。

print("%.2f" % 2.635)
# >>> '2.63'
print("%.2f" % 2.645)
# >>> '2.65'
print(int(2.5))
# >>> 2
