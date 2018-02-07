from app.Extension.BaseField import Field;

# 调用父类的方法设置数据类型为 varchar(100)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
