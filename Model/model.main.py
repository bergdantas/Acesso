from ast import Num
import cProfile


class Servico():
    
    def __init__ (self, nome, secretaria, qdeVagas, especial):

        self.nome = nome
        self.secretaria = secretaria
        self.qdeVagas = qdeVagas
        self.especial = especial

    def get_especial(self,especial):
        return self.especial

    def set_especial(self, especial):
        self.especial = especial
    
    def get_nome(self,nome):
        return self.nome

    def set_especial(self, nome):
        self.nome = nome
    
    def get_secretaria(self,secretaria):
        return self.secretaria

    def set_secretaria(self, secretaria):
        self.secretaria = secretaria

    def get_qdeVagas(self,qdeVagas):
        return self.qdeVagas

    def set_qdeVagas(self, qdeVagas):
        self.qdeVagas = qdeVagas


class Usuario():
    
    def __init__ (self, nome, cpf, tel, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.senha = senha
    
    def get_nome(self,nome):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_cpf(self,cpf):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_tel(self,tel):
        return self.tel

    def set_tel(self, tel):
        self.tel = tel
    
    def get_email(self,email):
        return self.tel

    def set_email(self, email):
        self.email = email

    def get_senha(self,senha):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

class Endereco(Usuario):

    def __init__ (self, num, rua, bairro, compl):
        self.num = num
        self.rua = rua
        self.bairro = bairro
        self.compl = compl
    
    def get_num(self,num):
        return self.num

    def set_nome(self, num):
        self.num = num
    
    def get_rua(self,rua):
        return self.rua

    def set_rua(self, rua):
        self.rua = rua
    
    def get_bairro(self,bairro):
        return self.bairro

    def set_bairro(self, bairro):
        self.bairro = bairro
    
    def get_compl(self,compl):
        return self.compl

    def set_compl(self, compl):
        self.compl = compl
    
    
class Operador(Usuario):

    def __init__ (self, nome, cpf, tel, email, senha):
        self.nome = nome        
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.senha = senha
    
    def get_nome(self,nome):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_cpf(self,cpf):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_tel(self,tel):
        return self.tel

    def set_tel(self, tel):
        self.tel = tel
    
    def get_email(self,email):
        return self.tel

    def set_email(self, email):
        self.email = email
    
    def get_senha(self,senha):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha


class Administrador(Usuario):
    #O operador possui Cód.ident

    def __init__ (self, nome, cpf, tel, email, senha):
        self.nome = nome        
        self.cpf = cpf
        self.tel = tel
        self.email = email
        self.senha = senha
    
    def get_nome(self,nome):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def get_cpf(self,cpf):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_tel(self,tel):
        return self.tel

    def set_tel(self, tel):
        self.tel = tel
    
    def get_email(self,email):
        return self.tel

    def set_email(self, email):
        self.email = email
    
    def get_senha(self,senha):
        return self.senha

    def set_senha(self, senha):
        self.senha = senha

