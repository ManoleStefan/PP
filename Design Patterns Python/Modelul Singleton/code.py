class SingletonType(type):
    instance = None
    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SingletonType,cls).__call__(*args,**kwargs)
        else:
            print("Only one instance allowed.")
        return cls.instance


class Singleton(object):
    #__metaclass__ = SingletonType # the Singleton class is an instance of SingletonType class
    instance = None
    def __init__(self):
        print("Init Singleton.")
        if not self.instance:
            self.instance = self
        else:
            print("Only one instance allowed")

    def do_something(self):
        print("Motherfucking Singleton")


s = Singleton()
s.do_something()
