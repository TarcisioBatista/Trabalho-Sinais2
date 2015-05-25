# -*- coding: cp1252 -*-
from numpy import *
import matplotlib.pyplot as plt

def convolui(x,h):
    #n0 é o deslocamento
    n0 = x.dom[-1] - h.dom[0]
    
    #aqui utilizo o primeiro elemento do vetor x.dom[0] pois ele não está
        #rebatido se estivesse teria que utilizar o ultimo x.dom[-1]
            #e o desloco de n0
    #inicial é o primeiro elemento do dominio de x
        #apos ser deslocado e rebatido
    inicial = x.dom[0] - n0
    # n é o tamanho de y que é o inicial menos o ultimo 
        # elemento do vetor que nao foi deslocado
    n = abs(inicial - h.dom[-1]) +1
    #criando e inicializando o vetor de saida com zeros
    imagemY = array([0]*n)
    i = 0
    #aqui é a parte principal da convolução e não é utilizado nada do dominio
        #baseado na função 'convolve' reparei q nã ha necessidade de utilizar o dominio
            #dentro da convolução, esse metodo foi descoberto quando fiz uma convoluçao
                #manual e coloquei o produto dos index e reparei o que acontecia a partir dai
                    #criei o algoritmo, 
    while i < len(x.img):
        aux = i
        for j in h.img:
            imagemY[aux] += x.img[i]*j
            aux+=1
        i+=1
    return sinal(inicial,imagemY)      


class sinal():
	def __init__(self, inicial, imagem):
        #cria um array para o dominio com origem no variavel inicial
            #e fim na soma entre o valor incial e a quantidade
                #de elementos do vetor imagem
		self.dom = array(range(inicial,imagem.size+inicial))
		self.img = imagem      
	def show(self):
		print 'dominio: {}'. format (self.dom)
		print 'imagem: {}'.  format (self.img)
	def plot(self,cor):
		plt.plot(self.dom,self.img,cor)
		plt.show()
	def escala(self):
		return [min(self.dom)-1,max(self.dom)+1,min(self.img)-1,max(self.img)+1]
	#escala retorna um vetor com os maximos e minimos
	    #(min(dom)-1,max(dom)+1,min(img)-1,max(img)+1)
		#para dar uma escala melhor ao grafico
            

def main():
    img1 = array([2,4,6,7,8,9,3,4,2,1])
    img2 = array([1,0,5,6,7,8,9,0,2])
    S = sinal(-1,img1)
    P = sinal(-5,img2)
    T = convolui(S,P)
    plt.grid(1)
    S.plot('go')
    plt.show()
    plt.grid(1)
    P.plot('ro')
    plt.show()
    plt.grid(1)
    T.plot('bo')
    plt.title('Covolui')
    plt.xlabel('dominio')
    plt.ylabel('imagem')
    plt.show()
    
main()
