##############################################################################
# Author: Fabio Araujo
# Date:
# Objective: exercicios3\capitulo 10\exercicio-10-01.py
##############################################################################


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = '20'
        self.marca = 'Semp'
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv_sala = Televisao()
tv_sala.ligada = False
tv_sala.canal = 4
tv_sala.tamanho = '20'
tv_sala.marca = 'Samsung'

tv_quarto = Televisao()
tv_quarto.ligada = False
tv_quarto.canal = 5
tv_quarto.tamanho = '24'
tv_quarto.marca = 'LG'

tv = Televisao()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
print(f"O canal da tv é: {tv.canal}")

tv.muda_canal_para_baixo()
print(f"O canal da tv é: {tv.canal}")

