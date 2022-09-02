import dogBreed
from datetime import datetime, timedelta


def filteringAlg(key, petfood):
    filtered_data = []

    for row in petfood:
        flag = True
        for alg in row['alg']:
            if alg in key:
                flag = False
        if flag:
            filtered_data.append(row)
    return filtered_data


def filteringHealth(key, petfood):
    filtered_data = []
    # 통통해요 일때 다이어트 사료 포함시키기
    for row in petfood:
        flag = False
        for health in row['health']:
            if health in key:
                flag = True
        if flag:
            filtered_data.append(row)
    return filtered_data


def setSize(curationData):
    breed = dogBreed.csv_to_dict()
    for row in breed:
        if row['breed'] == curationData['breed']:
            curationData['size'] = row['size']


def setLifeStage(curationData):

    birth = curationData['birthYear'] + '-' + \
        curationData['birthMonth'] + '-' + curationData['birthDay']
    birth = datetime.strptime(birth, '%Y-%m-%d')
    month = datetime.now() - birth
    print(datetime.now())
    print(month.days//30+1)


curationData = {'birthYear': '2022', 'birthMonth': '8', 'birthDay': '12'}
setLifeStage(curationData)
