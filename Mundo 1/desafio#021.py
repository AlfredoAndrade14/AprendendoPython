# Importando o PyGame
import pygame
import os

# Inicializando o PyGame
pygame.mixer.init()
pygame.init()

print("O NOME DA MUSCIA NÃO PODE TER ESPAÇOS E LETRAS MAIÚSCULAS")
print("O ARQUIVO DA MUSICA TEM QUE ESTAR NO MESMO CAMINHO DO ARQUIVO PYTHON")
print("##########################\n")
nome = input("DIGITE O NOME DA MUSICA COM A EXTENSÃO: ")
volume = float(input("DIGITE O VOLUME DA MÚSICA DE ENTRE 0 E 1.0: "))
# Carregando o arquivo MP3 e executando
if os.path.exists(nome):
    pygame.mixer.music.load(nome)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')
