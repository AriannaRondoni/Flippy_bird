MOVIMENTO CONTINUO ED ARRESTO:
- in_esecuzione = True: mantiene attivo il ciclo principale
- in_pausa = False: il gioco è subito attivo
- evento.type == pygame.QUIT: se si clicca la "X" della finestra, il ciclo si ferma e il gioco termina
- quando viene premuta la barra spaziatrice ("pygame.K_SPACE") e il ciclo non è in pausa ("and not in_pausa") l'uccello salta
- quando viene premuta la barra spaziatrice e il ciclo è in pausa ("and in_pausa"), si sta cliccando non per saltare ma per ricominciare una nuova partita
  - uccello_y = ALTEZZA // 2: rimette l'uccello al centro del display
  - si arresta tutto (tutte le variabili sono riportate a 0) per ricominciare una nuova partita

MOVIMENTO CONTINUO:
- velocità_y += gravità: la gravità aumenta la velocità dell'uccello verso il basso
- uccello_y += velocità_y: la nuova velocità è applicata alla posizione y dell'uccello 
