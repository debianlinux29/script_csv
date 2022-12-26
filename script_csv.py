'''
usage:
@exmple: python3 script_csv.py donner_test.csv username password
argv[0] = script
argv[1] = csv file
argv[2+] = row name
'''

import csv
import sys

list_of_arguments = sys.argv


'''
delimiter=' '
quotechar='|'

'''

file = sys.argv[1]

'''
if delimiter in list_of_arguments:
    delimiter_index = list_of_arguments.index(delimiter)
    delimiter= sys.argv[delimiter_index+1]
else:
    pass


if quotechar in list_of_arguments:
    quotechar_index = list_of_arguments.index(quotechar)
    quotechar= sys.argv[quotechar_index+1]
else:
    pass
'''

row_iter = []
for i in range(2, len(sys.argv)):
    res = sys.argv[i]
    row_iter.append(res)

"""
@func: csv_read_file
@param: file name
@param: array of row name
@return: 2D list with row column
"""

row = []
def csv_read_file(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for res in reader:
            res = [res[i] for i in row_iter]
            row.append(res)

csv_read_file(file)
print(row)

'''
for j,h in enumerate(list) : get list with index value
i = index
j = value
@func: write_as_csv
@param: without param
@return: resultat.csv
'''
def write_as_csv():
    with open('resultat.csv', 'w', newline='') as csvfile:
        fieldnames = row_iter
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        res = {} # dict of value with index fieldnames and value fielvalues
        for i in row: # row variable is a 2D list (i is a list type) ---> read csv file line per line
            for j,h in enumerate(row_iter): # for each line of row enumerate fieldnames
                res[h]= i[j]
                '''
                append dict with fieldnames  row_line[index fieldnames]
                writer.writerow() fonction take a dict of values
                index = fieldnames
                values = fieldvalues
                writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
                '''
            writer.writerow(res) # indent = line per row


write_as_csv()
