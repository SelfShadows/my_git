import threading

try:
    from greenlet import getcurrent as get_ident
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident


class Local(object):
    __slots__ = ("__storage__", "__ident_func__")  # 允许对象里面有哪些字段

    def __init__(self):
        object.__setattr__(self, "__storage__", {})
        object.__setattr__(self, "__ident_func__", get_ident)
        self.aa =123

    def __getattr__(self, name):
        try:
            return self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        ident = self.__ident_func__()
        storage = self.__storage__
        try:
            storage[ident][name] = value
        except KeyError:
            storage[ident] = {name: value}

    def __delattr__(self, name):
        try:
            del self.__storage__[self.__ident_func__()][name]
        except KeyError:
            raise AttributeError(name)

obj = Local()
obj.stack = []
obj.stack.append('小李')
obj.stack.append('老小')
obj.stack.pop()
obj.request = 456
print(obj.__storage__, obj.__storage__.get(get_ident())['stack'])
print('*************************************************************')


class LocalStack(object):

    def __init__(self):
        self._local = Local()

    def push(self, obj):
        """Pushes a new item to the stack"""
        rv = getattr(self._local, "stack", None)
        if rv is None:
            self._local.stack = rv = []
        rv.append(obj)
        return rv

    def pop(self):
        """Removes the topmost item from the stack, will return the
        old value or `None` if the stack was already empty.
        """
        stack = getattr(self._local, "stack", None)
        if stack is None:
            return None
        elif len(stack) == 1:
            return stack[-1]
        else:
            return stack.pop()

    @property
    def top(self):
        """The topmost item on the stack.  If the stack is empty,
        `None` is returned.
        """
        try:
            return self._local.stack[-1]
        except (AttributeError, IndexError):
            return None

obj = LocalStack()
obj.push('小李')
obj.push('老肖')
obj.pop()
print(obj._local.stack)
print('*************************************************************')


class RequestContent(object):
    def __init__(self):
        self.request = "xx"
        self.session = 'oo'


_lookup_req_object =LocalStack()
_lookup_req_object.push(RequestContent())
obj = _lookup_req_object.top
print(obj.session)
print(obj.request)
print('*************************************************************')


def get_request_or_session(arg):
    ctx = _lookup_req_object.top
    return getattr(ctx, arg)  # ctx.request/ ctx.session
import functools
session = functools.partial(get_request_or_session, 'session')
request = functools.partial(get_request_or_session, 'request')
print(request())
print(session())