#PARTE 1
LARGHEZZA_MURO = 60
SPAZIO_VUOTO = 150
velocità_muri = 3
lista_muri = []
 
def crea_muro():
    altezza_superiore = random.randint(100, 300)
    x = LARGHEZZA + 100
    return [x, altezza_superiore]
# Timer per generare muri ogni tot tempo
    AGGIUNGI_MURO = pygame.USEREVENT + 1
    pygame.time.set_timer(AGGIUNGI_MURO, 1500)
 
#PARTE 2
while in_esecuzione:
    for evento in pygame.event.get():
        if evento.type == AGGIUNGI_MURO and not in_pausa:
            lista_muri.append(crea_muro())

if not in_pausa:
# Movimento muri
    for muro in lista_muri:
        muro[0] -= velocità_muri
# Rimuovi muri fuori dallo schermo
        lista_muri = [m for m in lista_muri if m[0] + LARGHEZZA_MURO > 0]

