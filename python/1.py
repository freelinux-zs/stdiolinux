import random
secret = random.randint(1,10) #生成一个1到10的随机数
print("________python____________")
temp = input("输入一个整数看看是否和随机数相同：")
guess = int(temp)

while guess != secret:
    if guess > secret:
         print("偏大")
    else:
         print("偏小")
    temp = input("您猜错了，请重新输入一个整数：")
    guess = int(temp)
print("恭喜你猜对了,游戏结束")
