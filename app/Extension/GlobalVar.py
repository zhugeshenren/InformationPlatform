import threading
import time
import functools



## 通过装饰器进行装饰，达到对并发的支持
def LockWapper(fn):
    @functools.wraps(fn)
    def Wapper(self, *args, **kwargs):
        future = getattr(self, 'mutex')
        if self.mutex.acquire():
            var = fn(self,*args, **kwargs);
            self.mutex.release();
        return var;
    return Wapper;


class GlobalDict(dict):
    # 创建一个全局的字典
    _instance = None;

    # 定义一个互斥变量
    mutex = threading.Lock()

    def __init__(self,time):
        self.time = time;
        t = threading.Thread(target=self.ClearInvalidTime)
        t.start()


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = dict.__new__(cls,*args,**kwargs)
        return cls._instance

    # 插入键值对
    @LockWapper
    def Insert(self,key,value):
        self[key] = value;

    # 删除键值对
    @LockWapper
    def Delete(self,key,default):
        return self.pop(key,default)

    # 清空字典
    @LockWapper
    def Clear(self):
       return super(GlobalDict, self).clear(self);

    # 返回查找数据,查询不到返回None
    @LockWapper
    def Find(self,key):
        return self.get(key,None)

    def ClearInvalidTime(self):
        while True:
            time.sleep(self.time)

            print(time.localtime())

# 定义一个全局的值
class GlobalValue():
    time = None;
    elem = dict();

    # 定义一个互斥变量
    mutex = threading.Lock()

    count = 0;

    def Delete(self):
        #抢占锁
        if self.mutex.acquire():

            # 释放锁
            self.mutex.release();


# 维护一个全局的字典
#globalDict = GlobalDict(10)