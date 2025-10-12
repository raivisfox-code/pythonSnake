from random import randint
from tkinter import Canvas, Tk  # GUI bibliotēka TK Inter


class Game:
    def __init__(self, canvas):
        self.canvas = canvas  # veidojām konstruktora argumentu, kuru varēsim izmantot kā parametru turpmāk, šīs arguments ir tas pats canvas
        self.apple_coords = [randint(0, 29) for i in range(2)]
        # definējām masīvu, kas dināmiskais masīvs
        self.snake_coords = [[14, 14]]
        self.vector = {"Up": (0, -1), "Down": (0, 1),
                       "Left": (-1, 0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()  # lai varētu uztvert taustiņu nospiešanu
        self.canvas.bind("<Key_Press>", )  # saista notikumu ar funkciju

        self.Game()

    def new_method(self):
        return self.set_direction


def set_direction(self, event):  # funkcija, kas maina kustības virzienu
    if event.keysym in self.vector:
        self.direction = self.vector[event.keysym]


def draw(self):  # objektu zīmēšana
    self.canvas.delete("all")  # izdzēš visu, kas ir uz ekrāna
    x_apple, y_apple = self.apple_coords
    self.canvas.create_rectangle(
        x_apple*10, y_apple*10, (x_apple+1)*10, (y_apple+1)*10,
        fill="red", width=0
    )
    for x, y in self.snake_coords:
        self.canvas.create_rectangle(
            x*10, y*10, (x+1)*10, (y+1)*10, fill="green", width=0
        )

    def GAME(self):  # spēles loģika būs šeit
        self.draw()
        x, y = self.snake_coords[0]
        x += self.direction[0]
        y += self.direction[1]
        self.snake_coords.insert(0, [x, y])
        self.canvas.after(100, self.GAME)


root = Tk()  # izveidojām objektu, kas ir lodziņš
root.title("* * * Č Ū S K A * * *")
canvas = Canvas(root, width=300, height=300, bg="orange")
canvas.pack()  # izvēlāmies ģeometrijas pārvaldienku, var ņemt: pack, place, grid
game = Game(canvas)
root.mainloop()  # lai lodziņš nepazustu, lai visu laiku ir vaļā
