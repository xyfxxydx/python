import turtle
import time

#词典:
abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#-1创建空列表“步骤”和“点集”----------------------------------------------

step = []
p = []

#-1终--------------------------------------------------------------
while 1 > 0 :
    print("\n若作图完成请输入“作图完成”")
    time.sleep(0.5)
    a = input("\n请输入作图语句：")

    #0分割作图语句并将每个字储存在列表中---------------------------

    l_a = []
    for x in range(len(a)) :
        l_a.append(a[x])
    #0终
    
    #1判断“取”型语句---------------------------------------------

    if "取" in l_a :
        
        #1-1判断取自由（任意）点语句-------------------------------

        if "任" in l_a :
            a = l_a.index("任")
            if l_a[a+1] == "意" or l_a[a+1] == "取":
            
                #1-1-1寻找自由点数量-------------------------------

                for x in l_a :
                    i = 0
                    for i in range(10) :
                        if str(i) == x :
                            num = i
                            break

                #1-1-1终-------------------------------------------

                #1-1-2寻找所作点的字母-----------------------------
                a = l_a.index("点")
                for x in range(a+1,len(l_a)):
                    if l_a[x] != '，':
                        p.append(l_a[x])
                #1-1-2终-------------------------------------------

                #1-1-3将取任意点步骤输入“步骤”-------------------

                step.append("在平面内取任意"+str(num)+"点")
                print("\n此作图语句为在平面内取任意"+str(num)+"点：")
                time.sleep(0.5)
                print(p)
                time.sleep(1)
                print("\n已录入")

                #1-1-3终-------------------------------------------

        #1-1终-----------------------------------------------------

        #1-2判断去中点语句-----------------------------------------

        if "中" in l_a:
            a = l_a.index("中")
            if l_a[a+1] == "点":
                for x in l_a:
                    a = l_a.index(x)
                    for i in abc:
                        if i == x:
                            for j in abc:
                                if l_a[a+1] == j:
                                    p.append(l_a[-1])
                                    step.append("取"+i+l_a[a+1]+"中点"+l_a[-1])
                                    time.sleep(0.5)
                                    print("\n此作图语句为取"+i+l_a[a+1]+"中点"+l_a[-1])
                                    time.sleep(1)
                                    print("\n点集为：")
                                    time.sleep(0.5)
                                    print(p)
                                    a = 1
                                    break
                    if a == 1:
                        break
    #1终-----------------------------------------------------------
    
    #2判断“作”型语句---------------------------------------------
    if l_a == "作":
        pass
    #2终-----------------------------------------------------------
    
    #判断作图完毕--------------------------------------------------

    if a == "作图完毕" :
        break
    print("\n目前有的作图语句为：")
    time.sleep(0.5)
    print(step)
    time.sleep(1)
    print("\n目前有的点有：")
    time.sleep(0.5)
    print(p)
    #全剧终------------------------------------------------------------
