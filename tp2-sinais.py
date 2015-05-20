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
      aux = 0
      auxD = ready.dom[-1]
      Y = sinal([],[])
      for s in range(len(ready.dom)):
            for t in range(len(sinal2.dom)):
                  if (ready.dom[s]==sinal2.dom[t]):
                        #aqui pegamos o ultimo elemento do dominio do vetor que esta sendo deslocado,
                        #ele será substituido algumas veses mas no final ficará sempre na posição correta
                        #print '{} {}'.format(aux,auxD)
                        Y.dom[aux] = auxD
                        print Y.img[aux]
                        Y.img[aux]= Y.img[aux] + ((ready.img[s] * sinal2.img[t]))
                        print '    {}'. format(Y.img[aux]) 
                        ready.dslc(-1)
                        aux += 1
                        auxD += 1
            s = t = 0
      return Y
      
class sinal():
      def __init__(self, inicial, imagem):
            if inicial == []:
                  #criando vetor de zeros pois com a função np.zeros
                  #estava tendo um comportamento anomalo
                  self.dom = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                  self.img = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            #cria o vetor dominio do ponto inicial até o tamanho
            #do vetor de imagens
            else:
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
      P = sinal(-3,img1)
      S = sinal(-1,img2)
      S.show()
      P.show()
      convolui(P,S)

main()
