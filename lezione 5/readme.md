in_esecuzione = True
in_pausa = False
while in_esecuzione:
  orologio.tick(FPS)
  for evento in pygame.event.get():
      if evento.type == pygame.QUIT:
          in_esecuzione = False
      if evento.type == pygame.KEYDOWN:
          if evento.key == pygame.K_SPACE and not in_pausa:
              velocità_y = salto
          if evento.key == pygame.K_SPACE and in_pausa:
              uccello_y = ALTEZZA // 2
              velocità_y = 0
              lista_muri.clear()
              punteggio = 0
              in_pausa = False
           if not in_pausa:
              velocità_y += gravità
              uccello_y += velocità_y
