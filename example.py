
def func(*args, **kwargs):
    print(f'Args : {args[1]}')
    g = kwargs.get('two')
    print(f'Kwargs : {g}')



func(1, 3, 2, one= 1,  two=2, three=3)
 