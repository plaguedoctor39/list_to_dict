list1 = ['2018-01-01', 'yandex', 'cpc', 100]
def list_to_dict(list1):
    d1 = {}
    temp = d1
    for i, k in enumerate(list1, 1):
        if len(list1)-1 == i:
            temp[k] = list1[i]
            break
        temp[k] = {}
        temp = temp[k]
    return d1
print(list_to_dict(list1))