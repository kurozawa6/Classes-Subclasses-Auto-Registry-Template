class ObjectBase:
    __subclasses = {}
    label = 'Inherited Label.'

    def __init__(self, cust_parent_val1 = 'Default Custom Parent Value.',):
        self.cust_parent_val1 = cust_parent_val1

    def __init_subclass__(cls):
        cls.__subclasses[cls._subclass_type] = cls

    @classmethod
    def create(cls, _subclass_type, **params):
        if _subclass_type not in cls.__subclasses:
            raise ValueError(f'Invalid sub object type: {_subclass_type}')
        return cls.__subclasses[_subclass_type](**params)


class SubObject1(ObjectBase):
    _subclass_type = 'type1'
    label = 'Label For Sub Class Type1.'

    def __init__(self, child_cust_value1 = 'Default Custom Value 1.', child_mutable1 = None, **kwargs):
        super().__init__(**kwargs)
        self.child_cust_value1 = child_cust_value1
        self.child_mutable1 = child_mutable1 if child_mutable1 is not None else []


class SubObject2(ObjectBase):
    _subclass_type = 'type2'

    def __init__(self, child_cust_value2 = 'default', child_mutable2 = None, **kwargs):
        super().__init__(**kwargs)
        self.child_cust_value2 = child_cust_value2
        self.child_mutable2 = child_mutable2 if child_mutable2 is not None else {}


# Sample Output

print('Object A:')
print(A := ObjectBase.create('_subclass_type1', cust_parent_val1 = 'Modified Parent Value1.'))
print(A.label)
print(A.cust_parent_val1)
print(A.child_mutable1)
print(A.child_cust_value1 + '\n')
print(B := ObjectBase.create('_subclass_type2', child_cust_value2 = 'Modified Value 2.'))
print('Object B:')
print(B.label)
print(B.cust_parent_val1)
print(B.child_mutable2)
print(B.child_cust_value2)


# Object A:
# <__main__.SubObject1 object at 0x000001F538AE3490>
# Label For Sub Object Type1.
# Modified Parent Value1.
# []
# Default Custom Value 1.
# 
# <__main__.SubObject2 object at 0x000001F538AE3550>
# Object B:
# Inherited Label.
# Default Custom Parent Value.
# {}
# Modified Value 2.
