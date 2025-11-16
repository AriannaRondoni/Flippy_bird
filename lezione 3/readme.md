Definizione, Creazione e Animazione

la parte 1 di questa lezione, definisce le caratteristiche statiche e il meccanismo di generazione degli ostacoli:
- Vengono impostati parametri chiave come la larghezza dei muri (LARGHEZZA_MURO), la dimensione dello spazio libero attraverso cui l'uccello deve passare (SPAZIO_VUOTO) 
e la velocità di scorrimento orizzontale (velocità_muri).
- Viene introdotta la Funzione di Creazione (crea_muro): Questa funzione calcola in modo casuale l'altezza del tubo superiore 
e restituisce una lista che rappresenta la posizione iniziale del nuovo muro (fuori dal lato destro dello schermo).
- Viene configurato un timer di Pygame (pygame.time.set_timer) che attiva un evento personalizzato (AGGIUNGI_MURO) ogni 1,5 secondi.
Questo garantisce che un nuovo ostacolo venga generato a intervalli regolari

La parte 2, invece, implementa la logica dinamica all'interno del ciclo principale del gioco:
- Quando l'evento AGGIUNGI_MURO viene rilevato (grazie al timer impostato nella Lezione 3) e il gioco non è in pausa, un nuovo muro viene creato dalla funzione crea_muro() 
e aggiunto alla lista degli ostacoli attivi (lista_muri).
- Per simulare lo scorrimento del paesaggio (che dà l'illusione che l'uccello stia volando in avanti), 
ogni muro nella lista_muri viene spostato verso sinistra decrementando la sua coordinata X della velocità_muri in ogni frame.
- Il codice include un'operazione di pulizia (list comprehension) che rimuove dalla lista tutti i muri che sono usciti completamente dal lato sinistro dello schermo.
Questo è fondamentale per mantenere efficiente il gioco, evitando di elaborare e disegnare ostacoli che non sono più visibili.
