from tkinter import * 
mainWindow = Tk()
mainWindow.title("Casita con tkinter (Mini)")

mainWindow.geometry("300x300")


myCanvas = Canvas(mainWindow, bg="lightblue", height="300", width="300")

# Coordenadas 
casa_x_izq = 50
casa_y_arriba = 150
casa_x_der = 250
casa_y_abajo = 250
centro_x = (casa_x_izq + casa_x_der) / 2 # 150

# Fondo (Pasto) 
myCanvas.create_rectangle(
    0, casa_y_abajo, 300, 300, 
    fill="green", outline="green"
)

#  Sol 
sol_radio = 15
sol_x = 30
sol_y = 30
largo_rayo = 25

# Sol
myCanvas.create_oval(
    sol_x - sol_radio, sol_y - sol_radio, 
    sol_x + sol_radio, sol_y + sol_radio, 
    fill="yellow", outline="yellow"
)

#  Nube
myCanvas.create_oval(
    100, 20, 150, 40, 
    fill="white", outline="white"
)

# Casa: Cuerpo Principal 
myCanvas.create_rectangle(
    casa_x_izq, casa_y_arriba, casa_x_der, casa_y_abajo,
    fill="pink", outline="black", width=1
)

#  Casa: Techo 
altura_techo = 50
y_pico = casa_y_arriba - altura_techo
    
puntos_techo = [
    centro_x, y_pico, 
    casa_x_izq - 5, casa_y_arriba, 
    casa_x_der + 5, casa_y_arriba 
]
myCanvas.create_polygon(
    puntos_techo, 
    fill="orange", outline="black", width=1
)


# Ventana 1
v1_x1 = casa_x_izq + 15
v1_y1 = casa_y_arriba + 15
v1_x2 = v1_x1 + 30
v1_y2 = v1_y1 + 20
myCanvas.create_rectangle(v1_x1, v1_y1, v1_x2, v1_y2, fill="white", outline="sienna4", width=1)

# Puerta 
puerta_x = 135
puerta_y1 = casa_y_abajo - 40
puerta_y2 = casa_y_abajo
myCanvas.create_rectangle(
    puerta_x, puerta_y1, puerta_x + 25, puerta_y2,
    fill="sienna4", outline="sienna4", width=1
)
# Manija
myCanvas.create_oval(
    puerta_x + 5, puerta_y1 + 15, 
    puerta_x + 9, puerta_y1 + 19, 
    fill="black", outline="black"
)

myCanvas.pack()

mainWindow.mainloop()