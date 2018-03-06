from ctypes import *
import math

'''
    tea算法
'''
class Tea:

    '''
        加密
        DATA,和 KEY
    '''

    # 奇妙的数字
    _delta = 0x9e3779b9

    # 加密轮数
    _rounds = 16

    '''
        目前加密解密只适合于ascil编码，后期可以加装饰器，拦截data
        
        顺序加密
    '''
    def encode(self,data,key,encoding = "ascil"):

        if (encoding is not "ascil"):
            pass

        for t in  range(len(data)):
            data[t] = ord(data[t])

        for t in range(len(data)-1):
            data[t:t+2] = self._encryptTEA(data[t:t+2],key);



    '''
        逆序解密
    '''
    def decode(self,data,key,encoding = "ascil"):
        if(encoding is not "ascil"):
            pass

        for t in reversed(range(len(data)-1)):
            data[t:t+2] = self._decryptTEA(data[t:t+2],key);

        for t in range(len(data)):
            data[t] = chr(data[t])

    # 加密
    def _encryptTEA(self,v,k):
        y = c_uint32(v[0])
        z = c_uint32(v[1])
        k0,k1,k2,k3 = c_uint32(k[0]),c_uint32(k[1]),c_uint32(k[2]),c_uint32(k[3])
        sum = c_uint32(0)
        delta = self._delta;
        n = self._rounds
        w = [0, 0]

        while n > 0:
            sum.value += delta
            y.value += ((z.value << 4) + k0.value) ^ (z.value + sum.value) ^ ((z.value >> 5) + k1.value);

            z.value += ((y.value << 4) + k2.value) ^ (y.value + sum.value) ^ ((y.value >> 5) + k3.value);
            n -= 1

        w[0] = y.value
        w[1] = z.value
        return w;


    # 解密
    def _decryptTEA(self,v,k):
        y = c_uint32(v[0])
        z = c_uint32(v[1])
        k0, k1, k2, k3 = c_uint32(k[0]), c_uint32(k[1]), c_uint32(k[2]), c_uint32(k[3])
        sum = c_uint32(0)
        delta = self._delta;

        # 求解对数
        sum.value = delta << int(math.log(self._rounds,2));

        n = self._rounds

        w = [0,0];

        while n >0:
            z.value -= ((y.value << 4) + k2.value) ^ (y.value + sum.value) ^ ((y.value >> 5) + k3.value);
            y.value -= ((z.value << 4) + k0.value) ^ (z.value + sum.value) ^ ((z.value >> 5) + k1.value);
            sum.value -= delta
            n -= 1;

        w[0] = y.value;
        w[1] = z.value;
        return w;

'''
    测试用例
'''
if __name__ == "__main__":
    tea = Tea();
    print(ord('a'))
    print(chr(48))

    k = [112,113,114,115];

    v = list("2018-12-11-Dennis")
    tea.encode(v,k);

    print(v)
    tea.decode(v,k);


    print(''.join(v))
