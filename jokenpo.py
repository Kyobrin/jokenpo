import random
print ('========JOKENPO GAME=======')
npc = ['PEDRA', 'PAPEL', 'TESOURA']
print ('VOCÊ OUSA ME DESAFIAR PLEBE?')
print ('''ESCOLHA UM DESSES 3
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')

escolha = int(input('ESCOLHA UM DESSES E VEJA SE GANHARÁ DE MIM MERO PLEBEU: '))


match escolha:
    case 1:
        print ('-='*20)
        print ('Você escolheu PEDRA')
        ia =  random.choice(npc)
        print (f'EU ESCOLHO {ia} HAHAHA' )
        if ia == 'PEDRA':
            print ('DROGA, FOI UM EMPATE!!')
        elif ia == 'PAPEL':
            print ('VOCÊ PERDEU PLEBE HAHAHA!!')
        elif ia == 'TESOURA':
            print ('DROGA FUI VENCIDO?? NÃOOO!!')
        print ('-='*20)
    case 2:
        print ('-='*20)
        print ('Você escolheu PAPEL')
        ia =  random.choice(npc)
        print (f'EU ESCOLHO {ia} HAHAHA' )
        if ia == 'PAPEL':
            print ('DROGA, FOI UM EMPATE!!')
        elif ia == 'TESOURA':
            print ('VOCÊ PERDEU PLEBE HAHAHA!!')
        elif ia == 'PEDRA':
            print ('DROGA FUI VENCIDO?? NÃOOO!!')
        print ('-='*20)
    case 3:
        print ('-='*20)
        print ('Você escolheu TESOURA')
        ia =  random.choice(npc)
        print (f'EU ESCOLHO {ia} HAHAHA' )
        if ia == 'TESOURA':
            print ('DROGA, FOI UM EMPATE!!')
        elif ia == 'PEDRA':
            print ('VOCÊ PERDEU PLEBE HAHAHA!!')
        elif ia == 'PAPEL':
            print ('DROGA FUI VENCIDO?? NÃOOO!!')
        print ('-='*20)


