#这是一个计算BMI的程序，还可以判断您的BMI指数是否正常。
#感谢使用,本程序会询问您的性别。实际上BMI指数与性别无关，只是作为if嵌套和elif的练手之作。
#BMI=体重**2/身高
#BMI<=18.5为偏瘦
# 18.5<BMI<24<为正常
# 28<=BMI<=32为肥胖
# BMI>32为非常肥胖。
#made by:zqy
#time:2023.7.26 night
user_sex=input("您的性别")
user_weight=float(input('您的体重(kg)'))
user_height=float(input('您的身高(m)'))
BMI_result=user_weight/(user_height)**2
print("您的BMI值是"+str(BMI_result))
if user_sex=="男":
    if BMI_result<=18.5:
        print("您偏瘦，记得多吃点哦。")
    elif BMI_result<=18.5:
        print("您偏瘦，记得多吃点哦。")
    elif 18.5<BMI_result<24:
        print("一切正常，保持就好。")
    elif 28<=BMI_result<=32:
        print("哎呀，有点超重了，注意一下饮食和运动。")
    elif BMI_result>32:
        print("严重超重，请尽快减肥。")
else:
    if BMI_result <=18.5:
        print("您偏瘦，记得多吃点哦。")
    elif BMI_result <= 18.5:
        print("您偏瘦，记得多吃点哦。")
    elif 18.5 < BMI_result < 24:
        print("一切正常，保持就好。")
    elif 28 <=BMI_result<=32:
        print("哎呀，有点超重了，注意一下饮食和运动。")
    elif BMI_result > 32:
        print("严重超重，请尽快减肥。")
