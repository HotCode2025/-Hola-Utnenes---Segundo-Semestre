# De una tupla, crear lista con números < 5
t = (1, 7, 3, 9, 2, 6, 0, 5, 4)
menores = [n for n in t if n < 5]
print("Tupla:", t)
print("Menores a 5:", menores)
