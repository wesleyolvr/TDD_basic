from unittest import TestCase
from app import ano



class teste_func_bissexto(TestCase):
    def teste_eh_negativo(self):
        self.assertTrue(ano==True,msg='o valor do ano não pode ser negativo.')

    def teste_ano_valido(self):
        self.assertIsInstance(ano,int,msg='o valor do ano precisa ser inteiro.')
