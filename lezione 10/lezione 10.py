for muro in lista_muri:
    x = muro[0]
    altezza = muro[1]
    pygame.draw.rect(finestra, VERDE, (x, 0, LARGHEZZA_MURO, altezza))
    pygame.draw.rect(finestra, VERDE, (x, altezza + SPAZIO_VUOTO, LARGHEZZA_MURO, ALTEZZA - (altezza + SPAZIO_VUOTO)))