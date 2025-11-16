
list = [1,2,2,3]
set = set()
def analize_list(list,set):
    sum = 0
    dict = {'num':0,"avg":0,"minV":1000,"maxV":0}
    print(dict['num'])
    for item in list:
        set.add(item)
        sum+=item
        if item < dict["minV"]:
            dict["minV"] = item
        if item > dict["maxV"]:
             dict["maxV"] = item
    dict['num']=set
    dict['avg']=sum/len(list)

    return dict


print(analize_list(list,set))

dict = {
    "Moshe":10000,
    "Chaim":40050,
    "Shmoel":10200,
    "Avi":40200,
    "Efraim":74100
}
threshold = 50000


def filter_dicts(dict,threshold):
     new_list = []

     for item in dict:
         print(item)
         if dict[item] > threshold:
             new_list.append(item)
     return new_list

print(filter_dicts(dict,threshold))