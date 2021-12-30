tipo = str(input())
classe = str(input())
alimento = str(input())

if tipo == 'vertebrado':
    if classe == 'ave':
        if alimento == 'carnivoro':
            print('aguia')
        else: print('pomba')

if tipo == 'vertebrado':
    if classe == 'mamifero':
        if alimento == 'onivoro':
            print('homem')
        else: print('vaca')

if tipo == 'invertebrado':
    if classe == 'inseto':
        if alimento == 'hematofago':
            print('pulga')
        else: print('lagarta')

if tipo == 'invertebrado':
    if classe == 'anelideo':
        if alimento == 'hematofago':
            print('sanguessuga')
        else: print('minhoca')
