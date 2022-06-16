import os
from os.path import lexists

class MoveFileCommand(object):
    def __init__(self,src,dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self.rename(self.src,self.dest)

    def undo(self):
        self.rename(self.dest,self.src)

    def rename(self,src,dest):
        print(u"Redenumesc %s ca %s" % (src,dest))
        os.rename(src,dest)

command_stack = []
command_stack.append(MoveFileCommand('bugs.txt','bunny.txt'))
command_stack.append(MoveFileCommand('bunny.txt','stimpy.txt'))

assert not lexists("bugs.txt")
assert not lexists("bunny.txt")
assert not lexists("stimpy.txt")
try:
    with open("bugs.txt","w"):
        pass
    for cmd in command_stack:
        cmd.execute()

    for cmd in reversed(command_stack):
        cmd.undo()
finally:
    os.unlink("bugs.txt")