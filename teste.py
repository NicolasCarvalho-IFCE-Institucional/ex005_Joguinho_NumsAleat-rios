import pygame

pygame.init()

while True:
  events = pygame.event.get()

  print('foi')
  for event in events:
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              print('e')
          if event.key == pygame.K_RIGHT:
              print('d')