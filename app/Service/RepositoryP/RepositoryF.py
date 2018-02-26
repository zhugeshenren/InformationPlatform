import json

class Repository():
    def Exec(self):
        return;

    def BaseToDict(self,result):
        tdict = list()

        print(result)
        for tmp in result:
            tdict.append(tmp.ToDict())

        return tdict;
