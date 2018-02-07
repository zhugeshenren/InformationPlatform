# 将所有的数据库操作都封装在这个类里边
from app.DataAccessP.IDatabaseF import IDatabase


# 实现
class Database(IDatabase):
    def Select(self):
        return
