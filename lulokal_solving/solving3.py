'''
run = python solving3.py
input name,age,height
*just separate with comma
enter for end or closing input and this program will be show output
                                                                       '''
Tuples = []
while True:
    input_tupl = raw_input('name,age,height = ')
    if input_tupl != '':
        tupl = input_tupl.split(',')
        tupl [1], tupl [2] = int(tupl[1]), int(tupl[2])
        Tuples.append(tuple(tupl))
    elif input_tupl == '':
        print('\n',sorted(Tuples))
        break