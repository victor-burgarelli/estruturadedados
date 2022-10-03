from listnode import ListNode


class LinkedList:
    def __init__(self):
        #construtor da classe
        self.head = None
        self._size = 0
        self.maxSize = 30
        self.listIterator = None
        self.tail = None

    def nextNode(self):
        #passa o iterador para o proximo node
        if self.listIterator:
            self.listIterator = self.listIterator.next

    def __setitem__(self, index, elem):
        #altera os dados de um elemento n da lista
        self.listIterator = self.head
        for i in range(index):
            if self.listIterator:
                self.listIterator = self.listIterator.next

            else:
                raise IndexError("list index out of range")

        if self.listIterator:
            self.listIterator.nome = elem
        else:
            raise IndexError("list index out of range")

    def insNode(self, data):
        # insere um elemento numa posição n da lista e o coloca antes do iterador
        if self._size == 0:
            self.listIterator = ListNode(data)
            self.head = self.listIterator
            self.tail = self.listIterator
            self._size += 1

        elif self.listIterator == self.head:
            newNode = ListNode(data)
            self.listIterator.prev = newNode
            newNode.next = self.listIterator
            self.head = newNode
            self.listIterator = newNode
            self._size += 1

        elif self.listIterator and self.listIterator.next:
            buffer = self.listIterator.next
            newNode = ListNode(data)
            self.listIterator = newNode
            newNode.prev = self.listIterator
            newNode.next = buffer
            buffer.prev = newNode
            self.listIterator = newNode
            self._size += 1

        elif not self.listIterator.next:
            newNode = ListNode(data)
            self.listIterator.next = newNode
            newNode.prev = self.listIterator
            self.tail = newNode
            self._size += 1

    def posNode(self, position):
        self.listIterator = self.head
        for i in range(position):
            self.nextNode()

    def elimNode(self):
        #elimina o node da lista

        if not self.undefinedIterator():
            if self.listIterator == self.head:
                self.nextNode()
                self.head = self.listIterator
                self.listIterator.prev = None
                self._size -= 1
                if self._size == 0:
                    self.tail = self.listIterator

            elif not self.listIterator.next:
                self.tail = self.listIterator.prev
                self.listIterator = self.listIterator.prev
                self.listIterator.next = None
                self._size -= 1
                self.listIterator = self.head
            else:
                buffer = self.listIterator.next
                self.listIterator = self.listIterator.prev
                self.listIterator.next = buffer
                buffer.prev = self.listIterator
                self._size -= 1
                self.nextNode()

    def firstNode(self):
        #coloca o iterador no inicio da lista
        self.listIterator = self.head

    def lastNode(self):
        #coloca o iterador no final de lista
        while self.listIterator.next:
            self.listIterator = self.listIterator.next

    def addNode(self, data):
        #insere um node apos o iterador
        if self._size == 0:
            newNode = ListNode(data)
            self.head = newNode
            self.tail = self.head
            self.listIterator = newNode
            self._size += 1

        elif not self.undefinedIterator() and self.listIterator.next:
            buffer = self.listIterator
            newNode = ListNode(data)
            self.listIterator = self.listIterator.next
            self.listIterator.prev = newNode
            newNode.prev = self.listIterator
            newNode.next = self.listIterator
            self.listIterator = newNode
            newNode.prev = buffer
            buffer.next = newNode
            self._size += 1

        elif not self.undefinedIterator():
            newNode = ListNode(data)
            self.listIterator.next = newNode
            newNode.prev = self.listIterator
            self.tail = newNode
            self.listIterator = newNode
            self._size += 1

    def undefinedIterator(self):
        #verifica se o iterador esta em algum endereco de memoria
        if not self.listIterator:
            return True
        else:
            return False
   
    def __str__(self):
        #formata o print
        lista = ""
        self.firstNode()
        while (self.listIterator):
            lista = lista + str(self.listIterator.data)
            self.nextNode()
        lista = lista.strip(", ")
        return lista




