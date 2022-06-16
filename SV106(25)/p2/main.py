class Component:
    def printComponent(self,total_level):
        pass

class LeafComponent(Component):
    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.initial_level = level

    def printComponent(self,total_level):
        if self.level <= total_level:
            print(self.level*"\t" + " " + self.name)
        self.level += 2

    def reset(self):
        self.level = self.initial_level

class CompositeComponent(Component):
    def __init__(self,name,list,level):
        self.name = name
        self.list = list
        self.level = level
        self.initial_level = level

    def printComponent(self,total_level):
        if self.level <= total_level:
            for i in self.list:
                i.printComponent(total_level)
            self.level += 2

    def reset(self):
        for i in self.list:
            i.reset()
        self.level = self.initial_level

if __name__ == '__main__':
    l1 = [LeafComponent("Add Project..",2),LeafComponent("Open",2),CompositeComponent("New..",[LeafComponent("Project",4),LeafComponent("Project from existing source",4)],2),LeafComponent("Refactor..",2)]

    c1 = CompositeComponent("File",l1,0)

    opt = (int)(input("Alegeti nivelul meniului: "))
    lv = opt

    print(c1.name)
    c1.printComponent(opt)
    c1.reset()
    opt = (int)(input("Doriti sa mergeti inapoi: "))

    if opt == 1:
        print(c1.name)
        c1.printComponent(lv - 2)