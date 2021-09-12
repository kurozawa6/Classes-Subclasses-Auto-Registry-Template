class ObjectBase:
    subclasses = {}
    label = 'Inherited Label.'

    def __init__(self, cust_parent_val1 = 'Default Custom Parent Value.',):
        self.cust_parent_val1 = cust_parent_val1

    def __init_subclass__(cls):
        cls.subclasses[cls._SUB_OBJECT_TYPE] = cls

    @classmethod
    def create(cls, sub_object_type, **params):
        if sub_object_type not in cls.subclasses:
            raise ValueError(f'Invalid sub object type: {sub_object_type}')
        return cls.subclasses[sub_object_type](**params)


class SubObject1(ObjectBase):
    _SUB_OBJECT_TYPE = 'sub_object_type1'
    label = 'Label For Sub Object Type1.'

    def __init__(self, child_cust_value1 = 'Default Custom Value 1.', child_mutable1 = None, **kwargs):
        super().__init__(**kwargs)
        self.child_cust_value1 = child_cust_value1
        self.child_mutable1 = child_mutable1 if child_mutable1 is not None else []


class SubObject2(ObjectBase):
    _SUB_OBJECT_TYPE = 'sub_object_type2'

    def __init__(self, child_cust_value2 = 'default', child_mutable2 = None, **kwargs):
        super().__init__(**kwargs)
        self.child_cust_value2 = child_cust_value2
        self.child_mutable2 = child_mutable2 if child_mutable2 is not None else []

        
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
# []
# Modified Value 2.
