# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:19:05 2017

@author: Andy Chen
"""


class Tape(object):
    def __init__(self, tape=[], we='#'):
        '''
        tape: Data on tape
        we: Empty word
        '''
        self._tape = tape
        self._we = we

    def __str__(self):
        result = ''
        for w in self._tape:
            result = result + str(w) + ' '
        return result

    def change(self, ind, w):
        if len(self._tape) <= ind:
            for i in range(self._len, ind):
                self._tape.append(self._we)
            self._tape.append(w)
        else:
            self._tape[ind] = w

    def get(self, ind):
        if len(self._tape) > ind:
            return self._tape[ind]
        else:
            return self._we


class TuringMachine(object):
    def __init__(self, table, q=[0, 1], w=['A', 'B', 'C'], q0=0,
                 tape=Tape()):
        '''
        table: Function table
        q: Machine state
        w: Tape state
        q0: Init. machine state
        tape: Tape
        '''
        self._table = table
        self._Q = q
        self._W = w
        self._q = q0

        self._tape = tape
        self._head = 0
        self._halted = False

    def transition(self):
        f = self.getValue()
        if f in self._table:
            next_t = self._table[f]
            self._q, new_w, new_a = next_t
            self._tape.change(self._head, new_w)
            if new_a == 'R':
                self._head = self._head + 1
            elif new_a == 'L':
                if not self._head == 0:
                    self._head = self._head - 1
            elif new_a == 'S':
                self._halted = True
            print(self._tape)
            if self._halted:
                print('Halted!')
                return False
            return True
        else:
            self._halted = True
            print(self._tape)
            print('Error!')
            return False

    def getValue(self):
        return (self._q, self._tape.get(self._head))
