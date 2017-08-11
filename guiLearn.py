# from appJar import gui
# app=gui('title')
# app.addLabel('title','This is title')
# app.addLabel('lb1','label2 hehe哈哈')
# app.setBg('blue')
# app.setFont(10)
# app.setLabelBg('lb1','yellow')
# app.setLabelFg('title','red')
# app.setLabelFont(20,font='YaHei')
# app.setGeometry(500,200)
# app.setResizable(True)
# # def press(name):
# #     print(name,'is pressed')
# count=0
# def press(self):
#     global count
#     count=count+1
#     app.setLabel('lb1','pressed time:'+str(count))
#     if count==5:
#         app.stop()
# app.addButton('Button1',press)
# app.go()

# from appJar import gui
# app=gui('login')
# app.setBg('green')
# app.setFont(16)
# app.addLabel('lb1','Login Window')
# app.setLabelFg('lb1','white')
# app.addLabelEntry('用户名')
# app.setLabelFg('用户名','white')
# app.addSecretLabelEntry('密码')
# app.setLabelFg('密码','white')
# def press(name):
#     print(name,'is pressed')
#     if name=='提交':
#         username=app.getEntry('用户名')
#         password=app.getEntry('密码')
#         print(username,password)
#         if username=='admin' and password=='admin':
#             app.infoBox('Warning','Are you admin?')
#     if name=='重置':
#         app.clearEntry('用户名')
#         app.clearEntry('密码')
#         app.setFocus('用户名')
#     if name=='取消':
#         app.stop()
# app.addButtons(['提交','重置','取消'],press)
# app.setFont(12,font='YaHei')
# app.addStatusbar('hh')
# app.go()

# from appJar import gui
# app=gui('Lights')
# app.disableWarnings()
# app.addImage('light','J:/labelAndTitle.png')
# def press(name):
#     print(name,'pressed')
#     if name=='Exit':
#         app.stop()
#     if name=='On':
#         app.setImage('light','J:/on.png')
#         app.disableButton('On')
#         app.enableButton('Off')
#     if name=='Off':
#         app.setImage('light','J:/Off.png')
#         app.disableButton('Off')
#         app.enableButton('On')
# app.addButtons(['On','Off'],press)
# app.addButton('Exit',press)
# app.go()

# from appJar import gui
# import random
# answers=['yes','no','do not know','haha']
# def shake(self):
#     # global answers
#     if len(app.getEntry('Question'))==0:
#         app.errorBox('error','You must ask some question')
#     else :
#         app.playSound('J:/tonghua.wav')
#         answer=random.choice(answers)
#         app.setLabel('Answer',answer)
# def clear(self):
#     app.clearEntry('Question')
#     app.clearLabel('Answer')
# app=gui('Magic 8 Ball')
# app.setResizable(False)
# app.setFont(18)
# app.addEntry('Question')
# app.addButtons(['Shake','Clear'],[shake,clear])
#
# app.addImage('8ball','J:/on.png')
# app.addEmptyLabel('Answer')
#
# app.setLabelBg('Answer','yellow')
# app.setFocus('Question')
# app.go()

from appJar import gui
def press(name):
    if name=='Result':
        try:
            a=int(app.getEntry('entry1'))
            b=int(app.getEntry('entry2'))
            message='The result is as follows:\n'
            message+= 'Addition:'+str(a+b)+'\n'
            message+= 'substraction:'+str(a-b)
            app.setLabel('emptyLabel',message)
        except ValueError:
            app.errorBox('Illegal','Check your input')
            app.clearAllEntries()
            app.clearLabel('emptyLabel')
    if name=='Reset':
        app.clearAllEntries()
        app.clearLabel('emptyLabel')
    if name=='Exit':
        app.stop()

app=gui('Calculator')
app.addLabel('label_1','I am a label1',0,0)
app.addEntry('entry1',0,1)
app.addLabel('label_2','I am label2',0,3)
app.addEntry('entry2',0,4)
app.setFocus('entry1')
app.addEmptyLabel('emptyLabel',1,0,5)
app.setLabelRelief('emptyLabel',app.GROOVE)
app.setLabelAlign('emptyLabel',app.NW)
app.setLabelHeight('emptyLabel',8)
app.addButtons(['Result','Reset','Exit'],press,2,0,5)
app.go()