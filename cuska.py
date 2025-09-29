from tkinter import Canvas, Tk #GUI bibliotēka TK Inter

class Game:
    def __init__(self, canvas):
        self.canvas = canvas #veidojām konstruktora argumentu, kuru varēsim izmantot kā parametru turpmāk, šīs arguments ir tas pats canvas
        pass

root = Tk() #izveidojām objektu, kas ir lodziņš
root.title("* * * Č Ū S K A * * *")
canvas = Canvas(root, width=300, height=300, bg="black")
canvas.pack() #izvēlāmies ģeometrijas pārvaldienku, var ņemt: pack, place, grid
game = Game(canvas)
root.mainloop() #lai lodziņš nepazustu, lai visu laiku ir vaļā