import csv
with open('eggs.csv', 'w', newline= '') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ' ', 
                            quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'] * 3)
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline= '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', 
                            quotechar = '|')
    for row in spamreader:
        print(', '.join(row))
