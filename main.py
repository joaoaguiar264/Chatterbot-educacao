from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Bot')

trainer = ListTrainer(bot)
materiaEscolhida = False

trainer.train([
    'Oi',
    'Olá, sou o Edu.Bot e irei lhe auxiliar hoje! Por favor, escolha uma das disciplinas abaixo:\n [1]- Matemática\n [2]- Ciências\n [3]- História',
    '',
    'Olá, sou o Edu.Bot e irei lhe auxiliar hoje! Por favor, escolha uma das disciplinas abaixo:\n [1]- Matemática\n [2]- Ciências\n [3]- História'
])

matematica = [
    'Quanto é 32 + 54?',
    'O resultado de 32 + 54 é 86.',
    'Qual é a raiz quadrada de 81?',
    'A raiz quadrada de 81 é 9.',
    'Como cálcular a área de um quadrado?',
    'A área de um quadrado é igual a altura multiplicado pela lárgura'
]

ciencias = [
    'Quantos dentes possui um ser humano adulto?',
    'Um ser humano adulto que possui todos os dentes na boca, tem 32 dentes.',
    'O que é a fotossíntese?',
    'A fotossíntese é o processo pelo qual as plantas verdes, algas e algumas bactérias transformam a luz solar em energia química.',
]

historia = [
    'Quem descobriu o Brasil?',
    'Pedro Álvares Cabral descobriu o Brasil.',
    'Em que ano começou a Segunda Guerra Mundial?',
    'A Segunda Guerra Mundial começou em 1939.',
]

print('Olá, sou o Edu.Bot e irei lhe auxiliar hoje! Por favor, escolha uma das disciplinas abaixo:\n [1]- Matemática\n [2]- Ciências\n [3]- História')
while True:
    request = input('Você: ')
    if request.lower() == 'sair':
        print('Bot: Tchau')
        break
    elif not materiaEscolhida:
        if request.lower() == '1':
            trainer.train(matematica)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        elif request.lower() == '2':
            trainer.train(ciencias)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        elif request.lower() == '3':
            trainer.train(historia)
            materiaEscolhida = True
            print('Bot: Ótimo! Você pode me fazer um pergunta.')
        else:
            print('Bot: Não entendi, poderia repetir?')
    else:
        response = bot.get_response(request)
        if float(response.confidence) < 0.1:
            print('Bot: Desculpe, não possuo resposta para esta pergunta.')
        else:
            print('Bot:', response)
