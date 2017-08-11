""" Book  module definition"""
class Book(object):
    __id=0
    __isbn=''
    __name=''
    __stock=0
    __descr=''
    __rate=0.0
    def __init__(self,id,isbn,name,stock,descr,rate):
        self.__id=id
        self.__isbn=isbn
        self.__name=name
        self.__stock=stock
        self.__descr=descr
        self.__rate=rate
    def __str__(self):
        return 'Book: id='+str(self.__id)+',isbn='+self.__isbn+',name='+self.__name+',stock='+str(self.__stock)+',descr:'+self.__descr+',rate:'+str(self.__rate)

""" Reader module definition """
class Reader(object):
    __id=0
    __name=''
    __regId=''
    __sex=-1
    __age=0
    def __init__(self,id,name,regId,sex,age):
        self.__id=id
        self.__name=name
        self.__regId=regId
        self.__sex=sex
        self.__age=age
    def __str__(self):
        return 'Reader: id=%d, name=%s, regId=%s,sex=%d,age=%d' % (self.__id,self.__name,self.__regId,self.__sex,self.__age)

""" ReaderBook module definition """
class ReaderBook(object):
    __id=0
    __readerId=0
    __bookId=0
    __borrowTime=''
    __returnTime = ''
    def __init__(self,id,readerId,bookId,borrowTime,returnTime):
        self.__id=id
        self.__readerId=readerId
        self.__bookId=bookId
        self.__borrowTime=borrowTime
        self.__returnTime=returnTime
    def __str__(self):
        return 'ReaderBook: id=%d, readerId=%d, bookId=%d, borrowTime=%s, returnTime=%s' % (self.__id,self.__readerId,self.__bookId,self.__borrowTime,self.__returnTime)

# 测试区
if __name__=='__main__':
    book=Book(1,'11-xx-22','求生之路',10,'自己在网上查',6.9)
    print(book)
    reader=Reader(1,'杨子荣','231390129301xxxx',1,38)
    print(reader)
    readerBook=ReaderBook(1,1,1,'2000-1-1','2011-1-1')
    print(readerBook)
