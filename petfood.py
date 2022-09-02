import csv


def csv_to_dict():
    data = []
    with open('petfood.csv', newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            dict_value = {}
            dict_value['product_code'] = row['제품코드']
            dict_value['pet'] = row['대상']
            dict_value['name'] = row['이름']
            dict_value['type'] = row['Large_주식']
            dict_value['shape'] = row['Medium_사료형태']
            dict_value['brand'] = row['Small1_브랜드']
            dict_value['life_stage'] = row['Small2_Life stage']
            dict_value['size'] = row['Small3_반려동물크기']
            dict_value['health'] = row['Small4_건강개선기능']
            dict_value['feature'] = row['Small5_사료특징(Special diet)']
            dict_value['main_ingredient'] = row['Small6_주원료']
            dict_value['all_ingredient'] = row['전성분']
            dict_value['alg'] = row['알레르기']
            dict_value['kibble'] = row['Small9_알갱이크기']
            dict_value['weight'] = row['Small10_무게']
            dict_value['protein'] = row['조단백(DM)%']
            dict_value['fat'] = row['조지방(DM)%']
            dict_value['fiber'] = row['조섬유(DM)%']
            dict_value['ash'] = row['조회분(DM)%']
            dict_value['calcium'] = row['칼슘(DM)%']
            dict_value['phosphorus'] = row['인(DM)%']
            dict_value['kcal'] = row['칼로리Kcal/100g']
            dict_value['retail_price'] = row['판매가']
            dict_value['whole_price'] = row['도매가']

            data.append(dict_value)
    return data
