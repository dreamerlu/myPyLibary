from appJar import gui
from allDao import *
# 函数区
def addBookButtonProcess(btn):
    bookAttr=list()
    if btn == '提交':
        for entryName in ['isbnEntry','nameEntry','stockEntry','rateEntry']:
            if app.getEntry(entryName) == '':
                app.errorBox('空输入','请输入有效字符')
            if entryName == 'stockEntry':
                try:
                    bookAttr.append(int(app.getEntry(entryName)))
                except:
                    bookAttr.append(0)
                    app.errorBox('非法输入','请输入有效的整数')
            elif entryName == 'rateEntry':
                try:
                    bookAttr.append(float(app.getEntry(entryName)))
                except:
                    bookAttr.append(0)
                    app.errorBox('非法输入', '请输入有效的整数或者浮点数')
            else:
                bookAttr.append(app.getEntry(entryName))
        bookAttr.append(app.getTextArea('st'))
        BookDao.add(bookAttr[0],bookAttr[1],bookAttr[2],bookAttr[3],bookAttr[4])
        app.infoBox('操作成功','添加操作成功！')
        app.hideSubWindow('addWin')
        print(bookAttr)
    if btn == '重置':
        app.clearAllEntries()

def deleteBookButtonProcess(btn):
    pass

def showLabelEntry(item):
    if item == '添加':
        app.showSubWindow('addWin')
app=gui('图书管理系统','500x300')
app.setFont(12,font='YaHei')
app.createMenu('开始')
app.addMenuItem('开始','添加',showLabelEntry,shortcut='A',underline=1)
app.addMenuItem('开始','删除',shortcut='D',underline=1)
app.addMenuItem('开始','更新',shortcut='U',underline=1)
app.addMenuItem('开始','查询',shortcut='S',underline=1)

# 初始化 添加窗口subWindow
app.startSubWindow('addWin','添加窗口',True)
app.setGeometry(500,300)
app.setStretch("column")
app.setSticky('nw')
app.setPadding(5, 5)
# app.setInPadding(5,5)
app.addLabel('isbnLabel', 'isbn号', 1, 0)
app.setLabelWidth('isbnLabel', 5)
app.addEntry('isbnEntry', 1, 1)
app.setEntryWidth('isbnEntry', 40)
app.addLabel('nameLabel', '书名', 2, 0)
app.setLabelWidth('nameLabel', 5)
app.addEntry('nameEntry', 2, 1)
app.setEntryWidth('nameEntry', 40)
app.addLabel('stockLabel', '库存', 3, 0)
app.setLabelWidth('stockLabel', 5)
app.addEntry('stockEntry', 3, 1)
app.setEntryWidth('stockEntry', 40)
app.addLabel('rateLabel', '评分', 4, 0)
app.setLabelWidth('rateLabel', 5)
app.addEntry('rateEntry', 4, 1)
app.setEntryWidth('rateEntry', 40)
app.addLabel('descrLabel', '书籍描述', 5, 0)
app.addScrolledTextArea('st', 6, 0, 10)
app.setTextAreaWidth('st', 60)
app.setTextAreaHeight('st',5)
# app.setInPadding(10,10)
# app.setStretch('row')
# app.setPadding(20,2)
app.addButton('提交',addBookButtonProcess,7,0)
app.addButton('重置',addBookButtonProcess,7,2)
# app.addButtons(['提交','重置'],buttonProcess)
app.stopSubWindow()

#初始化 删除窗口
app.startSubWindow('deleteWin','删除窗口',True)
app.setGeometry(500,300)
app.setStretch("column")
app.setSticky('nw')
app.setPadding(5, 5)
# app.setInPadding(5,5)
app.addLabel('isbnLabel_delete', 'isbn号', 1, 0)
app.setLabelWidth('isbnLabel_delete', 5)
app.addEntry('isbnEntry_delete', 1, 1)
app.setEntryWidth('isbnEntry_delete', 40)
app.addButton('提交',deleteBookButtonProcess,2,0)
app.addButton('重置',deleteBookButtonProcess,2,1)
app.stopSubWindow()
app.go()