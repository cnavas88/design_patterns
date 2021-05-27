# Method 1 - A decorator.

def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class SingletonDecorator():
    def __init__(self, value):
        self.value = value

# Method 2 - A class with thread safe.

from threading import Lock, Thread

class Singleton(object):
    _instance = None
    _lock = Lock()

    def __new__(class_, *args, **kwargs):
        with class_._lock:
            print(class_._instance)
            if not isinstance(class_._instance, class_):
                class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClass(Singleton):
    def __init__(self, value):
        self.value = value


def test_singleton(value):
    print("SINGLETON IN THREAD")
    singleton = MyClass(value)
    print(singleton.value)


if __name__ == '__main__':
    # Client code Method 1

    s1 = SingletonDecorator(1)
    s2 = SingletonDecorator(2)

    print('My singleton 2 value: {}'.format(s1 == s2))
    print('My singleton 2 value: {}'.format(s2.value))
    print('My singleton 1 value: {}'.format(s1.value))

    s2.value = 3

    print('My singleton 2 value: {}'.format(s2.value))
    print('My singleton 1 value: {}'.format(s1.value))

    # Client code Method 2
    s1 = MyClass(1)

    print('My singleton 1 value: {}'.format(s1.value))

    s2 = MyClass(2)
    s2.value = 3

    print('My singleton 2 value: {}'.format(s1 == s2))
    print('My singleton 2 value: {}'.format(s2.value))
    print('My singleton 1 value: {}'.format(s1.value))

    # Client code Method 2 with Threads
    process1 = Thread(target=test_singleton, args=(1,))
    process2 = Thread(target=test_singleton, args=(2,))
    process1.start()
    process2.start()

