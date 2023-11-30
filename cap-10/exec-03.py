##############################################################################
# Author: Fabio Araujo
# Date:
# Objective: exercicios3\capitulo 10\exercicio-10-03.py
##############################################################################


class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.caanal = self.cmin

tv = Televisao(2, 10)
tv.muda_canal_para_cima()
print(tv.canal)
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

