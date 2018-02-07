
# 定义一个基础的Field  主要作为后期 ORM的开发，前期只是表明存在这个结构
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)