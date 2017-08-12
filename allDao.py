""" 此文件负责写操纵所有类对应的数据库表的方法 """
import sqlite3
from allModule import *
import time
class DB(object):
    __dbPath='J:/library.db'
    __con=sqlite3.connect(__dbPath)
    @staticmethod
    def getCon():
        return DB.__con
    @staticmethod
    def relieveCon():
        DB.__con.close()
    @staticmethod
    def getCursor():
        return DB.__con.cursor()

class BookDao(object):
    @staticmethod
    def add(isbn='', name='', stock=0, descr='', rate=0):
        """ Add """
        con=DB.getCon()
        cursor=DB.getCursor()
        cursor.execute('insert into t_book (isbn,name,stock,descr,rate) VALUES (?,?,?,?,?)',(isbn,name,stock,descr,rate))
        con.commit()

    @staticmethod
    def delete(id):
        """ Delete """
        con = DB.getCon()
        cursor = DB.getCursor()
        cursor.execute('delete from t_book WHERE id=?',(id,))
        con.commit()

    @staticmethod
    def deleteByISBN(isbn):
        """ Delete """
        con = DB.getCon()
        cursor = DB.getCursor()
        cursor.execute('delete from t_book WHERE isbn=?', (isbn,))
        con.commit()

    @staticmethod
    def update(id,isbn='', name='', stock=0, descr='', rate=0):
        """ Update """
        def encapStr(str):
            return '\''+str+'\''
        con = DB.getCon()
        cursor = DB.getCursor()
        sql='set '
        sqlPart=dict()
        if len(isbn)>0:
            sqlPart['isbn']=encapStr(isbn)
        if len(name)>0:
            sqlPart['name']=encapStr(name)
        if stock!=0:
            sqlPart['stock']=stock
        if len(descr)>0:
            sqlPart['descr']=encapStr(descr)
        if rate>0:
            sqlPart['rate']=rate
        for key in sqlPart.keys():
            sql+=' '+str(key)+'='+str(sqlPart[key])+','
        sql=sql[0:-1]
        sql+=' where id='+str(id)
        sql='update t_book '+sql
        print(sql)
        cursor.execute(sql)
        con.commit()

    @staticmethod
    def selectById(id):
        con=DB.getCon()
        cursor=DB.getCursor()
        queryresult=cursor.execute('select * from t_book where id=?',(id,))
        for result in queryresult:
            id,isbn,name,stock,descr,rate=result[:]
            book=Book(id,isbn,name,stock,descr,rate)
            return book

    @staticmethod
    def selectByISBN(isbn):
        con = DB.getCon()
        cursor = DB.getCursor()
        queryresult = cursor.execute('select * from t_book where isbn=?', (isbn,))
        for result in queryresult:
            id, isbn, name, stock, descr, rate = result[:]
            book = Book(id, isbn, name, stock, descr, rate)
            return book

class ReaderDao(object):
    @staticmethod
    def add(name='',regId='',sex=-1,age=0):
        con=DB.getCon()
        cursor=DB.getCursor()
        cursor.execute('insert into t_reader (name,regId,sex,age) VALUES (?,?,?,?)',(name,regId,sex,age))
        con.commit()

    @staticmethod
    def delete(id):
        con = DB.getCon()
        cursor = DB.getCursor()
        cursor.execute('delete from t_reader WHERE id=?',(id,))
        con.commit()

    @staticmethod
    def update(id,name='',regId='',sex=-1,age=0):
        def encapStr(str):
            return '\''+str+'\''
        con = DB.getCon()
        cursor = DB.getCursor()
        sql='set '
        sqlPart=dict()
        if len(name)>0:
            sqlPart['isbn']=encapStr(name)
        if len(regId)>0:
            sqlPart['name']=encapStr(regId)
        if sex != -1:
            sqlPart['sex']=sex
        if age !=0:
            sqlPart['age']=age
        for key in sqlPart.keys():
            sql+=' '+str(key)+'='+str(sqlPart[key])+','
        sql=sql[0:-1]
        sql+=' where id='+str(id)
        sql='update t_reader '+sql
        cursor.execute(sql)
        con.commit()

    @staticmethod
    def selectById(id):
        cursor = DB.getCursor()
        queryresult = cursor.execute('select * from t_reader where id=?', (id,))
        for result in queryresult:
            id,name,regId,sex,age=result[:]
            reader=Reader(id,name,regId,sex,age)
            return reader

    @staticmethod
    def selectByRegId(regId):
        con = DB.getCon()
        cursor = DB.getCursor()
        queryresult = cursor.execute('select * from t_reader where regId=?', (regId,))
        for result in queryresult:
            id,name, regId, sex, age = result[:]
            reader = Reader(id, name, regId, sex, age)
            return reader

class ReaderBookDao(object):
    @staticmethod
    def add(readerId,bookId,borrowTime='',returnTime=''):
        con=DB.getCon()
        cursor=DB.getCursor()
        if borrowTime=='':
            borrowTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        cursor.execute('insert into t_reader_book (readerId,bookId,borrowTime,returnTime) VALUES (?,?,?,?)',(readerId,bookId,borrowTime,returnTime))
        con.commit()

    @staticmethod
    def deleteById(id):
        con = DB.getCon()
        cursor = DB.getCursor()
        cursor.execute('delete from t_reader_book WHERE id=?', (id,))
        con.commit()

    @staticmethod
    def deleteByRefId(readerId,bookId):
        con = DB.getCon()
        cursor = DB.getCursor()
        cursor.execute('delete from t_reader_book WHERE readerId=? AND bookId=?', (readerId,bookId))
        con.commit()
# Test
# db=DB()
# con=db.getCon()
# cursor=db.getCursor()
# result=cursor.execute('select * from t_book')
# for row in result:
#     print(row)
# BookDao.add('','居山而行',2,'《居山而行》是90后女冠雲姑的首部散文集，作者在书中写了'
#                      '自己出家前的生活，出家后的日常，出家后的修行生活等多个方面，内容涉及'
#                      '饮食、旅行、与世俗人的来往、修行、读书等，为读者提供了丰富的、与众不同的'
#                      '生活轨迹的感悟，对世俗、情感、孤独、文章、生死、幸福等，提出了非常独到而超 脱的见解，'
#                      '能给读者以心灵的慰藉及生活的指导，是一部情志高远的诚心之作。',8.9)
# BookDao.add()
# BookDao.delete(3)
# test='我爱你永远'
# BookDao.update(4,'','',1,test,0)
# book=BookDao.selectById(4)
# book=BookDao.selectByISBN('9787559404763')
# print(book)
# ReaderDao.add('James Bond','2001213123131234',1,39)
# ReaderDao.add()
# ReaderDao.delete(2)
# ReaderDao.update()
# print(ReaderDao.selectById(1))
# print(ReaderDao.selectByRegId('2001213123131234'))
# ReaderBookDao.add(1,1,'','2017-09-11 23:00:01')
# ReaderBookDao.deleteById(2)
ReaderBookDao.deleteByRefId(1,1)