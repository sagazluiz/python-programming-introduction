##############################################################################
# Author: Fabio Araujo
# Date:
# Objective: exercicios3\capitulo 10\exercicio-10-01.py
##############################################################################


class Televisao:
    def __init__(self, canal_inicial, min, max):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max
#        self.tamanho = '20'
#        self.marca = 'Semp'
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = Televisao(5, 1, 99)
for x in range(0, 120):
    tv.muda_canal_para_cima()
print(tv.canal)

for x in range(0, 120):
    tv.muda_canal_para_baixo()
print(tv.canal)




#tv_sala.ligada = False
#tv_sala.canal = 4
#tv_sala.tamanho = '20'
#tv_sala.marca = 'Samsung'

#tv_quarto = Televisao()
#tv_quarto.ligada = False
#tv_quarto.canal = 5
#tv_quarto.tamanho = '24'
#tv_quarto.marca = 'LG'

#tv = Televisao()
#tv.muda_canal_para_cima()
#tv.muda_canal_para_cima()
#print(f"O canal da tv é: {tv.canal}")

#tv.muda_canal_para_baixo()
#print(f"O canal da tv é: {tv.canal}")

