# -*- coding: cp1252 -*-
import matplotlib.pyplot as plt
from numpy import *
import numpy as np

def convolui(x,H):
      X = x.rbt()
      pronto = X.dslc(abs(X.dom[-1]-H.dom[0]))
      dom = pronto.dom[-1]
      # n é o tamanho do vetor final
      n = H.dom[-1] - pronto.dom[0] +1
      #apesar dos elementos do dominio de y não serem zeros
      #eles não irão influenciar pois serão substituidos
      img = array([0]*n)
      #aux será o marcador das posições em que os elementos serão
      #guardados na imagem
      aux = 0       
      while aux < n:
        for t in range(len(pronto.dom)):
            for s in range(len(H.dom)):
                if (H.dom[s] == pronto.dom[t]):
                    img[aux] = img[aux] + (pronto.img[t] * H.img[s])
        pronto.dslc(-1)
        aux += 1
      return sinal(dom,img)
      
class sinal():
      def __init__(self, inicial, imagem):
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
            #deslocamento serÃ¡ feito da forma x(n - n0)
            #self.dom[-1] Ã© o ultimo elemento do vetor
            self.dom = array(range(self.dom[0]-n0, self.dom[-1]-n0+1))
            return sinal(self.dom[0],self.img)

      def plot(self,cor):
            plt.plot(self.dom,self.img,cor)
		
      def show(self):
            print 'dominio: {}'. format (self.dom)
            print 'imagem: {}'.  format (self.img)
            
      def size(self):
            return len(self.dom)


def main():
      img1 = array ([3,4,2,1,5,5,6,7,8,9,6,1,3,4,5,6,2,7,])
      img2 = array([-1,-3,-1,-20,0,0,-4,0,2,4,5])
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
