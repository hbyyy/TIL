def get_description():
    '''

    :return: random weather -> str
    '''
    from random import choice
    possiblilties = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possiblilties)
