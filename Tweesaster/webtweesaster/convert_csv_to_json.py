import csv
import json
from webtweesaster.models import Profile
allData = []

# https://docs.python.org/2/library/csv.html
# change to the csv file name that you are trying to upload
def open_csv():
    file_name = 'gempa_bumi_2018.csv'
    with open(file_name) as csvfile:
        csvfile = csv.reader(csvfile, delimiter=';')
        for each in csvfile:
            temp = '{"username": "' + each[0] + '",' + '"date": "' + each[1] + '",' + '"retweets": "' + each[2] + '",' + '"favorites": "' + each[3] + '",' + '"text": "' + each[4].replace('"', '') + '",' + '"geo": "' + \
                each[5] + '",' + '"mentions": "' + each[6] + '",' + '"hashtags": "' + each[7] + '",' + \
                '"id": "' + each[8] + '",' + '"permalink": "' + \
                each[9] + '",' + '"flag": "' + each[10] + '"}'
            # print(temp, "\n")
            temp = json.loads(temp)
            Profile.objects.create(retweets=temp["retweets"], favorites=temp["favorites"], flag=temp["flag"],text=temp["text"])
            
        print(allData)
        

    # app_name = 'webtweesaster' # change this to your Django app name
    # model_name = 'person' # the name of you Django model
    # field_1 = 'date' # the name of first field
    # field_2 = 'retweets' # the name of second field
    # field_3 = 'favorites' # the name of first field
    # field_4 = 'text' # the name of second field
    # field_5 = 'id' # the name of first field
    # field_6 = 'flag' # the name of second field
    # x = 0
    # output = []
    # for each in csvfile:
    #     x += 1
    #     row = {}
    #     row = {'model': app_name+'.'+model_name, 'pk': x, 'fields': ({field_1: each[field_1], field_2: each[field_2], field_3: each[field_3], field_4: each[field_4], field_5: each[field_5], field_: each[field_2]})}
    #     output.append(row)
    # json.dump(output, open('converted_file.json','w'), indent=4, sort_keys=False)


# ........ json data model example......
# [
#   {
#     "model": "myapp.person",
#     "pk": 1,
#     "fields": {
#       "first_name": "John",
#       "last_name": "Lennon"
#     }
#   },
#   {
#     "model": "myapp.person",
#     "pk": 2,
#     "fields": {
#       "first_name": "Paul",
#       "last_name": "McCartney"
#     }
#   }
# ]
