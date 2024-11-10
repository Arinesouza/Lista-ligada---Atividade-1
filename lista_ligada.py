class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo

    def get_valor(self):
        return self.valor


class LinkedList: 
    def __init__(self):
        self.inicio = None

    def processar_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as f:
                print(f"Lendo o arquivo: {arquivo}")

                # Primeira linha: elementos iniciais da lista
                elementos_iniciais = list(map(int, f.readline().strip().split()))
                print(f"Elementos iniciais: {elementos_iniciais}")
                for valor in elementos_iniciais:
                    self.inserir_fim(valor)

                # Segunda linha: número de ações
                num_acoes = int(f.readline().strip())
                print(f"Número de ações: {num_acoes}")

                for _ in range(num_acoes):
                    acao = f.readline().strip().split()
                    tipo_acao = acao[0]

                    if tipo_acao == 'A':  # Adicionar
                        valor = int(acao[1])
                        posicao = int(acao[2]) if len(acao) > 2 else None
                        print(f"Ação: Adicionar o elemento {valor} na posição {posicao}")
                        if posicao is not None:
                            self.inserir_posicao(valor, posicao)
                        else:
                            self.inserir_fim(valor)
                    
                    elif tipo_acao == 'R':  # Remover
                        valor = int(acao[1])
                        print(f"Ação: Remover o primeiro elemento com valor {valor}")
                        self.remove(valor)
                    
                    elif tipo_acao == 'P':  # Imprimir
                        print("Ação: Imprimir a lista")
                        self.imprimir_lista()

        except FileNotFoundError:
            print(f"Erro: O arquivo {arquivo} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {arquivo}: {e}")

    def inserir_fim(self, valor):
        novo_no = No(valor)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novo_no)

    def inserir_posicao(self, valor, posicao):
        novo_no = No(valor)
        if posicao == 0 or self.inicio is None:
            novo_no.set_proximo(self.inicio)
            self.inicio = novo_no
        else:
            aux = self.inicio
            anterior = None
            atual_posicao = 0

            while aux is not None and atual_posicao < posicao:
                anterior = aux
                aux = aux.get_proximo()
                atual_posicao += 1

            novo_no.set_proximo(aux)
            if anterior is not None:
                anterior.set_proximo(novo_no)
                
    def remove(self, valor):
        if self.inicio is None:
            print("Lista vazia.")
            return

        if self.inicio.get_valor() == valor:
            self.inicio = self.inicio.get_proximo() 
            print(f"Elemento {valor} removido.")
            return

        atual = self.inicio
        while atual.get_proximo() is not None:
            if atual.get_proximo().get_valor() == valor:
                atual.set_proximo(atual.get_proximo().get_proximo())  
                return
            atual = atual.get_proximo()

        print(f"Elemento {valor} não encontrado.")

        
    def imprimir_lista(self):
        aux = self.inicio
        if not aux:
            print("Lista vazia.")
        while aux is not None:
            print(aux.get_valor(), end=" ")
            aux = aux.get_proximo()
        print()

    def executar_acoes(self):
        self.processar_arquivo('arq.txt')
        self.processar_arquivo('arq2.txt')

lista = LinkedList()
lista.executar_acoes()