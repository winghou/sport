# -*- encoding=utf8 -*-
__author__ = "x1c"

#同步代码



from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(force_restart=False)



def baoming(next,password):
    
    
    poco(text=next).click()


    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()

#     if exists(Template(r"tpl1528450290699.png", record_pos=(-0.003, -0.762), resolution=(720, 1280))):
#         poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
#         if exists(Template(r"tpl1528450335596.png", record_pos=(0.207, 0.236), resolution=(720, 1280))):
# 
#             touch(Template(r"tpl1528450335596.png", record_pos=(0.207, 0.236), resolution=(720, 1280)))


    poco("返回 按钮").click()

    
    if exists(Template(r"tpl1528105856130.png", record_pos=(0.375, 0.808), resolution=(720, 1280))):

        # poco(text="动态").click()
        touch(Template(r"tpl1528188846463.png", record_pos=(0.372, 0.803), resolution=(720, 1280)))

    poco("com.tencent.mobileqq:id/lebasv").swipe([-0.1882, -0.3258])
    
    sleep(1.0)
    sleep(1.0)
    sleep(1.0)
    sleep(1.0)
    
    touch(Template(r"tpl1528002726796.png", record_pos=(-0.26, 0.414), resolution=(720, 1280)))

    # poco(text="运动").click()

    sleep(1.0)
    sleep(1.0)
    sleep(1.0)
    sleep(1.0)

    touch(Template(r"tpl1526302079911.png", record_pos=(-0.137, -0.204), resolution=(1080, 1920)))
    sleep(1.0)
    sleep(1.0)


    
    if exists(Template(r"tpl1526557404409.png", threshold=0.75, target_pos=5, rgb=False, record_pos=(0.004, 0.369), resolution=(720, 1280))):
        touch(Template(r"tpl1526484272806.png", record_pos=(0.0, 0.369), resolution=(720, 1280)))
    else:
        swipe(Template(r"tpl1530023736209.png", record_pos=(0.414, -0.482), resolution=(720, 1280)), vector=[-0.0137, -0.0784])
        sleep(2)

        touch(Template(r"tpl1526557706092.png", record_pos=(0.356, 0.829), resolution=(720, 1280)))


    # poco("立即报名").click()
    sleep(3.0)


    


    touch(Template(r"tpl1526383833479.png", record_pos=(0.206, 0.601), resolution=(720, 1280)))
    
    sleep(3.0)
    
    touch(Template(r"tpl1526383895819.png", record_pos=(-0.003, 0.261), resolution=(720, 1280)))


    sleep(3.0)

    #输入密码
    passw(password)



    sleep(1.0)
    sleep(1.0)
    sleep(1.0)


    touch(Template(r"tpl1526485039773.png", record_pos=(-0.006, 0.547), resolution=(1080, 1920)))
    
    sleep(1.0)
    sleep(1.0)


    touch(Template(r"tpl1526556931448.png", record_pos=(-0.006, 0.203), resolution=(720, 1280)))
    




    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    
    touch(Template(r"tpl1530539147759.png", record_pos=(0.417, -0.754), resolution=(720, 1280)))
    sleep(2)
    touch(Template(r"tpl1530539159910.png", record_pos=(-0.004, 0.514), resolution=(720, 1280)))
    sleep(3)
    touch(Template(r"tpl1530539178739.png", record_pos=(0.015, -0.746), resolution=(720, 1280)))
    touch(Template(r"tpl1530539202183.png", record_pos=(0.007, -0.46), resolution=(720, 1280)))
    
    sleep(3.0)

    touch(Template(r"tpl1530539505946.png", record_pos=(-0.34, -0.619), resolution=(720, 1280)))
    if exists(Template(r"tpl1530944767422.png", record_pos=(0.01, 0.579), resolution=(720, 1280))):
        touch(Template(r"tpl1530717678279.png", record_pos=(0.0, 0.565), resolution=(720, 1280)))


     



    touch(Template(r"tpl1530717511032.png", record_pos=(-0.007, 0.821), resolution=(720, 1280)))

    sleep(2.0)

    touch(Template(r"tpl1530539253912.png", record_pos=(-0.003, 0.806), resolution=(720, 1280)))
    sleep(5.0)


    #输入密码
    passw(password)
    sleep(2.0)


    touch(Template(r"tpl1530539274184.png", record_pos=(0.007, 0.724), resolution=(720, 1280)))
    sleep(2.0)

    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    
    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    poco("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    poco("com.tencent.mobileqq:id/conversation_head").click()


    poco(text="设置").click()


    touch(Template(r"tpl1526302387499.png", record_pos=(-0.367, -0.598), resolution=(1080, 1920)))



def passw(on):
    if on:

        touch(Template(r"tpl1526484939674.png", record_pos=(-0.326, 0.386), resolution=(1080, 1920)))
        touch(Template(r"tpl1526484949147.png", record_pos=(-0.338, 0.671), resolution=(1080, 1920)))
        touch(Template(r"tpl1526484955271.png", record_pos=(-0.333, 0.396), resolution=(1080, 1920)))
        touch(Template(r"tpl1526484960209.png", record_pos=(-0.337, 0.531), resolution=(1080, 1920)))
        touch(Template(r"tpl1526484965998.png", record_pos=(0.002, 0.394), resolution=(1080, 1920)))
        touch(Template(r"tpl1526484971572.png", record_pos=(-0.335, 0.386), resolution=(1080, 1920)))
    
    else:


        touch(Template(r"tpl1526557855415.png", record_pos=(-0.335, 0.397), resolution=(720, 1280)))
        touch(Template(r"tpl1526557890075.png", record_pos=(0.333, 0.4), resolution=(720, 1280)))
        touch(Template(r"tpl1526557855415.png", record_pos=(-0.335, 0.397), resolution=(720, 1280)))
        touch(Template(r"tpl1526557905969.png", record_pos=(-0.336, 0.536), resolution=(720, 1280)))
        touch(Template(r"tpl1526557924934.png", record_pos=(0.004, 0.814), resolution=(720, 1280)))
        touch(Template(r"tpl1526557929389.png", record_pos=(0.0, 0.674), resolution=(720, 1280)))

    




# baoming('3295909585',1)#8
# baoming('1610852713',1)#9
# baoming('2730948428',1)#10
# baoming('3395252436',1)#11
# baoming('3162719941',1)#12
# baoming('1079014185',0)#20

# baoming('2908591091',1)#13
# baoming('3216766523',1)#14
# baoming('2121576590',0)#15
# baoming('2975054100',0)#16
# baoming('3047095118',0)#17
# baoming('3092927296',0)#18
# baoming('3214154578',0)#19


# baoming('872173548',1)#0
# baoming('2231036155',1)#2 
# baoming('3589576972',1)#3
# baoming('2207540889',1)#4
# baoming('3289574562',1)#5
# baoming('2730933296',1)#6  
# baoming('1658594531',1)#7
baoming('3317341495',1)#1














