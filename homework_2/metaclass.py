import re


class CustomMeta(type):
    """Кастомный метакласс, который и заменяет методы в CustomClass"""
    def __call__(cls, *args, **kwargs):
        cls_obj = super().__call__(*args, **kwargs)
        attr_to_change = {}
        for item in dir(cls_obj):
            if not re.fullmatch(r'^__\w+__$', item):
                attr_to_change[item] = getattr(cls_obj, item)
        print(attr_to_change)
        for attr, logic_of_attr in attr_to_change.items():
            setattr(cls_obj, "custom_" + attr, logic_of_attr)
            try:
                delattr(cls, attr)
            except AttributeError:
                delattr(cls_obj, attr)
        return cls_obj


class CustomClass(metaclass=CustomMeta):
    """Кастомный класс, основанный на метаклассе, в котором все методы
       с префиксом custom_"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def __add__(self, other):
        return 1

    @staticmethod
    def line():
        """Метод, который мы заменим на кастомный"""
        return 100
