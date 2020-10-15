"""
1 tabela com 9 espaços origina 9 tabelas com 8 espaços
9 tabelas com 8 espaços originam (9x8) tabelas com 7 espaços
9x8 tabelas com 7 espaços originam 9x8x7 tabelas com 6 espaços
9x8x7 tabelas com 6 espaços originam 9x8x7x6 tabelas com 5 espaços
9x8x7x6 tabelas com 5 espaços originam 9x8x7x6x5 tabelas com 4 espaços
9x8x7x6x5 tabelas com 4 espaços originam 9x8x7x6x5x4 tabelas com 3 espaços
9x8x7x6x5x4 tabelas com 3 espaços originam 9x8x7x6x5x4x3 tabelas com 2 espaços
9x8x7x6x5x4x3 tabelas com 2 espaços originam 9x8x7x6x5x4x3x2 tabelas com 1 espaço
9x8x7x6x5x4x3x2 tabelas com 1 espaços originam 9x8x7x6x5x4x3x2x1 tabelas com 0 espaços
9x8x7x6x5x4x3x2x1

total de 986410 tabelas
"""
from random import randint, seed
import math


class Node:
    def __init__(self):
        self.table = None
        self.next = []
        self.prev = None

    def print_under(self):
        for n in self.next:
            n.print_under()
        print(self.table.print_table())

    def clone_node(self, i_pos, turn):
        new_Node = Node()
        new_Table = Table()
        new_Table.pos = self.table.pos.copy()
        if turn == 'x':
            new_Table.pos[i_pos] = 1
        else:
            new_Table.pos[i_pos] = 2
        new_Node.table = new_Table
        self.next.append(new_Node)
        new_Node.prev = self
        new_Node.table.empty_slots = self.table.empty_slots - 1
        return new_Node


class Tree:
    def __init__(self):
        self.root = None


class Table:
    def __init__(self):
        self.pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.empty_slots = 9
        # valor 0 = empate, 1 = vitória, -1 = derrota ( sempre tomando o x como referência)
        self.value = 0
        self.value_temp = -3

    def print_table(self):
        for i in range(9):
            print("|", end="")
            if self.pos[i] == 0:
                print(" |", end="")
            elif self.pos[i] == 1:
                print("X|", end="")
            elif self.pos[i] == 2:
                print("O|", end="")
            if i != 0 and (i + 1) % 3 == 0:
                print()

    def value_check(self):
        winner = -1
        if self.pos[0] == self.pos[1] == self.pos[2] != 0:
            winner = self.pos[0]
        elif self.pos[3] == self.pos[4] == self.pos[5] != 0:
            winner = self.pos[3]
        elif self.pos[6] == self.pos[7] == self.pos[8] != 0:
            winner = self.pos[6]
        elif self.pos[0] == self.pos[3] == self.pos[6] != 0:
            winner = self.pos[0]
        elif self.pos[1] == self.pos[4] == self.pos[7] != 0:
            winner = self.pos[1]
        elif self.pos[2] == self.pos[5] == self.pos[8] != 0:
            winner = self.pos[2]
        elif self.pos[0] == self.pos[4] == self.pos[8] != 0:
            winner = self.pos[0]
        elif self.pos[2] == self.pos[4] == self.pos[6] != 0:
            winner = self.pos[2]
        # em caso de empate
        elif self.empty_slots == 0:
            return 0
        return winner

    def table_compare(self, table):
        same_elements = 0
        for i in range(9):
            if self.pos[i] == table.pos[i] and self.pos[i] != 0:
                same_elements += 1
        return same_elements

    def check_winner(self):
        winner = 0
        if self.pos[0] == self.pos[1] == self.pos[2] != 0:
            winner = self.pos[0]
        elif self.pos[3] == self.pos[4] == self.pos[5] != 0:
            winner = self.pos[3]
        elif self.pos[6] == self.pos[7] == self.pos[8] != 0:
            winner = self.pos[6]
        elif self.pos[0] == self.pos[3] == self.pos[6] != 0:
            winner = self.pos[0]
        elif self.pos[1] == self.pos[4] == self.pos[7] != 0:
            winner = self.pos[1]
        elif self.pos[2] == self.pos[5] == self.pos[8] != 0:
            winner = self.pos[2]
        elif self.pos[0] == self.pos[4] == self.pos[8] != 0:
            winner = self.pos[0]
        elif self.pos[2] == self.pos[4] == self.pos[6] != 0:
            winner = self.pos[2]
        elif self.empty_slots == 0:
            winner = 3
        return winner


def generate_tree(tree, node, turn, cont):
    if tree.root is None:
        tree.root = node
    # se for no folha
    if node.table.empty_slots == 0:
        if node.table.value_check() == 0:
            node.table.value = 0
        elif node.table.value_check() == 1:
            node.table.value = 1
        elif node.table.value_check() == 2:
            node.table.value = -1
        return cont + 1
    # parte abaixo serve para os nodos internos
    for i in range(9):
        # verifica se a posição está vazia
        if node.table.pos[i] == 0:
            # max
            # propaga o melhor resultado do nó mais externo para o próximo nó interno
            val = node.table.value_check()
            if turn == 'x':
                new_Node = node.clone_node(i, turn)
                cont = generate_tree(tree, new_Node, 'o', cont)
                # se o valor do nodo n puder ser definido apenas por ele mesmo, olha os próximos
                if val == -1:
                    if new_Node.table.value == 1:
                        node.table.value_temp = 1
                    elif new_Node.table.value == 0 and node.table.value_temp != 1:
                        node.table.value_temp = 0
                    elif new_Node.table.value == -1 and node.table.value_temp != 1 and node.table.value_temp != 0:
                        node.table.value_temp = -1
                else:
                    if val == 2:
                        node.table.value_temp = -1
                    else:
                        node.table.value_temp = val
            # min
            # propaga o pior resultado do nó mais externo para o próximo nó interno
            else:
                new_Node = node.clone_node(i, turn)
                cont = generate_tree(tree, new_Node, 'x', cont)
                # se o valor do nodo n puder ser definido apenas por ele mesmo, olha os próximos
                if val == -1:
                    if new_Node.table.value == -1:
                        node.table.value_temp = -1
                    elif new_Node.table.value == 0 and node.table.value_temp != -1:
                        node.table.value_temp = 0
                    elif new_Node.table.value == 1 and node.table.value_temp != -1 and node.table.value_temp != 0:
                        node.table.value_temp = 1
                else:
                    if val == 2:
                        node.table.value_temp = -1
                    else:
                        node.table.value_temp = val

    node.table.value = node.table.value_temp

    print(round((cont/986410)*100, 2), "%")

    return cont + 1


# faz uma busca na árvore pelo melhor "caminho" de jogadas e retorna um nodo com tabela igual a atual
def table_search_with_value(node, table, plays):
    # compara a tabela procurada com a tabela do nodo atual
    num_same_elements = table.table_compare(node.table)
    # verifica se todos os elementos do nodo em questão são iguais ao procurado
    if num_same_elements == (9 - node.table.empty_slots):
        # verifica se as tabelas são completamente iguais
        if table.empty_slots == node.table.empty_slots:
            # adiciona a jogada na lista de jogadas de 1 ponto
            for _node in node.next:
                if _node.table.value == 1:
                    plays[1].append(_node)
                # adiciona a jogada na lista de jogadas de 0 pontos
                if _node.table.value == 0:
                    plays[0].append(_node)
        # se n forem completamente iguais ainda tem passos faltando, tenta encontrar a tabela totalmente igual dnv
        else:
            for i in node.next:
                if i is not None:
                    plays = table_search_with_value(i, table, plays)
    return plays


# recebe um tabuleiro como entrada, e retorna a melhor jogada para x no formato de coordenadas (x,y)
def minmax(tree, _table):
    x = 0
    y = 0
    plays = {0: [], 1: []}
    plays = table_search_with_value(tree.root, _table, plays)
    # se n houverem jogadas de valor 1 pega alguma de valor 0
    if not plays[1]:
        _node = plays[0][0]
    else:
        _node = plays[1][0]
    for i in range(9):
        # procura a jogada na tabela selecionada
        if _table.pos[i] != _node.table.pos[i]:
            y = i % 3
            x = math.floor(i / 3)
    return x, y


# ALGUMA MERDA TA BUGADA CONCERTAR DPS
def init_game():
    tree = Tree()
    node = Node()
    tree.root = node
    node.table = Table()
    generate_tree(tree, node, 'x', 0)
    turn = "x"
    x = 0
    y = 0
    of_table = Table()
    over = False
    while not over:
        if turn == "x":
            print("VEZ DO X")
            x, y = minmax(tree, of_table)
            p = 3 * x + y
            of_table.pos[p] = 1
            of_table.empty_slots -= 1
            turn = "o"
        else:
            turn = "x"
            go = False
            while not go:
                x = input("Entre com o x: ")
                y = input("Entre com o y: ")
                if (x == "0" or x == "1" or x == "2") and (y == "0" or y == "1" or y == "2"):
                    k = 3 * int(x) + int(y)
                    if of_table.pos[k] == 0:
                        of_table.pos[k] = 2
                        of_table.empty_slots -= 1
                        go = True
                        of_table.print_table()
                    else:
                        print("Escolha uma posição vazia.")
                else:
                    print("Entre com valores válidos: 0 a 2")

        print()
        print()
        of_table.print_table()
        print()

        winner = of_table.check_winner()
        if winner != 0:
            over = True
        if winner == 1:
            print("X venceu!")
        if winner == 2:
            print("O venceu!")
        if winner == 3:
            print("Empatou!")


init_game()