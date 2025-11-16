Se l'uccello supera il bordo del display (superiore o inferiore) il gioco si ferma.

COME?:  
- se la y dell'uccello (uccello_y) è minore di 0 (cioè la y minima del display), l'uccello ha superato il bordo inferiore
- se la y dell'uccello sommato alla sua dimensione (siccome la sua y corrisponde solo al lato superiore del quadrato mentre la dimensione aggiunge anche tutto lo spazio fino al bordo inferiore) è maggiore dell'ALTEZZA (y massima del display),l'uccello ha superato il bordo superiore

RISULTATO:
- il ciclo si ferma e il gioco finisce (in_pausa = True)
