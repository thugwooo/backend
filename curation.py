from csv_to_dict import dog_breed
from datetime import datetime
import re


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
    breed = dog_breed()
    for row in breed:
        if row['breed'] == curationData['breed']:
            curationData['size'] = row['size']


def setLifeStage(curationData):
    if curationData['pet'] == '강아지':
        birth = curationData['birthYear'] + '-' + \
            curationData['birthMonth'] + '-' + curationData['birthDay']
        birth = datetime.strptime(birth, '%Y-%m-%d')
        month = (datetime.now() - birth).days//30+1
        curationData['month'] = month
        print(month)
        if month < 12:
            curationData['life_stage'] = '퍼피'
        elif month < 85:
            curationData['life_stage'] = '어덜트'
        else:
            curationData['life_stage'] = '시니어'


curationData = {'pet': '강아지', 'birthYear': '2022',
                'birthMonth': '8', 'birthDay': '4'}
setLifeStage(curationData)


def make_url(name):
    han = re.compile('[^ ㄱ-ㅣ가-힣+]')
    st = han.sub('', name)
    st = st.replace(' ', '-')
    return st
