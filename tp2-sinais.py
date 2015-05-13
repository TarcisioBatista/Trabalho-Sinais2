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
      img1 = array ([4,0,3])
      img2 = array([2,0,1,3])
      S = sinal(-1,img1)
      P = sinal(-3,img2)
      convolui(P,S)
      Y = sinal(0,0)
      for i in S.dom:
            for j in P.dom:
                  if j == i:
                    Y.dom.append = i # ou j
                    Y.img.index(S.dom.index(i)) = Y.img.index(S.dom.index(i)) + S.img[S.dom.index(i)]*P.img[P.dom.index(i)] 
            
      #print np.convolve (img1,img2)
main()
