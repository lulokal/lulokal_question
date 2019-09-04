"""
    Ginus Pandhu Setyawna
    ginus_pandhu@hotmail.com / 082282227625
"""

import operator

tuples_1 = ("Tom", 19, 80)
tuples_2 = ("John", 20, 90)
tuples_3 = ("Jony", 17, 91)
tuples_4 = ("Jony", 17, 93)
tuples_5 = ("Jason", 21, 85)

list_of_tuple = [tuples_1, tuples_2, tuples_3, tuples_4, tuples_5]
list_of_tuple.sort(key=operator.itemgetter(0, 1, 2))
print(list_of_tuple)
