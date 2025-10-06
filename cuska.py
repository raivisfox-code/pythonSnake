from random import randint
from tkinter import Canvas, Tk #GUI bibliotēka TK Inter

class Game:
    def __init__(self, canvas):
        self.canvas = canvas #veidojām konstruktora argumentu, kuru varēsim izmantot kā parametru turpmāk, šīs arguments ir tas pats canvas
        self.apple_coords = [randint(0, 29) for i in range(2)]
        
        self.GAME()

    def draw(self):
        x_apple, y_apple = self.apple_coords
        print(x_apple)
        self.canvas.create_rectangle(x_apple*10, y_apple*10, (x_apple+1)*10, (y_apple+1)*10, fill = "red", width = 0)

    def GAME(self):
        self.draw()

root = Tk() #izveidojām objektu, kas ir lodziņš
root.title("* * * Č Ū S K A * * *")
canvas = Canvas(root, width=300, height=300, bg="orange")
canvas.pack() #izvēlāmies ģeometrijas pārvaldienku, var ņemt: pack, place, grid
game = Game(canvas)
root.mainloop() #lai lodziņš nepazustu, lai visu laiku ir vaļā