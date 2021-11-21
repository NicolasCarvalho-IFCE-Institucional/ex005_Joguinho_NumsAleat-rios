#importanto bibliotecas
import pygame
from random import choice
from time import sleep
import sys


#carregando cor e fonte do texto do placar
cortexto = (79,47,79)

pygame.font.init()
fonte_padrao = pygame.font.get_default_font()
fonte = pygame.font.Font(fonte_padrao, 30)

#posições do placar
POplacar_usuario = (140, 70)
POplacar_castor = (465, 70)


#fundo do jogo
imagem_fundo = pygame.image.load('imagens/jogofundo2.png')
imagem_venceu = pygame.image.load('imagens/venceu_img.png')
imagem_perdeu = pygame.image.load('imagens/perdeu_img.png')

#personagem do jogo
imagem_castor = pygame.image.load('imagens/jogador.png')


#definindo a largura e altura
largura = 580
altura = 640


#instanciando o display
tela = pygame.display

#inciando o pygame e tela
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('sons/fundo.wav')
pygame.mixer.music.play(-1)
tela.init()


#configurando opções da tela
dimensoes = tela.set_mode((largura, altura))
tela.set_caption('Beto, o castor')
argumentos_secundarios = None


#jogadas possíveis
jogadas_possiveis = {'49': (80, 210),
                    '50': (400, 210),
                    '51': (80, 345),
                    '52': (400,345),
                    '53': (80, 480),
                    '54': (400,480),}


#definindo posicoes iniciais
jogada_do_usuario = (None, None)
jogada_do_castor = (None, None)


#definindo jogabilidade
tempo_de_espera = 2
cont = 0

pontos_do_usuario = 0
pontos_do_castor = 0

taxa_minima_de_espera = 1
taxa_de_decrescimo = 0.25

diferenca_ganhadora = 25

tentativa_jogador = False




def ColocarTexto(texto, fonte, janela, dimensao, cortexto):
 objTexto = fonte.render(texto, True, cortexto)
 rectTexto = objTexto.get_rect()
 rectTexto.topleft = dimensao
 janela.blit(objTexto, rectTexto)




#loop principal do jogo
while True:

  #posicionando o fundo
  dimensoes.blit(imagem_fundo, (0,0))


  #atualizando a tela (escondendo o castor)
  tela.update()
  
  ColocarTexto(str(pontos_do_usuario), fonte, dimensoes, POplacar_usuario, cortexto)
  ColocarTexto(str(pontos_do_castor), fonte, dimensoes, POplacar_castor, cortexto)

  #tempo de espera do castor dentro da toca
  sleep(tempo_de_espera)  


  #sorteando e posicionando o castor
  jogada_do_castor = jogadas_possiveis[choice(list(jogadas_possiveis))]

  dimensoes.blit(imagem_castor, jogada_do_castor)


  #atualizando a tela (aparecendo o castor)
  tela.update()




  #analisando as entras do usuário
    #verificando se alguma tecla do teclado foi pressionada
  for i in range(1, int(tempo_de_espera*1000 + 1)):

    for evento in pygame.event.get():

      #verificando evento de saída do jogo
      if evento.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      #verificando se alguma tecla foi prescionada
      if evento.type == pygame.KEYDOWN:

        #verificando possibilidades de jogadas
        for jogada_possivel in jogadas_possiveis:

          #verificando se a tecla pressionada está no conjunto de tecla possíveis
          if evento.key == int(jogada_possivel):
            jogada_do_usuario = jogadas_possiveis[jogada_possivel]

            #verificando se a posição do usuário é a mesma do castor
            if jogada_do_usuario == jogada_do_castor:
              pontos_do_usuario += 1
              tentativa_jogador = True
              print('ACERTOU')
            else:
              pontos_do_castor += 1
              tentativa_jogador = True
              print('ERROU')

            bonk = pygame.mixer.Sound('sons/pompom.wav')
            bonk.play()

          #se nada ocorrer, continua o jogo
          else:
            pass

      #se nada ocorrer, continua o jogo
      else:
        pass

      #verifica se já houve uma tentativa
      if tentativa_jogador == True:
        break
      else:
        pass

    #verifica se já houve uma tentativa
    if tentativa_jogador == True:
      break
    else:
      pass

    #espera um milésimo de segundo para analisar o teclado de novo
    sleep(tempo_de_espera/1000)




  #se o jogador não jogou, o castor pontua
  if tentativa_jogador == False:
    pontos_do_castor += 1
  else:
    pass


  #atualizando dados para a próxima jogada
  cont = 0
  tentativa_jogador = False
  

  #atualizando velocidade de aparececimento e desaparecimento do castor 
  if tempo_de_espera != taxa_minima_de_espera: 
    if pontos_do_usuario % 6 == 0:
      tempo_de_espera -= taxa_de_decrescimo
    else:
      pass
  else:
    pass


  #exibindo placar no terminal
  print('JOGADOR: {} x CASTOR: {}'.format(pontos_do_usuario, pontos_do_castor))


  #calculando diferença dos pontos
  diferenca_de_pontos = pontos_do_usuario - pontos_do_castor


  #verificando se já existe um vencedor
  if diferenca_de_pontos == diferenca_ganhadora:
    print('PARABÉNS, VOCÊ GANHOU !!')
    dimensoes.blit(imagem_venceu, (0,0))
    tela.update()
    sleep(3)
    break
  elif diferenca_de_pontos == ( diferenca_ganhadora * -1 ):
    print('PUXA, VOCÊ PERDEU. TENTE OUTRA VEZ !!')
    dimensoes.blit(imagem_perdeu, (0,0))
    tela.update()
    sleep(3)
    break
  else:
    pass