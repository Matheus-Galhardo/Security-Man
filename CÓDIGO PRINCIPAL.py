import sys #importa o módulo que será necessário para algumas
           #funções no sistema.
import time #importa o módulo de tempo para o jogo.

# -- função de texto -----------------------------------------------------------
#esta função imprime o texto letra por letra simulando uma narração.
def texto_narrador (texto):
  #print(texto)
    for letra in texto:
        time.sleep(0.05)  #dá um tempo de espera para a saída
        sys.stdout.write(letra)   #digita letra por letra na saída
# -- fim da função de texto ----------------------------------------------------

# -- função de espera ----------------------------------------------------------
#esta função cria um tempo de espera na execução do jogo.
def espera(tempo): #ela recebe os segundos de espera como argumento.
  segundos = "." * tempo #os pontos são multiplicados, cada ponto é 1 segundo.
  for s in segundos:
    time.sleep(1)
    sys.stdout.write(s)
# -- fim função de espera ------------------------------------------------------

# -- função de escolha ---------------------------------------------------------
#esta função checa a validade do input recebido pelo jogador para as escolhas.
def escolha(escopo): #recebe a quantidade de opções disponíveis para o jogador
                     #durante o momento de escolha em que essa função é chamada.
  print(">> 0 - Sair do jogo") #escolha padrão para sair do jogo.
  while True:
    try:
      acao = int(input(">>[")) #aqui o jogador escolhe a opção desejada
    except ValueError: #caso o jogador digite algo além de número inteiro.
      print("\nNarrador: Você digitou algo inválido. Escolha apenas o número "
            + "correspondente à ação.\n")
      continue
    if acao < 0 or acao > escopo: #se o número escolhido for além do escopo
                                  #de opções, será invalidado.
      print("\nNarrador: Opção inválida. Escolha o número entre as opções "
            + "apresentadas.\n")
    elif acao == 0: #jogador escolheu sair do jogo.
      print("Obrigado por jogar!")
      sys.exit("O jogo foi encerrado")  #comando para sair encerrar o jogo.
    else:
      break
  print("") #print para criar uma nova linha
  return acao
# -- fim da função de escolha --------------------------------------------------

# -- função de criação de jogador ----------------------------------------------
#esta função irá criar a classe que representa o jogador.
def criar_jogador():

  texto_narrador("Primeiro me diga você é menino ou menina?"
                + "\n\n>> 1 - Menino\n>> 2 - Menina") #texto de introdução.
  genero = escolha(2) #define o gênero do jogador.
  texto_narrador("Alice: E qual o seu primeiro nome, agente?\n")
  while True:
    try:
      nome = str(input(">>[ ")) #define o nome do jogador.
      break
    except ValueError:
      print("\nAlice: Seu nome não pode ser um número hahaha.\n")
      continue

  texto_narrador("\nAlice: Agora me diga qual a sua idade?\n")
  while True:
    try:
      idade = int(input(">>[ ")) #define a idade do jogador.
      if idade < 14 or idade > 17: #o escopo do projeto é para jogadores entre
                                   #14 e 17 anos.
        print("\nAlice: Desculpe, nós somente aceitamos agentes com idade "
              + "entre 14 e 17 anos.\n")
        continue
      else:
        break
    except ValueError:
      print("\nAlice: Sua idade não pode ser uma letra. Tem que ser um número "
            + "inteiro hahaha.\n")
      continue

  texto_narrador("\nAlice: E qual seu ano escolar?\n")
  while True:
    try:
      ano = int(input(">>[ ")) #define o ano escolar do jogador.
      if ano < 1 or ano > 2: #o escopo do projeto é para o 1º e 2º ano.
        print("\nAlice: Nosso programa é apenas para alunos entre o 1º e 2º.")
        continue
      else:
        break
    except ValueError:
      print("\nAlice: Me diga só o número do ano escolar. Está bem?\n")
      continue

  texto_narrador("\nAlice: Agora a pergunta mais importante! Você prefere "
                + "cachorro ou gato?\n")
  print(">> 1 - Cachorro\n>> 2 - Gato")
  animal = escolha(2) #define o animal favorito do jogador.
  if animal == 1:
    texto_narrador("Alice: Eu também prefiro, eles são bem alegres!")
    animal = "cachorro"
  elif animal == 2:
    texto_narrador("Alice: Também gosto muito da calmaria dos gatos. Hahaha")
    animal = "gato"

  return Jogador(nome, idade, ano, genero, animal) #cria o objeto.
# -- fim da função de criação de jogador ---------------------------------------

# -- função de pontuação final -------------------------------------------------
#esta função será utilizada para calcular o placar final do jogador e retornar
#como feedback para o mesmo, incentivando-o a rejogar.
def pontuacao_final(pontuacao_f, curiosidade_f, tentativas_f):
  global avaliacao_f #variável que define o placar final.
  print("Alice: Hoje você atendeu um total de 6 clientes!\n")
  espera(3)
  print("\n\nAlice: Foram necessárias: " + str(tentativas_f)
        + " tentativas para solucionar todos os problemas.\n")

  if pontuacao_f == 26: #26 é o valor inicial da pontuação que diminui a cada
                        #resposta errada do jogador.
    if jogador.genero == 1:
      titulo = "SecurityMan" #título final dado ao jogador. Diferencia caso
                              #seja menino ou menina.
    elif jogador.genero == 2:
      titulo = "SecurityWoman"
    nivel = "profissional" #nivel de habilidade do jogador. Utilizado no texto
                           #de avaliação final.
    continuacao = ("nossos agentes de mais destaque. "
                  + "Aqueles que têm o melhor raciocínio para os problemas. "
                  + "Meus parabéns!!!") #este texto foi passado à uma variável
                                       #pois será diferente para cada um dos 3
                                       #níveis de jogador.
  elif pontuacao_f >= 20: #caso o jogador erre 6 vezes, irá ter o segundo nível
                         #de pontuação.
    if jogador.genero == 1:
      titulo = "SecurityBoy" #também muda conforme gênero do jogador.
    elif jogador.genero == 2:
      titulo = "SecurityGirl"
    nivel = "habilidoso"
    continuacao = ("nossos agentes com muita habilidade, o único abaixo do "
                   + "SecurityMan.\nÉ uma ótima posição, mas você ainda pode "
                   + "alcançar o maior nível tentando novamente. Muito bem e "
                   + "continue se dedicando!")
  elif pontuacao_f < 20 : #mais de 16 erros levam à pontuação de menor nível.
    if jogador.animal == "cachorro": #título muda conforme o animal favorito.
      titulo = "SecurityDog"
    elif jogador.animal == "gato":
      titulo = "SecurityCat"
    nivel = "médio"
    continuacao = ("nossos agentes com um bom nível de habilidade, mas que "
                   + "ainda precisam de muito treinamento.\nVocê foi bem mas "
                   + "aindatem bastante a melhorar, agente. Pode-se alcançar "
                   + "os dois níveis de habilidade que estão acima deste."
                   + "\nContinue tentando e estudando, você irá se tornar "
                   + "um SecutiryMan/Woman em pouco tempo. Não desista, "
                   + "agente!!")

  if curiosidade_f == 3: #aqui será avaliado o quanto o jogador se interessou
                        #em saber das informações extras.
    tipo = "muito interessado"  #nível de interesse.
    continuacao2 = ("Gostei de ver! Você se mostrou um" + jogador.pronome_artigo
                    + " agente que está  disposto a aprender cada detalhe e "
                    + "estar sempre  atualizado. É este tipo de atitude que "
                    + "forma os melhores agentes!!")
  elif curiosidade_f > 0:
    tipo = "um pouco interessado"
    continuacao2 = ("Você mostrou que quer aprender mais, apesar de não ter "
                    + "tido interesse em todos os assuntos. É um ótimo começo, "
                    + "procure o que te interessa e se aprofunde no tópico."
                    + "\nSaiba que apenas os melhores fazem isso!")
  elif curiosidade_f <= 0:
    tipo = "sem interesse"
    continuacao2 = ("Você não procurou saber o porquê de cada tópico. Pense "
                    + "melhor, agente, como podemos ajudar os outros e nos "
                    + "ajudarmos se não temos conhecimento?\nProcure estudar "
                    + "bastante todo o tipo de assunto, é isso que os campeões "
                    + "fazem!")

  avaliacao_f = ("Com base na sua pontuação final, declaro seu título como "
                + titulo + " é um título de nível " + nivel
                + ".\nDesignado aos " + continuacao + "\nVocê foi um agente do "
                + "tipo " + tipo + ".\n" + continuacao2)
#por fim, o texto final foi passado à variável pois será utilizado na função
#'texto_narrador', achei a forma mais simples de utilizar a função.
  return avaliacao_f
# -- fim da função de pontuação final ------------------------------------------

# -- criação da classe de jogador ----------------------------------------------
class Jogador:  #classe que define os dados do jogador

    def __init__(jogador, nome, idade, ano, genero, animal):
        jogador.nome = nome
        jogador.idade = idade
        jogador.ano = ano
        jogador.genero = genero #aqui se determina o gênero para os pronomes
        jogador.animal = animal

        if genero == 1: #aqui serão definidos os pronomes com base no gênero
          jogador.pronome_sujeito = "ele"
          jogador.pronome_artigo = "o"
          jogador.pronome_possessivo = "dele"
          jogador.pronome_conjugal = "-lo"
          jogador.pronome_tratativo = "senhor"
        if genero == 2:
          jogador.pronome_sujeito = "ela"
          jogador.pronome_artigo = "a"
          jogador.pronome_possessivo = "dela"
          jogador.pronome_conjugal = "-la"
          jogador.pronome_tratativo = "senhora"
# -- fim da criação da classe de jogador ---------------------------------------

pontuacao = 26 #aqui é declarado a pontuação máxima. Irá diminuir dependendo do
               #desempenho do jogador.
curiosidade = 0
tentativas = 0 #curiosidade e tentativas começam em 0 e aumentam conforme o
                #jogador joga.

# -- começo do loop do jogo ----------------------------------------------------
print(""" _______  _______  _______           _______ __________________            _______  _______  _
(  ____ \(  ____ \(  ____ \|\     /|(  ____ )\__   __/\__   __/|\     /|  (       )(  ___  )( (    /|
| (    \/| (    \/| (    \/| )   ( || (    )|   ) (      ) (   ( \   / )  | () () || (   ) ||  \  ( |
| (_____ | (__    | |      | |   | || (____)|   | |      | |    \ (_) /   | || || || (___) ||   \ | |
(_____  )|  __)   | |      | |   | ||     __)   | |      | |     \   /    | |(_)| ||  ___  || (\ \) |
      ) || (      | |      | |   | || (\ (      | |      | |      ) (     | |   | || (   ) || | \   |
/\____) || (____/\| (____/\| (___) || ) \ \_____) (___   | |      | |     | )   ( || )   ( || )  \  |
\_______)(_______/(_______/(_______)|/   \__/\_______/   )_(      \_/     |/     \||/     \||/    )_)
                                                                                                     """) #print da tela título do jogo
print("                        ---| Bem-Vindo ao meu jogo 'Security Man' |---\n"
      + "---| Este é um jogo de texto, para escolher a opção desejada, digite "
      + "o número correspondente e aperte ENTER |---\n""") #print de tutorial.
print(">> 1 - Começar o jogo") #opção para iniciar o jogo. A opção de sair está
                               #inclusa na função de escolhas.

if escolha(2) == 1:
  print("Jogo iniciado!\n")
  while True: #loop principal do jogo
    texto_narrador("Narrador: Você se senta na frente do computador. Olha a "
                  + "data de hoje no canto inferior, hoje é 27 de Dezembro de "
                  + "2124.\nVocê navega entre os aplicativos e abre o "
                  + "TerraChat, um aplicativo de mensagens e e-mails. Logo "
                  + "sobe uma notificação à direita da tela, você tem uma nova "
                  + "solicitação de bate-papo!\n\nAbrir o bate-papo?\n")
    print(">> 1 - Abrir bate-papo")
    escolha(1)
    texto_narrador("Alice: Bom dia! Me chamo Alice Inspector, tudo bem com "
                  + "você??\n")
    print(">> 1 - Tudo ótimo!!\n>> 2 - Estou bem, obrigado.")
    escolha(2)
    texto_narrador("Alice: Fico feliz em ouvir isto! :) Falo da empresa Silver "
                  + "Shell, a maior empresa de segurança digital do Brasil!\n"
                  + "Estou aqui como recrutadora procurando pelos mais "
                  + "qualificados aspirantes à hackers do bem para nos ajudar. "
                  + "Como você já deve saber, estamos entrando no ano de 2125."
                  + "\nA internet está cada vez maior e mais perigosa. Nossa "
                  + "tecnologia avançou, temos carros voadores mas ainda "
                  + "enfrentamos desafios com a nossa segurança pessoal.\n"
                  + "A cada dia, o número de usuários que sofrem com a perda "
                  + "de dados e roubo digital aumenta. Os hackers estão por "
                  + "toda a parte do **cyberespaço!!!**\n Venho te convidar "
                  + "para o nosso programa de inteligência, sua função será "
                  + "encontrar falhas de segurança cybernética e usar a "
                  + "perspicácia para garantir a segurança de todos!\nVocê "
                  + "tem determinação para se tornar SECURITY MAN/WOMAN?\n")
    print(">> 1 - Sim, tenho!")
    escolha(1)
    texto_narrador("Alice: Certo!! Vamos, então, começar com o seu cadastro no "
                  + "nosso programa de super agentes!")

    jogador = criar_jogador() #chama a função que cria o jogador

    texto_narrador("Por último, para confirmar a sua identidade, preciso "
                  + "que me confirme o e-mail e senha que usou para entrar "
                  + "nesse chat.\n")
    print(">> 1 - Não posso passar essas informações.\n>> 2 - Posso confirmar "
          + "minha identidade de outras formas.\n>> 3 - email: "
          + jogador.nome.lower() + "@terramail.com || senha: "
          + jogador.nome.lower() + "12345")

    acao = escolha(3)
    if acao == 1:
      texto_narrador("Alice: Exatamente! Este tipo de informação é confidencial"
                    + ", parabéns! Não podemos passar senhas pessoais para "
                    + "desconhecidos! Isso foi um teste e você se saiu bem! "
                    + "hahaha")
    elif acao == 2:
      texto_narrador("Alice: Hahaha, isso foi apenas um teste, " + jogador.nome
                    + ". E Você passou. Não podemos passar senhas pessoais "
                    + "para desconhecidos!")
    elif acao == 3:
      texto_narrador("Alice: Hahaha, isso foi apenas um teste, " + jogador.nome
                    + ". Essas informações são confidenciais! Não podemos "
                    + "passar, nunca, senhas pessoais para desconhecidos. "
                    + "\nMesmo que seja para alguém dizendo ser do banco ou de "
                    + "empresas!")

    texto_narrador("Bem, considere essa pegadinha um aquecimento. A "
                  + "partir de agora, você irá se deparar com as mais diversas "
                  + "situações e precisará ser perspicaz na sua análise\npara "
                  + "garantir o cumprimento das normas de segurança digital. "
                  + "Não se preocupe, eu irei te acompanhar. Serei sua "
                  + "copiloto e sua parceira, me chame sempre que precisar. "
                  + "\nVamos começar! Para atender nosso clientes, utilizamos "
                  + "o aplicativo 'Security Field' lá encontraremos clientes "
                  + "que precisam de ajuda e vamos orientá-los da forma "
                  + "correta.\nProcure por nosso site 'Silver Shell' no "
                  + "navegador para baixar o app.\n")
    texto_narrador("Narrador: Você abre o navegador do Google e escreve o nome "
                  + "na barra de pesquisa. Lá, encontra 2 sites bem "
                  + "parecidos.\n")
    print(">> 1 - Clicar no primeiro resultado 'si1vershe11.com'\n>> 2 - "
          + "Clicar no segundo resultado 'silvershell.com'")

    while True:
      acao = escolha(2)
      if acao == 1:
        texto_narrador("Alice: Cuidado, " + jogador.nome + "!! Olhe atentamente "
                      + "o link do site que você vai clicar. Alguns hackers "
                      + "criam sites fakes imitando o nome de sites reais,"
                      + "\napenas com uma letra ou outra trocada, para enganar "
                      + "pessoas desavisadas na internet. Com atenção, "
                      + "verifique o site correto.\n")
        print(">> 1 - Clicar no primeiro resultado 'si1vershe11.com'\n>> 2 - "
              + "Clicar no segundo resultado 'silvershell.com'")
        continue
      elif acao == 2:
        texto_narrador("Alice: Este site mesmo. Você percebeu que o outro site "
                      + "tinha o nome parecido? Deve ser obra de algum hacker "
                      + "mal intencionado. Pronto, pode clicar em 'baixar'.\n")
        break

    texto_narrador("Narrador: Você clica para baixar o aplicativo\n")
    print("Baixando aplicativo")
    espera(5)
    texto_narrador("\n\nAlice: Enquanto baixa o app. Gostaria de ouvir uma "
                  + "curiosidade sobre tipos de hackers?\n")
    print(">> 1 - Sim, me conte!\n>> 2 - Não estou interessado em curiosidades "
          + "no momento.")

    acao = escolha(2)
    if acao == 1:
      texto_narrador("Alice: Sabia que existem 3 tipos de hackers? São eles os "
                    + "'White Hat' (chapéu branco), Grey Hat (chapéu cinza) e "
                    + "'Black Hat' (chapéu preto).\nAqueles criminosos que "
                    + "invadem sistemas e roubam dados que vemos muitas vezes "
                    + "em filmes, são os Black Hat, são eles quem combatemos!"
                    + "\nOs 'White Hat', por outro lado, são contratados por "
                    + "empresas e ajudam-nas a descobrir falhas na segurança do "
                    + "seu próprio sistema,\ncomo você está fazendo agora, "
                    + jogador.nome + ". Os Grey Hat ficam entre os dois "
                    + "tipos, eles invadem sistemas sem consentimento da "
                    + "empresa\npara descobrir falhas e pedem dinheiro em troca "
                    + "de mostrarem as falhas que encontraram, mas eles não "
                    + "vazam as falhas\ncaso a empresa se recuse pagar o "
                    + "dinheiro, apenas a omitem. Eles não são tão ruins "
                    + "quanto os Black Hat,\nmas ainda são antiéticos! Ser um "
                    + "hacker não é necessariamente ser um criminoso, existem "
                    + "aqueles que fazem o bem com o conhecimento que têm. "
                    + ":D\n")
      curiosidade += 1
    elif acao == 2:
      texto_narrador("Alice: Poxa, que pena, era uma curiosidade bem "
                    + "interessante. Procure sobre tipos de hackers mais tarde "
                    + "se surgir o interesse!\n")

    espera(3)
    texto_narrador("Aplicativo baixado com sucesso.\n")
    texto_narrador("Alice: Pronto! Estamos com o app aberto, vejo que já temos "
                  + "um cliente esperando nosso atendimento, o senhor Machado "
                  + "de Assisto. Entre no chat dele e dê um oi.\n")
    texto_narrador("Narrador: Você entrou no chat, o cliente começou a digitar "
                  + "logo após a sua mensagem de cumprimento.\n")
    texto_narrador("Machado de Assisto: Bom dia, " + jogador.nome + ". Estou "
                  + "com uma dificuldade em criar minha conta no banco. O "
                  + "aplicativo não aceita a senha que quero usar,\nestá "
                  + "dizendo que a senha não é forte o suficiente. "
                  + "O que seria isso?\n")
    texto_narrador("Alice: Humm... me parece um caso típico de senha simples. "
                  + "Você sabe o que torna uma senha forte?\nPode dar algum "
                  + "exemplo de senha forte para o cliente? Se precisar de "
                  + "alguma dica, pode me chamar!\n")

    while True:
      print(">> 1 - 'MachadoDeAssisto12345'\n>> 2 - '8a5W'\n>> 3 - "
            + "'Mch4do4859@$'\n>> 4 - Pedir ajuda à Alice")
      acao = escolha(4)
      if acao == 1:
        texto_narrador("Alice: Não é uma boa opção de senha. Senhas não devem "
                      + "contar nomes próprios e também não podem ter "
                      + "sequência de números.\nEvite informações que podem "
                      + "ser descobertas em redes sociais, por exemplo nome de "
                      + "animais de estimação ou datas de aniversários.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 2:
        texto_narrador("Alice: Pode ser uma boa senha, mas é muito curta, seria "
                      + "facilmente quebrada por programas de quebra de senha "
                      + "se comparada à senhas maiores.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 3:
        texto_narrador("Alice: Essa é uma ótima senha! Ela faz o uso correto "
                      + "de misturar letras com números e simbolos, além de "
                      + "ter um número ideal de digitos.\n")
        break
      elif acao == 4:
        texto_narrador("Alice: Senhas podem seguir um padrão bem conhecido "
                      + "hoje em dia que dificulta a quebra de senhas por "
                      + "hackers.\nElas devem conter, no mínimo, 8 digitos e "
                      + "misturar letra maiúscula com minúsucla, números e "
                      + "simbolos como '#' ou '@',\nalém de evitar ter "
                      + "informações facilmente obtidas como datas de "
                      + "aniversários e nomes próprios.\n")
        continue

    texto_narrador("Machado de Assisto: Certo, " + jogador.nome + ". Eu "
                  + "entendi o padrão de senhas que devo seguir para minhas "
                  + "contas pessoais. Devo agradecê" + jogador.pronome_conjugal)
    texto_narrador("Alice: Parabéns, agente! Vamos prosseguir com a nossa "
                  + ".\npróxima cliente. A senhora Carolina Maria de Deus está "
                  + "esperando um 'alô' no chat dela.\n")
    texto_narrador("Narrador: A cliente espera você digitar antes de começar "
                  + "o pedido.\n")
    texto_narrador("Carolina Maria de Deus: Bom dia, "
                  + jogador.pronome_tratativo + " " + jogador.nome
                  + "! Estou constantemente recebendo mensagens estranhas e "
                  + "ligações no meu número de telefone de números "
                  + "desconhecidos mas não permiti isso!\nTambém recebo "
                  + "promoções falsas no meu e-mail e todas essas mensagens "
                  + "mostram o parte do meu cpf. Essas informações eu só "
                  + "cadastro em sites que eu acesso,\nestou com medo de ter "
                  + "sido hackeada. Como posso evitar que mais sites tenham "
                  + "acesso aos meus dados assim?\n")
    texto_narrador("Alice: Isso já me aconteceu também, é muito chato! Ela "
                  + "parece ser o tipo de pessoa que passa seus dados em "
                  + "qualquer site que entra,\nmas quem nunca cadastrou o cpf "
                  + "ou e-mail em alguma loja só pra receber um descontinho, "
                  + "não é? hahahah\n")

    while True:
      print(">> 1 - Dizer para ela trocar de número e e-mail.\n>> 2 - "
            + "Aconselhar a cliente a não cadastrar seus dados pessoais em "
            + "sites desconhecidos e de baixa confiança.\n>> 3 - Orientá-la a "
            + "bloquear todos esses contatos desconhecidos para não receber "
            + "mais promoções falsas.\n>> 4 - Pedir alguma dica à Alice")
      acao = escolha(4)
      if acao == 1:
        texto_narrador("Alice: Calma aí, agente " + jogador.nome + ". Isso não "
                      + "vai adiantar se ela continuar cadastrando os novos "
                      + "números e e-mails em outros sites,\nsem falar em o "
                      + "que ela pode fazer com dados que não pode mudar como "
                      + "o próprio RG ou CPF?.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 2:
        texto_narrador("Alice: Isso mesmo. Não é seguro colocar dados pessoais "
                      + "em sites desconhecidos, esses dados podem ser "
                      + "vendidos a terceiros para enviarem spam ao portador"
                      + ".\nEla também pode procurar formas de tirar seus "
                      + "dados de 'Data Brokers', a própria lei da LGPD à "
                      + "ajudaria nisso.\n")
        break
      elif acao == 3:
        texto_narrador("Alice: Não seria viável, levaria muito tempo para "
                      + "bloquear dezenas de contato. Os cibercriminosos "
                      + "também sempre podem criar novos endereços "
                      + "para comunicação.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 4:
        texto_narrador("Alice: São vários os sites que pedem os mais diversos "
                      + "dados pessoais de quem os acessa. Sempre se pergunte "
                      + "se os dados que estão pedindo\nsão realmente "
                      + "relevantes para a sua experiência dentro do site e "
                      + "tome muito cuidado com sites suspeitos aonde você "
                      + "vá se cadastrar!\n")
        continue

    texto_narrador("Carolina Maria de Deus: Entendido, irei tomar mais cuidado "
                  + "com os lugares nos quais digito meus sites pessoais\n")
    texto_narrador("Alice: Muito bem! Essas ligações e e-mails são muito "
                  + "incômodos. Mas, felizmente, temos a lei ao nosso lado "
                  + "para casos assim, basta recorrermos\nà Lei Geral de "
                  + "Proteção de Dados e podemos exigir a eliminação dos "
                  + "nossos dados nesses sites.\nVamos prosseguir ao próximo "
                  + "cliente. O Luís Azevedo já entrou no chat.\n")
    texto_narrador("Luís: Me ajude! Eu estava navegando pelo Instabook quando, "
                  + "entrando nos comentários, vi um link de uma receita de "
                  + "bolo de cenoura que parecia uma delííícia.\nSem pensar "
                  + "duas vezes cliquei no link da receita que me pediu para "
                  + "baixar e executar com programa que me diria a receita "
                  + "que pedi.\nEntretanto, não apareceu receita alguma!! "
                  + "Agora meu celular está muito lento e aparecendo "
                  + "propagandas insuportáveis na minha telaa!!\n")
    texto_narrador("Alice: Me parece que o jeito mais fácil é reverter o "
                  + "celular dele para as configurações de fábrica, mais "
                  + "precisamente formatar, pois foi infectado com um adware."
                  + "\nAlém disto, como poderíamos orientá-lo a não cometer "
                  + "o mesmo erro novamente?\n")

    while True:
      print(">> 1 - Ele não deve clicar em qualquer link desconhecido e não "
            + "deve baixar programas que não conheça.\n>> 2 - Ele pode mandar "
            + "um e-mail para a fabricante do celular dele e pedir que "
            + "reforçem o sistema de segurança do dispositivo.\n>> 3 - Pedir "
            + "ajuda à Alice.")
      acao = escolha(3)
      if acao == 1:
        texto_narrador("Alice: Exato, é necessário prestar muita atenção em "
                      + "links desconhecidos, sites que pedem para baixar "
                      + "outros programas ou pedem para ativar as notificações "
                      + "devem ser tratados com cautela.\n")
        break
      elif acao == 2:
        texto_narrador("Alice: Mas eles já fazem isso frequentemente. Sempre "
                      + "tem atualizações para corrirgir erros no sistema e as "
                      + "empresas como o Instabook já bloqueiam links em "
                      + "comentários.\nMas de nada adianta se o usuário não "
                      + "tiver cuidado e ainda procurar estes links.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 3:
        texto_narrador("Alice: Estas propagandas com certeza vieram do programa "
                      + "que ele baixou neste link suspeito...\n")
        continue

    texto_narrador("Luís: Então foi desse download que vieram essas propagandas "
                  + "invasoras?! Muito obrigado, irei perder todas as minhas "
                  + "músicas baixadas ao formatar meu dispositivo...\nbem, "
                  + "acho que é consequência por ter sido tão descuidado!\n")
    texto_narrador("Alice: Ei, ainda bem que ele pode salvar essas músicas na "
                  + "nuvem ou unidade de armazenamento externa antes de "
                  + "formatar para não perdê-las.\nIsso se chama backup, "
                  + "lembre-se de sempre fazer backup dos seus arquivos "
                  + "importantes.\n")
    espera(3)
    texto_narrador("\n\nNarrador: Você escuta um som de aviso vindo do chat.\n")
    texto_narrador("Ufaaa, já estamos na metade do nosso expediente, vamos "
                  + "tomar um café, " + jogador.nome + "?\n")
    print(">> 1 - Vamos, com certeza!\n>> 2 - Já não via a hora, estou com "
          + "muita fome.\n")

    acao = escolha(2)
    texto_narrador("Narrador: Vocês entram no bate-papo de intervalo onde uma "
                  + "multidão de agentes mandavam mensagens, animados, sobre "
                  + "diversos assuntos\n")
    texto_narrador("Alice: Então, " + jogador.nome + ", quer ouvir mais uma "
                  + "curiosidade sobre nossos casos anteriores enquanto "
                  + "estamos aqui?\n")
    print(">> 1 - Claro, estou bem curios" + jogador.pronome_artigo
          + ".\n>> 2 - Não gosto de conversar "
          + "enquanto faço meu lanche.")

    acao = escolha(2)
    if acao == 1:
      texto_narrador("Alice: Existem diversos tipos de malwares na internet, "
                    + "nosso cliente Luís foi acometido por um desses tipos: o "
                    + "'Adware'.\nAdwares são programas que, quando instalados,"
                    + " infestam o sistema do usuário com avisos, pop-ups e "
                    + "propagandas que geram dinheiro para os hackers Black "
                    + "Hats.\nExistem os 'Trojans', que são como uma caixinha "
                    + "de surpresa em forma de executável, o usuário acredita "
                    + "estar instalando apenas um programa quando,\nna "
                    + "verdade, instala vários outros programas escondidos "
                    + "juntos! E temos os 'Ramsonwares', são programas que "
                    + "fazem o dispositivo de refém,\nbloqueiam e criptografam "
                    + "tudo o que tem no sistema e pedem um pagamento em "
                    + "dinheiro em troca de desbloquear o dispositivo do "
                    + "usuário. Temos outros malwares além desses.\n")
      curiosidade += 1
    elif acao == 2:
      texto_narrador("Alice: Você tem razão. Pode pesquisar por tipos de "
                    + "malwares após nosso expediente hoje para sanar a "
                    + "curiosidade!\n")

    espera(4)

    texto_narrador("\n\nAlice: Pronto, fim da pausa! Olha, já temos mais um "
                  + "cliente precisando de ajuda!\n")
    texto_narrador("José de Aleitura: Boa tarde, me chamo José de Aleitura e "
                  + "preciso de suporte para a minha rede de internet wifi!\n"
                  + "Últimamente a conexão aqui em casa anda muito lenta! "
                  + "Nosso roteador é novo e já verificamos com a provedora "
                  + "sobre os cabos, estão todos normais.\nParece que a "
                  + "conexão fica muito lenta somente durante o dia, não "
                  + "sabemos o porquê pois nunca mexemos nas configurações da "
                  + "rede desde que instalamos aqui em casa. Pode nos "
                  + "ajudar?\n")
    texto_narrador("Alice: Hummm... Somente durante o dia? Deve ser algo "
                  + "relacionado com o uso demasiado da rede. O que você acha, "
                  + jogador.nome + "?\n")

    while True:
      print(">> 1 - Sugerir que ele assine uma internet mais rápida para a "
            + "sua casa.\n>> 2 - Dizer que o problema pode estar nos "
            + "componentes físicos e que seria melhor trocá-los.\n>> 3 - "
            + "Recomendar que troque a senha do wi-fi e desconecte todos os "
            + "dispositivos desconhecidos da rede.\n>> 4 - Perguntar o que a "
            + "Alice pode dizer mais sobre o caso.")
      acao = escolha(4)
      if acao == 1:
        texto_narrador("Alice: Não podemos sugerir algo tão exclusivo assim, "
                      + "querid" + jogador.pronome_artigo + " agente. Nem todos "
                      + "têm a condição de pagar por uma internet mais cara..."
                      + "\nLembre-se, nosso dever é encontrar a melhor solução "
                      + "para cada tipo de cliente focando na inclusão de "
                      + "cada um.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 2:
        texto_narrador("Alice: " + jogador.nome + ", hahaha, o cliente acabou "
                      + "de dizer que verificou o roteador e os cabos, a parte "
                      + "física parece estar em ótimo estado. Deve haver "
                      + "outro motivo nessa lentidão.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 3:
        texto_narrador("Alice: Bem apontado, agente! Toda banda larga tem um "
                      + "limite de taxa de dados que podem transmitir, se a "
                      + "lentidão não vem do meio físico,\ndevem ter muitos "
                      + "dispositivos conectados ao mesmo tempo. Isso ocorre "
                      + "muito quando o cliente assina a internet, não muda a "
                      + "senha do wifi padrão\ne deixa que visitas e amigos "
                      + "conectem-se à rede quando visitam a casa. Logo o "
                      + "bairro todo está usando o wi-fi dele e ele nem "
                      + "imagina hahaha.\n")
        break
      elif acao == 4:
        texto_narrador("Alice: Claro, vou te dizer meu insight disso! Toda "
                      + "banda larga que contratamos tem um limite de download "
                      + "e upload, ou seja,\no limite de dados que podem "
                      + "passar por àquela rede ao mesmo tempo! Quanto mais "
                      + "dispositivos conectados ao mesmo tempo, menos "
                      + "velocidade de conexão fica disponível para cada um.\n")
        continue
    texto_narrador("José de Aleitura: Hummm, então é isso que devo fazer. Irei "
                  + "entrar em contato com a minha provedora, muito "
                  + "obrigado.\n")
    texto_narrador("Alice: Nossa, uma conexão lenta irrita qualquer um, "
                  + "concorda? Agora ele consegue resolver\ne nem entramos no "
                  + "fato de ser muito perigoso pra segurança cibernéticater o "
                  + "roteador de casa com a senha padrão. Bem, vamos ao "
                  + "próximo.\n")

    texto_narrador("Graciliano Panos: Olá, boa noite. Recebi um SMS do meu "
                  + "banco me dizendo que houve uma compra de R$500 reais no "
                  + "meu cartão de crédito e lá tinha um\nlink e um telefone "
                  + "para entrar em contato e resolver por suspeita de fraude. "
                  + "O problema é que essa é a primeira vez que recebo um SMS "
                  + "do banco e estou desconfiado. Como prossigo?\n")
    texto_narrador("Alice: Gente... SMS ainda está sendo usado em 2125?\n")

    while True:
      print(">> 1 - Orientá-lo a acessar o aplicativo do banco e entrar em "
            + "contato com os canais de comunicação oficiais.\n>> 2 - Dizer "
            + "para ligar para o número do SMS, só uma chamada não deve ser "
            + "perigosa.\n>> 3 - Dizer para ignorar SMS e seguir com a vida.\n"
            + ">> 4 - Pedir ajuda à Alice.")
      acao = escolha(4)
      if acao == 1:
        texto_narrador("Alice: Isso mesmo! A única forma segura de verificar "
                      + "essa suposta compra é entrando nos meios oficiais "
                      + "do banco, seja app ou canais de SAQ.\n")
        break
      elif acao == 2:
        texto_narrador("Alice: Não acho uma boa ideia... Mesmo que seja apenas "
                      + "uma ligação, os golpistas são treinados para "
                      + "convencer de que são quem não são.\nE o cliente ainda "
                      + "poderia perder tempo ligando em um número não "
                      + "oficial.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 3:
        texto_narrador("Alice: Hahaha essa é uma resposta muito simples, nós da "
                      + "Secure Shell não agimos assim. Temos que ensinar o "
                      + "cliente a maneira correta de manter sua segurança "
                      + "digital.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 4:
        texto_narrador("Alice: Olha, mandar SMS não é algo natural dos bancos, "
                      + "isso por si só já é digno de suspeita. Geralmente "
                      + "mandam e-mail ou pode ser até ligações diretas.\nMas "
                      + "a segurança garantida está no aplicativo ou site "
                      + "oficial do banco, lá ele pode encontrar os canais de "
                      + "comunicação oficiais.\n")
        continue
    texto_narrador("Graciliano Panos: Então é isso, obrigado. Vou acessar o "
                  + "aplicativo que é mais seguro.\n")

    texto_narrador("Alice: Este caso é de ótimo aprendizado para você também, "
                  + "agente " + jogador.nome + ". Este tipo de golpe se chama "
                  + "'Phishing' e é um dos mais comuns hoje em dia. Quer saber "
                  + "mais?\n")
    print(">> 1 - Sim, me conte!\n>> 2 - Já está ficando tarde, vamos ao "
          + "próximo?")

    acao = escolha(2)
    if acao == 1:
      texto_narrador("Alice: Phishing é quando um golpista se passa por alguma "
                    + "entidade confiável como o banco, empresa ou até alguém "
                    + "do governo!\nEle vai usar de informações fáceis de "
                    + "conseguir como parte do seu cpf, rg ou e-mail para te "
                    + "convencer ser alguém de confiança.\nUm exemplo é uma "
                    + "ligação de alguém dizendo ser do banco e, então, ele "
                    + "diz os últimos dígitos do seu cpf. Após te convencer, "
                    + "ele vai tentar\ntirar de você o máximo de informações "
                    + "possível ou te induzir a acessar algum site falso. "
                    + "Para evitar isso, peça que confirme mais informações "
                    + "que somente\na entidade real teria acesso ou , melhor "
                    + "ainda, apenas desligue e entre em contato direto com os "
                    + "canais oficiais.\n")
      curiosidade += 1
    elif acao == 2:
      texto_narrador("Alice: Está ficando tarde, realmente. Vamos prosseguir.")

    texto_narrador("Vamos começar a conversa com o nosso último cliente\n")
    texto_narrador("Lygia Fatelles: Boa noite, " + jogador.pronome_tratativo
                  +" " + jogador.nome + ". Estava eu passando pelos vídeos do "
                  + "Instabook quando vi uma blogueira que gosto muito\n "
                  + "dizendo sobre uma campanha de natal imperdível! "
                  + "Aparentemente a loja de perfumes Obotitura está "
                  + "oferecendo um perfume muito caro de graça!\nBasta eu "
                  + "entrar no link, preencher o formulários com meus dados e "
                  + "responder um pequeno quiz de 5 perguntas. Vi nos "
                  + "comentários muitas pessoas dizerem que funcionou, será "
                  + "verdade isso?\n")
    texto_narrador("Alice: Mais um caso com o Instabook, hein, você acha que é "
                  + "verdade, " + jogador.nome + "?\n")

    while True:
      print(">> 1 - Dizer que os comentários no post confirmam ser verdade. "
            + "A cliente pode preencher o formulário.\n>> 2 - Apontar que não "
            + "tem perigo ela colocar dados pessoais no formulário apenas para "
            + "testar o quiz.\n>> 3 - Pedir para a cliente confirmar essa "
            + "campanha no site oficial ou nas contas oficias da empresa no "
            + "Instabook.\n>> 4 - Perguntar o mesmo à Alice")
      acao = escolha(4)
      if acao == 1:
        texto_narrador("Alice: Sim, pode fazer sentido. Mas o que nos garante "
                      + "que esses comentários são verdadeiros? Podem ser "
                      + "robôs, IA's\nou até mesmo pessoas reais que foram "
                      + "pagas para comentar e induzir ao erro.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 2:
        texto_narrador("Alice: Lembra do nosso cliente mais cedo, "
                      + jogador.nome + "? Não é seguro espalharmos nossos "
                      + "dados pessoais pela internet,\nmesmo que sejam dados "
                      + "comuns apenas para testar o formulário. Quanto mais "
                      + "o cliente evitar, melhor.\n")
        pontuacao -= 1
        tentativas += 1
        continue
      elif acao == 3:
        texto_narrador("Alice: É realmente a opção mais segura. Essa promoção "
                      + "pode sim ser real, mas o cliente tem que ter certeza "
                      + "disto.\nUma promoção desse tamanho com certeza vai "
                      + "estar nos canais oficiais da empresa.\n")
        break
      elif acao == 4:
        texto_narrador("Alice: Uma promoção imperdível de natal, basta somente "
                      + "cadastrar dados pessoais? Hmmmm... Sabemos que não é "
                      + "recomendável cadastrar mesmo que seja real.\nMas, se "
                      + "a cliente quiser confirmar mesmo assim... Promoções "
                      + "grandes assim serão divulgadas nos meios oficiais da "
                      + "empresa como o próprio site,\nnão basta apenas "
                      + "vídeos de blogueiras.\n")
        continue
    texto_narrador("Lygia Fatelles: Certo! Vou procurar se essas promoções "
                  + "existem no site da empresa e no TikTube, não posso perder "
                  + "meu perfume!\n")
    texto_narrador("Alice: Hahaha, é melhor ela tomar cuidado ou vai voltar "
                  + "aqui novamente dizendo que está recebendo chamadas de "
                  + "números desconhecidos.\n")

    espera(3)
    print("\n\nFIM DE TURNO\n")
    espera(3)
    print("\n\nFIM DE TURNO")

    texto_narrador("Alice: Olha só a hora, passou rápido, não foi? hahaha. "
                  + "Então, " + jogador.nome + ", adorei passar o dia te "
                  + "acompanhando nesses casos.\nNão é bom sentir que está "
                  + "ajudando as pessoas a manterem a sua segurança? Eu amo "
                  + "esse trabalho!\nComo de costume, eu sempre avalio a forma "
                  + "como nossos agentes se saíram no final do dia. Faço isso "
                  + "com base nas tentativas até a resposta correta\ne também "
                  + "avalio o seu valor de curiosidade por se interessar nos "
                  + "tópicos que explico.\nNão se preocupe, minhas dicas não "
                  + "diminuem a potuação.\nVamos ver?\n")

    espera(5)
    print(" \n")

    pontuacao_final(pontuacao, curiosidade, tentativas)

    texto_narrador(avaliacao_f)
    print("\n")
    print("MUITO OBRIGADO POR JOGAR!")
    break

else:
  print("Obrigado por jogar!") #saída do jogo


  #fim do jogo <----------->
