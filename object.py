import sys
from operate_gene import *
from execute import *
SIZE = 600
class LSystemObj():
    
    def __init__(self, gene):
        
        self._gene = gene

    def life(self):
        self.energy = exe_it(self._gene)
    def breed(self, obj_list):
        for _ in range(random.randint(0,(SIZE-len(obj_list))//9)):
            if len(obj_list)<SIZE:

                obj_list.append(LSystemObj(self._gene))
        for _ in range(random.randint(0,(SIZE-len(obj_list))//12)):
            if len(obj_list)<SIZE:
                if gs:=variation(self._gene):

                    obj_list.append(LSystemObj(gs))
    def __repr__(self):
        return self.energy.__repr__()
    
def init_obj_list(n) :
    return [LSystemObj(get_genes()) for i in range(n)]

def run_list(obj_list):
    for o in obj_list:
        o.life()
    obj_list = list(filter(lambda x:x.energy>4,obj_list))
    obj_list.sort(key = lambda x:x.energy)
    
    if len(obj_list):
        print(obj_list[0]._gene,end = "\n")
    if len(obj_list)-1>0:
        obj_list.pop()
    obj_child_list = []
    for o in obj_list:
        o.breed(obj_child_list)
    return obj_child_list
    

if __name__ == "__main__":
    
    box = init_obj_list(SIZE)
    for i in range(1200):
        box = run_list(box)
