# import test
from utils import DynamicGraph
################
# velocità media
# v = X - Xo / t - to
################
################
# accellerazione
# a = V - Vo / t - to

# abbiamo un oggetto lanciato da un dirupo di 50m di profondità ad una velocità di 15 m/s
# voglio visualizzare lo spostamento dell'oggetto (Y) in funzione del tempo
def object_thrown_by_cliff_1():
    v0 = 15           # Velocità iniziale (m/s)
    a = -9.80         # Accelerazione gravitazionale (m/s^2)
    y0 = 0            # Posizione iniziale (m)
    max_depth = -50   # Depth of the cliff (m)

    # Crea grafico
    graph = DynamicGraph(xlim=(-10, 10), ylim=(-50, 50), title="Object Thrown from a Cliff")

    # simula movimento fino a quando la palla raggiunge la fine del dirupo (-50m)
    time = 0
    while True:
        y = y0 + v0 * time + (1/2) * a * time**2  # formula posizione
        graph.add_point(time, y)
        print(round(time,3),y)

        # ferma se l'oggetto raggiunge la fine del dirupo.
        if y <= max_depth:
            print(f"The object has reached the bottom of the cliff at t = {time} seconds.")
            break
        
        time += 0.1  # Incremento tempo (+1.0s)

    print('tempo che sta in aria:',round(time,3),'s') # tempo impiegato dal moto
    graph.close()


object_thrown_by_cliff_1()

