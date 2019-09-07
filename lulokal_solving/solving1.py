'''
run => python solving1.py
after running you can input words with separated (dont use space only separated)
and this program will be sort by abjad
        '''
words = raw_input("enter words, comma separated = ")
words = words.split(',')
print(','.join(sorted(words)))