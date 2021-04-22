import turtle
import time



#
#
#开始尝试作图
#
#

while 1 > 0 :
    a = input("请输入作图语句：")

    #分割作图语句并将每个字储存在列表中
    l_a=[]
    for x in range(len(a)) :
        l_a.append(a[x])
    
    #判断取自由（任意）点语句
    if "任" in l_a :
        a = l_a.index("任")
        if l_a[a+1] == "意" :
            print("此作图语句为取任意点语句")
