# 逻辑行和物理行 logic line and physical line

i = 5
print(i)

# is the same as: (--- 分号表示逻辑行结束，此处两个物理行，两个逻辑行)

i = 5;
print(i);

# is the same as: （--- 此处用一个物理行写了两个逻辑行,分号表示逻辑结束，但是语句可以继续）

i = 5; print(i);

# 一般来说不建议一个物理行包括多个逻辑行，也就是说避免使用分号。
