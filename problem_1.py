"""
    Ginus Pandhu Setyawna
    ginus_pandhu@hotmail.com / 082282227625
"""

input_string = raw_input("Insert your comma separated word: ")
split_string = input_string.split(',')
sorted_list = sorted(split_string)
result = ','.join(sorted_list)
print(result)
