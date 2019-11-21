from django.shortcuts import render
from .convert_csv_to_json import open_csv
from webtweesaster.models import Profile
from django.shortcuts import HttpResponse
from django.core.exceptions import *

dict = {}
class counter():
    alldata = Profile.objects.all()
    for each in alldata:
        text = each.text.split(" ")
        flag = each.flag
        for word in text:
            if flag != "flag":
                if word in dict:
                    dict[word][int(flag)] += 1
                else:
                    dict.update({word: [0, 0]})
                    dict[word][int(flag)] += 1

def home(request):
	Profile.objects.all().delete()
	open_csv()
	counter()
	print(dict)
	return render(request, 'home.html')

def search(request):
	if request.method == 'POST':
		search_id = request.POST.get('textfield', None)
		try:
			get_text = request.POST["textfield"]
			return HttpResponse("get_text")
		except:
			return HttpResponse("no such user")
	else:
		return render(request, 'home.html')
