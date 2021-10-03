from random import choice

while True:
    dadu1 = choice(range(1,7))
    dadu2 = choice(range(1,7))
    print('Dadu pertama anda adalah {}'.format(dadu1))
    print('Dadu kedua anda adalah {}'.format(dadu2))
    print('Jumlah dadu anda adalah {}'.format(dadu1+dadu2))
    
    while True:
        lagi = input('Apakah akan mengocok dadu lagi? (ya/tidak): ')
        if lagi.lower() in ['ya','tidak']:
            break
    else:
        continue
    
    if lagi.lower() == 'ya':
        continue
    elif lagi.lower() == 'tidak':
        break
