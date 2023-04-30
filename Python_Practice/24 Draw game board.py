flor = '--'
wall = '|'
space =' '

i = int(input('input table size '))
line = flor*i+'\n'+(wall+space)*i+wall+'\n'
print(line*i+ flor*i)