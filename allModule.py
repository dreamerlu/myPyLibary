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
        return 'Book: id='+str(self.__id)+',isbn='+self.__isbn+',name='+self.__name+',stock='+self.__stock+',descr:'+self.__descr+',rate:'+self.__rate

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
