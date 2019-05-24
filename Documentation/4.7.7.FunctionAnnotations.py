# -*- coding:utf-8 -*-
def f(ham: str, eggs: str = 'eggs') -> str:
    """
    传参标注只用于提示传参类型，不会对实际传参进行校验
    """
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
