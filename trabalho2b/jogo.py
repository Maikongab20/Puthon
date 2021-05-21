import random

perguntas = {
    'facil' : ['Onde se localiza Machu Picchu?', 'Quem inventou a lâmpada?', 'Quais as duas línguas mais faladas no mundo?', 'Quem pintou Mona Lisa?','Qual a especialidade do otorrinolaringologista?'],
    'medio' : ['Qual das alternativas traz uma das medidas do presidente Trump, anunciada em 2017, que causou polêmica?','Qual destas frases foi dita pelo Papa Francisco?','Qual a primeira mulher a ganhar um prêmio Nobel?','Como morreu Saddam Hussein?','Países Baixos, Mianmar e Irã são países que mudaram de nomes. Antes eram chamados respectivamente de:'],
    'dificil' : ['Em que país se localizava Auschwitz, o maior campo de concentração nazista?','Quem é Abraham Weintraub?','O que é um Papiloscopista?','O que é Ortorexia?','Que tipo de tempestade é um haboob?']
}

respostas = {
    'facil': {
        'Onde se localiza Machu Picchu?': 'B',
        'Quem inventou a lâmpada?': 'C',
        'Quais as duas línguas mais faladas no mundo?': 'B',
        'Quem pintou Mona Lisa?': 'A',
        'Qual a especialidade do otorrinolaringologista?': 'E',
    },
    'medio': {
        'Qual das alternativas traz uma das medidas do presidente Trump, anunciada em 2017, que causou polêmica?':'C',
        'Qual destas frases foi dita pelo Papa Francisco?':'C',
        'Qual a primeira mulher a ganhar um prêmio Nobel?':'E',
        'Como morreu Saddam Hussein?':'D',
        'Países Baixos, Mianmar e Irã são países que mudaram de nomes. Antes eram chamados respectivamente de:':'C'
    },
    'dificil': {
        'Em que país se localizava Auschwitz, o maior campo de concentração nazista?':'B',
        'Quem é Abraham Weintraub?':'A',
        'O que é um Papiloscopista?':'B',
        'O que é Ortorexia?':'A',
        'Que tipo de tempestade é um haboob?':'C'
    }
}

alternativas = {
    'Onde se localiza Machu Picchu?': ['Colômbia', 'Peru','China','Bolivia','Índia'],
    'Quem inventou a lâmpada?': ['Graham Bell','Steve Jobs','Thomas Edison','Henry Ford','Santos Dumont'],
    'Quem pintou Mona Lisa?': ['Leonardo da Vinci', 'Salvador Dalí', 'Van Gogh', 'Tarsila do Amaral', 'Pablo Picasso']
    'Qual a especialidade do otorrinolaringologista?': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', ''] 
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
    '': ['', '', '', '', '', '']
}

pergunta = perguntas['dificil'][random.randint(0, 4)]
k = respostas['dificil'][pergunta][0]
print("\nPergunta: {}\nResposta: {}".format(pergunta,k))