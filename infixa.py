class pilha:
    def __init__(self):  # construtor da classe - executado ao criar um objeto.
        self.dados = []  # criar uma lista para armazenar os dados da pilha

    def push(self, pval):  # inserir pval no topo da pilha
        self.dados.append(pval)  # insere pval no final da lista dados

    def pop(self):  # retira o topo da pilha e retorna
        return self.dados.pop()  # retira o último da lista dados

    def vazia(self):  # verifica se a pilha está vazia e retorna True ou False
        return False if self.dados else True

    def topo(self):  # retorna o topo da pilha (sem retirar)
        return self.dados[-1] # retorna o último valor da lista dados

    def mostrar(self, *args):
        if args:
            print(args[0])
        #for i in range(len(self.dados) - 1, -1, -1):
        #    print(self.dados[i])
        for v in reversed(self.dados):  # percorre a lista dados em ordem inversa
            print(v)


def infixa_posfixa(pinf):
    prior = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    p = pilha()
    pf = ''
    for c in pinf:  
        if c.isalnum():  
             pf += c  
        elif c in {'+', '-', '*', '/'}:
            if p.vazia():
                p.push(c)
            else:
                if prior[c] > prior[p.topo()]:
                    p.push(c)
                else:
                    while not p.vazia():
                        if p.topo() != '(':
                            pf += str(p.pop())
                        else:  
                            break
                    p.push(c)
        elif c == '(':
            p.push(c)
        elif c == ')':
            while  not p.topo() == '(':
                pf += str(p.pop())
            p.pop()
    while not p.vazia():
        pf += p.pop() 
    return pf 



inf = input('Expressão infixa: ')
pos = infixa_posfixa(inf)
print(pos)