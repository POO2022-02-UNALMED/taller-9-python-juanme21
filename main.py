from tkinter import Tk, Button, Entry, StringVar

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("290x250")
count = 0

## Configuracion de funciones
def btn_click(item):
    global expression
    global count
    if str(item) in ["+", "-", "*", "/"]:
        count += 1
        if count > 1:
            result = str(eval(expression))
            expression = result + item
            input_text.set(expression)
            return

    expression = expression + str(item)
    input_text.set(expression)


def btn_clear():
    global expression
    expression = ""
    input_text.set(expression)


def btn_equal():
    global expression
    global count
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
    count = 0


input_text = StringVar()
expression = ""

# Configuración pantalla de salida
pantalla = Entry(
    root,
    width=22,
    bg="black",
    fg="white",
    borderwidth=0,
    font=("arial", 18, "bold"),
    textvariable=input_text,
)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(
    root,
    text="1",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(1),
).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(
    root,
    text="2",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(2),
).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(
    root,
    text="3",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(3),
).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(
    root,
    text="4",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(4),
).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(
    root,
    text="5",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(5),
).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(
    root,
    text="6",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(6),
).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(
    root,
    text="7",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(7),
).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(
    root,
    text="8",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(8),
).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(
    root,
    text="9",
    width=9,
    height=3,
    bg="white",
    fg="red",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click(9),
).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(
    root,
    text="=",
    width=20,
    height=3,
    bg="red",
    fg="white",
    borderwidth=0,
    cursor=" hand2",
    command=lambda: btn_equal(),
).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(
    root,
    text=".",
    width=9,
    height=3,
    bg="spring green",
    fg="black",
    cursor="hand2",
    borderwidth=0,
    command=lambda: btn_click("."),
).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(
    root,
    text="+",
    width=9,
    height=3,
    bg="deep sky blue",
    fg="black",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click("+"),
).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(
    root,
    text="-",
    width=9,
    height=3,
    bg="deep sky blue",
    fg="black",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click("-"),
).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(
    root,
    text="*",
    width=9,
    height=3,
    bg="deep sky blue",
    fg="black",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click("*"),
).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(
    root,
    text="/",
    width=9,
    height=3,
    bg="deep sky blue",
    fg="black",
    borderwidth=0,
    cursor="hand2",
    command=lambda: btn_click("/"),
).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
