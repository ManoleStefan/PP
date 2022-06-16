import copy

def memento(obj,deep=False):
    state = copy.deepcopy(obj.__dict__) if deep else copy.copy(obj.__dict__)
    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)
    return restore()

class Transaction(object):
    deep = False
    states = []
    def __init__(self,deep,*targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [memento(target,self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()

class Transactional(object):
    def __init__(self,method):
        self.method = method

    def __get__(self, obj,T):
        def transaction(*args,**kwargs):
            state = memento(obj)
            try:
                return self.method(obj,*args,**kwargs)
            except Exception as e:
                state()
                raise e
        return transaction

class NumObj(object):
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return '<%s : %r>'%(self.__class__.__name__,self.value)

    def increment(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = '1111'
        self.increment()


num_obj = NumObj(-1)
print(num_obj)
a_transaction = Transaction(True,num_obj)
try:
    for i in range(3):
        num_obj.increment()
        print(num_obj)
        a_transaction.commit()
        print('--tranzactie finalizata')
    num_obj.value += 'x'
    print(num_obj)
except Exception:
    a_transaction.rollback()
    print('--tranzactie esuata - restauram la situatia anterioara')