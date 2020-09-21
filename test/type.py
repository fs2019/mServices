

'''
元类
type
metaclass
'''

User=type('User',(),{
    'say': lambda self,msg: 'hi %s' %msg
})
u=User()
print(u.say('jack'))




class BaseField():
    pass
class CharField(BaseField):
    def __init__(self,length):
        self.length=length
class IntField(BaseField):
    pass
class BaseModelMeta(type):
    def __new__(cls, name, bases,attrs):
        print('--BaseModelMeta--',name)
        print('--BaseModelMeta--',bases)
        print('--BaseModelMeta--',attrs)
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        fields={}
        for key,field in attrs.items():
            if isinstance(field,BaseField):
                fields[key]=field
        table=attrs.get('__tablename__',name.lower())
        attrs['fields']=field
        attrs['table']=table
        return type.__new__(cls,name,bases,attrs)

class Model(metaclass=BaseModelMeta):
    def create(self):
        print('---create---')
        sql='create table %s(%s)'
        table_name=self.table
        columns=['%s %s' %(key,'varchar(%s)'% field.length \
            if isinstance(field,CharField) else 'Integer') \
            for key,field in self.fields.items()]
        sql=sql % (table_name,','.join(columns))
        print(sql)
    def save(self):
        pass
    def delete(self):
        pass
    def query(self):
        pass
class Person(Model):
    __tablename__='t_person'
    id=IntField()
    name=CharField(50)
    city=CharField(20)
p=Person()
p.create()
