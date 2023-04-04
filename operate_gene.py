import collections
import random

gene_char = "XYZF+-[]"

def variation(genes):
    index = random.randint(0,3)
    gene = list(genes[index])
    new_char = gene_char[random.randint(0,7)]
    if new_char == '[' or new_char == ']':
        gene[random.randint(0,9)]='['
        gene[random.randint(0,9)]=']'
    else:
        k =random.randint(0,9)
        if gene[k] ==']' or gene[k]=='[':
            gene[random.randint(0,9)] = new_char
        gene[k] = new_char
    if is_gene(gene):
        genes = list(genes)
        genes[index] = ''.join(gene)
        genes = tuple(genes)
        if random.randint(1,9)>7:
            return variation(genes)
        return genes
    else:
        return None

def is_gene(gene):
    stack = collections.deque()
    for i in gene:
        if i == '[':
            stack.append(i)
        if i == ']':
            if len(stack):
                stack.pop()
            else:
                return False
    if len(stack):
        return False
    return True

def get_gene():
    
    gene_ = ""
    for i in (random.randint(0,7) for j in range(10)):
        gene_ += gene_char[i]

    if is_gene(gene_):
        return gene_
    else:
        return get_gene()
def get_genes():

    return tuple(get_gene() for i in range(4))

if __name__ == "__main__":
    genes = get_genes()
    print(genes)
    if gs:=variation(genes):
        print(gs)

    
