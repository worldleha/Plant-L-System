

def iter_expression(initzation, law):
    iterating = initzation
    iterating = iterating.replace(*law)
    return iterating


def iter_expressions(expression, laws, n):
    for _ in range(n):
        for law in laws:
            expression = iter_expression(expression, law)
    return expression
            
def remove_char(expression, char):
    return expression.replace(char,'')
## '+LX-'  ('X','[+LX-]')

if __name__ == "__main__":
    expression = iter_expressions('+LX-',[('X','[+LX-XL]'),('X','[+L-XL]')],5)
    print(remove_char(expression, 'X'))
