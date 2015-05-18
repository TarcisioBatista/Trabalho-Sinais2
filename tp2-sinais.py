# -*- coding: cp1252 -*-
#import matplotlib.pyplot as plt
from numpy import *

#def convolui(sinal1,sinal2):
      


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
            self.dom = array(range(self.dom[0]-n0, self.dom[self.dom.size-1]-n0+1))
            return self.dom

def main():
      imagem = array([1,2,3,4,5])
      S = sinal(-3,imagem)
      S2 = S.rbt()
      print S2.dom
      print S2.dslc(-1)
main()
