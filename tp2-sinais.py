# -*- coding: cp1252 -*-
import matplotlib.pyplot as plt
import numpy as np
from numpy import *


class sinal():
      def __init__(self, inicial, imagem):
                #cria o vetor dominio do ponto inicial até o tamanho
                #do vetor de imagens
                self.dom = array(range(inicial,imagem.size+inicial))
                self.img = imagem
      def __rbt__(self):
                #invertendo o vetor de imagens
                #invertendo apenas a ordem do elementos
                self.img = imagem[::-1]
                #invertendo o vetor de dominio
                #invertendo a ordem e o sinal dos elementos
                self.dom = -self.dom[::-1]
                return sinal(self.dom,self.img)

def main():
      imagem = array([1,2,3,4,5])  
      S = sinal(-3,imagem)
      print S.dom
      print S.img
      S2 = S.rbt(S)
      print S2.dom
      print S2.img
main()

