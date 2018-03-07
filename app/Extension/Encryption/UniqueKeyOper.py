from app.Extension.Encryption.TeaAlgo import tea


"""
    关键的key
"""
class UniqueKey:

    _key = [123,456,789,150];

    '''
        
    '''
    def encode(self,args):
        ch = "";

        tmpList = list(args);
        tea.encode(tmpList,self._key)
        for t in tmpList:
            ch += str(t)+"-"


        return ch;


    def decode(self,code):
        pass

# 单例
uniqueKey = UniqueKey();