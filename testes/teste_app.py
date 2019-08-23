from unittest import TestCase
from app import ano



class teste_func_bissexto(TestCase):
    def teste_eh_negativo_or_zero(self):
        self.assertTrue(ano > 1,msg='o valor do ano não pode ser negativo ou zero')

    def teste_ano_valido(self):
        self.assertIsInstance(ano,int,msg='o valor do ano precisa ser inteiro.')

