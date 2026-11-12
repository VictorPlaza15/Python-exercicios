'Programa que toque um arquivo mp3'

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Agora você escuta a música, para finalizar o programa, aperte enter!')