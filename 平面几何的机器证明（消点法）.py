import turtle
import time



#
#
#开始尝试作图
#
#

#创建空列表“步骤”
step = []

while 1 > 0 :
    print("\n若作图完成请输入“作图完成”")
    a = input("\n请输入作图语句：")

    #分割作图语句并将每个字储存在列表中
    l_a=[]
    for x in range(len(a)) :
        l_a.append(a[x])
    
    #1判断“取”型语句
    if "取" in l_a :
        
        #1-1判断取自由（任意）点语句
        if "任" in l_a :
            a = l_a.index("任")
        
            if l_a[a+1] == "意" or l_a[a+1] == "取":
            
                #寻找自由点数量
                for x in l_a :
                    i = 0

                    for i in range(10) :
                        if str(i) == x :
                            num = i
                            break
                
                #将取任意点步骤输入“步骤”
                step.append("在平面内取任意"+str(num)+"点")
                print("\n此作图语句为在平面内取任意"+str(num)+"点")
        #1-1终
    #1终
    
    #2判断“作”型语句
    if l_a == "作":
        pass
    #2终
    
    #判断作图完毕
    if a == "作图完毕" :
        break
    #终
