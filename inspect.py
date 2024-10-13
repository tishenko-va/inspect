import pprint
import inspect
# Тип объекта.
#   - Атрибуты объекта.
#   - Методы объекта.
#   - Модуль, к которому объект принадлежит.
#   - Другие интересные свойства объекта, учитывая его тип (по желанию
# методы = [a для a в dir(i), если можно вызвать (getattr(i, a))]
# атрибуты = [a для a в dir(i), если нельзя вызвать (getattr(i, a))]
def introspection_info(obj):
    type_ = type(obj)
    attr_ = dir(obj)
    metods_ = [method for method in attr_ if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {f'type:{type_} attributes:{attr_} metods:{metods_} module:{module}'}
    return info

number_info = introspection_info(42)
print(number_info)
