from tkinter import Canvas, Tk #GUI bibliotēka TK Inter

root = Tk() #izveidojām objektu, kas ir lodziņš
root.title("* * * Č Ū S K A * * *")
canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

root.mainloop() #lai lodziņš nepazustu, lai visu laiku ir vaļā