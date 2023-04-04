
import iteration
import draw

def exe_it(genes):
    init = "X"
    laws = (('X',genes[0]),('Y',genes[1]),('Z',genes[2]),('F',genes[3]))
    expression = iteration.iter_expressions(init,laws,2)
    return draw.draw_expression(expression,5,36,90,1)

if __name__ == '__main__':

    laws = [('F','+F-[F-F]+[-F+F]')]
    
    
    #print(expression)
    
    
'''
    laws = [('G','GFX[+++++GFG][-----GFG]'),
            ('X','F-XF')]

            
'''
