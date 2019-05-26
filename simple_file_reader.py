
if __name__ == '__main__':

    with open('some_file.txt', 'r', encoding='UTF-8') as file:
        line = file.readline()

        print(line)
    results = []
    with open("hw_200.csv", "r", encoding="UTF-8") as file:
        labels = file.readline().strip().split(",")
        for line in file:
            values = line.strip().split(sep=",")
            tuples_list = zip(labels, values)
            data = dict(tuples_list)
            results.append(data)
