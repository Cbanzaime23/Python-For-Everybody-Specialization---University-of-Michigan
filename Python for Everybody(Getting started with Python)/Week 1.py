import csv

def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    import csv

    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table

#print(read_csv_file("Master_2016.csv"))

def bigCount(file_name):
    """Count the frequency of words in a files"""



    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now

        csv_reader = csv.reader(csv_file, delimiter=',')

        #Count word frequency
        counts = dict()
        for line in csv_reader:

            for word in line:
                counts[word] = counts.get(word, 0) + 1

        #Find the most common words
        bigcount = None
        bigword = None
        for word, count in counts.items():
            if bigcount is None or count > bigcount:
                bigword = word
                bigcount = count

    return counts #(bigword, bigcount)

print(bigCount("Master_2016.csv"))
