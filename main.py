# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:28:13 2017

@author: Andy Chen
"""

from turing_machine import Tape, TuringMachine

table = {(0, 0): (0, 0, 'R'),
         (0, 1): (1, 1, 'R'),
         (1, 0): (2, 1, 'R'),
         (1, 1): (1, 1, 'R'),
         (2, 0): (3, 0, 'L'),
         (2, 1): (2, 1, 'R'),
         (3, 1): (0, 0, 'S')}

tm = TuringMachine(table, q=[0, 1, 2, 3], w=[0, 1],
                   tape=Tape([0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                             2))

i = 1
print('===== {} ====='.format(i))
print(tm.getValue())
while tm.transition():
    i = i + 1
    print('===== {} ====='.format(i))
    print(tm.getValue())
