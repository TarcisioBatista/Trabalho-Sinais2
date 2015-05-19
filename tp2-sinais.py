# -*- coding: cp1252 -*-
#import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def convolui(sinal1,sinal2):
      rebatido1 = sinal1.rbt()
      #rebatido e deslocado as ready
      #rebatido.dom[-1] é o ultimo elemento do vetor
      ready = rebatido1.dslc(rebatido1.dom[-1]-sinal2.dom[0])
      ready.show()
      sinal2.show()
      Y = sinal(0,0)
      aux = 0
      for s,t in zip(ready.dom,ready.img):
            for j in sinal2.img:
                  if (s==i):
                        #aqui pegamos o ultimo elemento do dominio do vetor que esta sendo deslocado,
                        #ele será substituido algumas veses mas no final ficará sempre na posição correta
                        if (Y.dom[0]==0):
                              Y.dom[0] = ready.dom[-1]
                              Y.img[0]= Y.img[0] + (t * j)
                              ready.dslc(-1)
                              aux = aux + 1
                        else:
                              Y.dom[aux] = Y.dom[aux-1]+1
                              Y.img[aux]= Y.img[aux] + (t * j)
                              ready.dslc(-1)
                              aux++
      
class sinal():
      def __init__(self, inicial, imagem):
            #cria o vetor dominio do ponto inicial até o tamanho
            #do vetor de imagens
            self.dom = array(range(inicial,imagem.size+inicial))
            self.img = imagem            
            
      def rbt(self):
            #invertendo o vetor de imagens
            #invertendo apenas a ordem do elementos
            self.img = self.img[::-1]
            #invertendo o vetor de dominio
            #invertendo a ordem e o sinal dos elementos
            self.dom = -self.dom[::-1]
            return sinal(self.dom[0],self.img)
      
      def dslc(self, n0):
            #deslocamento será feito da forma x(n - n0)
            #self.dom[-1] é o ultimo elemento do vetor
            self.dom = array(range(self.dom[0]-n0, self.dom[-1]-n0+1))
            return sinal(self.dom[0],self.img)
      
      def show(self):
            print 'dominio: {}'. format (self.dom)
            print 'imagem: {}'.  format (self.img)

def main():
      img1 = array ([3,4,2,1])
      img2 = array([1,0,2])
      P = sinal(-1,img1)
      S = sinal(-3,img2)
##      for i in range(len(P.dom)):
##            print '{} {}'. format(i,P.dom[i])
      for t,s in zip(P.dom,P.img):
            print '{} {}'. format(t,s)
      #convolui(P,S)     
      #print np.convolve (img1,img2)
main()
