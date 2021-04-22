import math
import time
#引入所需模块



answer=input("请选择方程类型（输入：“a b”形式。其中“a”为“元”的数量；“b”为“次”数）：\n")
answer_list=answer.split(" ")
#询问方程类型



if int(answer_list[0])==1 and int(answer_list[1])==2:
    model='1 2'
elif int(answer_list[0])==2 and int(answer_list[1])==1:
    model='2 1'
#判断方程类型



if model=='1 2':
    print("请将元一元二次方程化成“ax^2+bx+c=0”的形式\n")
    time.sleep(1)

    a=int(input("请分别输入a，b，c的值：\na："))
    time.sleep(0.1)

    b=int(input("\nb："))
    time.sleep(0.1)

    c=int(input("\nc："))
    time.sleep(0.1)
    #询问并获得a，b，c的值

    delta=b**2-4*a*c
    #“delta”为Δ（delta）

    if delta<0:
        print("\n此方程无解")
        time.sleep(1)
        #无解情况

    elif delta>0:
        son=math.sqrt(delta)
        #定义分子

        x=int((son+b)/(2*a))
        print("\n此方程的第一个解x1为："+str(x))
        time.sleep(1)
        #计算并打印出x1

        x=int((son-b)/(2*a))
        print("\n此方程的第二个解x2为："+str(x))
        time.sleep(1)
        #计算并打印出x2
        #有两解情况

    elif delta==0:
        son=math.sqrt(delta)
        #定义分子

        x=int((son+b)/(2*a))
        print("\n此方程仅有一解x为："+str(x))
        time.sleep(2)
        #计算并打出x
        #仅有一解情况



if model=='2 1':
    print("请将二元一次方程化为 ax+by=c，dx+ey=f 的形式")
    time.sleep(1)

    a=int(input("请分别输入a，b，c，d，e，f的值：\na="))
    time.sleep(0.1)

    b=int(input("\nb="))
    time.sleep(0.1)
    
    c=int(input("\nc="))
    time.sleep(0.1)
    
    d=int(input("\nd="))
    time.sleep(0.1)
    
    e=int(input("\ne="))
    time.sleep(0.1)
    
    f=int(input("\nf="))
    time.sleep(0.1)
    #询问并获得a，b，c，d，e，f的值

    Δ=a*e-b*d
    Δx=c*e-b*f
    Δy=a*f-c*d
    x=Δx/Δ
    y=Δy/Δ
    #计算x，y的值

    print("\nx的值为："+str(x))
    print("\ny的值为："+str(y))
    #显示x，y的值

print("\n欢迎下次使用本工具")
#退出程序
