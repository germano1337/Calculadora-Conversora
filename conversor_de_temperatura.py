import tkinter as tk

calculadora = tk.Tk()

def botaoConverterClicado():
    if temperaturaCelsius.get() != "":
        C = float(temperaturaCelsius.get())
        F = (C * 9 / 5) + 32
        temperaturaFahrenheit.set(F)
    if  temperaturaFahrenheit.get() != "":
        F = float(temperaturaFahrenheit.get())
        C = (F - 32 ) * 5 / 9
        temperaturaCelsius.set(C)

def botaoSairClicado():
    calculadora.quit()        
        
temperaturaCelsius = tk.StringVar()
temperaturaFahrenheit = tk.StringVar()

rotuloCelsius = tk.Label(text="Temperatura Celsius: ", width= 25 , anchor=tk.W)
textoCelsius = tk.Entry(textvariable = temperaturaCelsius)
rotuloFahrenheit = tk.Label(text="Temperatura Fahrenheit: ", width= 25 , anchor=tk.W)
textoFahrenheit = tk.Entry(textvariable = temperaturaFahrenheit)

botaoConverter = tk.Button(calculadora, text="Converter", command= botaoConverterClicado)
botaoSair= tk.Button(calculadora, text="Sair", command=botaoSairClicado)

rotuloCelsius.grid(row = 0, column =0)
textoCelsius.grid(row = 0, column=1)
rotuloFahrenheit.grid(row = 1, column=0)    
textoFahrenheit.grid(row = 1, column=1)

botaoConverter.grid(row = 2, column=0, columnspan=2)   
botaoSair.grid(row= 3, column = 0, columnspan= 3)


calculadora.mainloop()          