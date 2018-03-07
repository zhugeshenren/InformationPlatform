from urllib.parse import unquote

'''
    功能 : 将 self.request.body 中的数据解析为python字典
    
    bug1 : ajax 数据 key 中出现 '['  ']' 一定会导致解析异常，但是value不会，事实上可以加密
    bug2 : 当前台传入的数据为:
        {key1:{key2:[val1,val2,val3]}}
        这样解析会出现异常，解析为
        {key1:{key2:{'' : [val1,val2,val3]} }}
        事实上为了保证解析的一致性，这个Bug目前无法解决，因为当key确实为''是，url编码与上述相同，所以尽量保证前台传入数据不包含list格式
'''

class DecodeHtmlBody():
    def DecodeBody(self,urltext):
        text = urltext.decode('utf-8');
        text = text.split('&');
        tmpdict = dict();

        for txt in text:
            # 分割出每一段
            key = '';
            value = ''
            tmp = '';
            for c in txt:
                if c is '=':
                    key = tmp;
                    tmp = '';
                    continue;
                tmp += c;
            value = tmp;

            key = unquote(key);

            # 开始迭代生成字典
            # 更新tmpdict
            self.__update_key_dict(tmpdict,self.__decode_body_key(key,value))

        return tmpdict;

    def __decode_body_key(self,key,value):
        strlist = list();
        # 利用栈匹配括号
        stack_count = 0;

        tmp = '';
        tlen = 0;
        for i in range(0,len(key)):
            if key[i] is '[':
                tlen = i;
                break;
            tmp += key[i];

        strlist.append(tmp);


        key = key[tlen:];
        tmp = '';
        for c in key:
            if c is '[':
                stack_count += 1;
                continue;
            elif c is ']':
                stack_count -= 1;
                if stack_count is 0:
                    strlist.append(tmp);
                    tmp = '';
                continue;
            tmp += c;

        if len(strlist) is 0:
            return None

        tmpdict = dict();
        tmpdict[strlist[len(strlist)-1]] =  unquote(value);

        for tmpkey in reversed(strlist[:len(strlist)-1]):
            mm = dict()
            mm[tmpkey] = tmpdict
            tmpdict = mm;
        return tmpdict

    def __update_key_dict(self,tmpdict,elem):
        # 处理key相同时的情况
        # 在递归中加入类型判断 使得算法更加难以理解
        while tmpdict.get(list(elem.keys())[0],None):
            key = list(elem.keys())[0];
            if (type(elem.get(key)) is not dict and type(tmpdict.get(key)) is not dict):
                if (type(tmpdict.get(key)) is not list):
                    td = tmpdict.get(key);
                    tlist = list();
                    tlist.append(tmpdict.get(key));
                    tlist.append(elem.get(key));
                    tmpdict[key] = tlist;
                    return;
                else:
                    tmpdict[key].append(elem.get(key));
                    return;

            tmpdict = tmpdict.get(key);
            elem = elem.get(key);

        tmpdict.update(elem);


decodeHtmlBody =  DecodeHtmlBody();




