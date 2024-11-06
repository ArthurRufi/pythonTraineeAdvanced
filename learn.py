import tkinter

lista1 = [1, 3, 6, 9, 12]
lista2 = [7, 2, 3, 10, 31]

compreensio = [(x) for x in lista1 for y in lista2 if x > y]
print (compreensio)