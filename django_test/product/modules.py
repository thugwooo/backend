
def str_to_list(data):
    data = data.replace(' ', '').replace('[', '').replace(']', '').replace("'",'').split(',')
    return data