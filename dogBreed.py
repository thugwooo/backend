import csv


def csv_to_dict():
    data = []

    with open('dogBreed.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_value = {}
            dict_value['breed'] = row['견종']
            dict_value['size'] = row['사이즈']
            data.append(dict_value)
    return data
