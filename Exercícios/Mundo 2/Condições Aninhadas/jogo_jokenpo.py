'Jogo de jokenpô'

import random

print('Pedra, papel ou tesoura?')
escolha_humana = str(input()).lower()
jkp = ['pedra', 'papel', 'tesoura']
escolha_bot = random.choice(jkp)
print('Jo...ken...PÔ!!!')
print('Eu escolhi', escolha_bot)
if escolha_humana == 'tesoura' and escolha_bot == 'papel':
    print('Você Ganhou!!!')
elif escolha_humana == 'pedra' and escolha_bot == 'tesoura':
    print('Você Ganhou!!!')
elif escolha_humana == 'papel' and escolha_bot == 'pedra':
    print('Você Ganhou!!!')

elif escolha_bot == 'tesoura' and escolha_humana == 'papel':
    print('Eu ganhei hahahaha!!!')
elif escolha_bot == 'papel' and escolha_humana == 'pedra':
    print('Eu ganhei hahahaha!!!')
elif escolha_bot == 'pedra' and escolha_humana == 'pedra':
    print('Eu ganhei hahahaha!!!')

else: 
    print('Empate! vamos novamente')
