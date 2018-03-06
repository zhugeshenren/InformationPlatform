from ctypes import *

'''
    tea算法
'''
class Tea:

    '''
        加密
        DATA,和 KEY
    '''

    delta = 0x9e3779b9;

    def encode(self,data,key):
        pass;



    '''
        解密
    '''
    def decode(self,data,key):
        pass

    # 加密
    def _encryptTEA(self,v,k):
        y = c_uint32(v[0])
        z = c_uint32(v[1])
        k0,k1,k2,k3 = c_uint32(k[0]),c_uint32(k[1]),c_uint32(k[2]),c_uint32(k[3])
        sum = c_uint32(0)
        delta = self.delta;
        n = 8
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
        delta = self.delta;

        sum.value = delta << 3;
        n = 8;
        w = [0,0];

        while n >0:
            z.value -= ((y.value << 4) + k2.value) ^ (y.value + sum.value) ^ ((y.value >> 5) + k3.value);
            y.value -= ((z.value << 4) + k0.value) ^ (z.value + sum.value) ^ ((z.value >> 5) + k1.value);
            sum.value -= delta
            n -= 1;

        w[0] = y.value;
        w[1] = z.value;


        return w;


if __name__ == "__main__":
    tea = Tea();
    print(ord('a'))
    k = [112,113,114,115];
    v = [888,999];
    v = tea._encryptTEA(v,k);

    print(v);

    v = tea._decryptTEA(v,k);

    print(v)