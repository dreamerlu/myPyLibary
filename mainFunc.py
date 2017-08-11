# import datetime
# test=datetime.datetime(2011,12,1,13,57,1)
# print(test)
#2011-12-01 13:57:01
import time
test=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(test,type(test))