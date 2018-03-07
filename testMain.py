

from app.Extension.Encryption.UniqueKeyOper import UniqueKey

# 程序的测试入口
if __name__ == "__main__":
    un = UniqueKey();
    t = un.encode("zhuge","shenren")
    print(t);
    pass