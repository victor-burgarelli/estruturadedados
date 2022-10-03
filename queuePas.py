from queuenode import QueueNode


class Queue:

    def __init__(self):
        #construtor da classe
        self.first = None
        self.last = None
        self._size = 0
        self.maxSize = 10
        self.queueIterator = self.first

    def push(self, elem):
        # insere um elemento no final da fila

        if self._size < self.maxSize:
            node = QueueNode(elem)

            if self.first is None and self.last is None:
                self.first = node
                self.last = node

            else:
                self.last.next = node
                self.last = node

            self._size += 1

        else:
            raise IndexError("Can't add. The queue is full")

    def pop(self):
        # remove o primeiro elemento da fila

        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
        else:
            raise IndexError("Can't remove. The queue is empty")

    def peek(self):
        # retorna o topo da fila
        if self._size > 0:
            return self.first.data

        raise IndexError("The queue is empty")

    def __len__(self):
        # retorna o tamanho da fila
        return self._size

    def nextNode(self):
        #pula iterador da fila
        self.queueIterator = self.queueIterator.next
        if not self.queueIterator:
            self.queueIterator = None
    
    def firstNode(self):
        #aponta para o inicio da fila
        self.queueIterator = self.first

    def __str__(self):
        #configura o print da fila
        fila = ""
        self.firstNode()
        while (self.queueIterator):
            fila = fila + str(self.queueIterator.data)
            self.nextNode()
        return fila





