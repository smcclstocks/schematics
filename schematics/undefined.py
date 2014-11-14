class UndefinedType(object):

    __instances = {}

    def export_repr(self, field):
        return None

    def __str__(self):
        return 'Undefined'

    def __repr__(self):
        return 'Undefined'

    def __eq__(self, other):
        return (type(self) is type(other)
                or (type(other) is UndefinedType
                    and issubclass(type(self), UndefinedType)))

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return not self == other

    def __gt__(self, other):
        return False

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return self == other

    def __nonzero__(self):
        return False

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = object.__new__(cls)
        return cls.__instances[cls]

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if type(self) is UndefinedType:
            raise TypeError("'UndefinedType' object does not support attribute assignment")
        else:
            return object.__setattr__(self, name, value)


Undefined = UndefinedType()


def has_value(arg):
    return arg != Undefined and arg is not None

