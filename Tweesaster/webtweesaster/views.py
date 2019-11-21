from django.shortcuts import render
from .convert_csv_to_json import open_csv
from webtweesaster.models import Profile
from django.shortcuts import HttpResponse
from django.core.exceptions import *

dict = {}
sampah = ["ada", "terjadi", "lagi"]


class counter():
	alldata = Profile.objects.all()
	for each in alldata:
		text = each.text.lower().split(" ")
		flag = each.flag
		for word in text:
			# word = word.lower()
			if flag != "flag":
				if word in dict:
					dict[word][int(flag)] += 1
				else:
					dict.update({word: [0, 0]})
					dict[word][int(flag)] += 1


def home(request):
	Profile.objects.all().delete()
	# dict = {}
	open_csv()
	counter()
	print(dict)
	for word in dict.keys():
		if dict[word][1] > 0 :
			print(word, dict[word][1])
	return render(request, 'home.html')


def search(request):
	if request.method == 'POST':
		data = request.POST.get('textfield')
		print(analyze(data))
		return render(request, 'home.html')
	else:
		return render(request, 'home.html')


def analyze(tweet):
	print(tweet)
	words = tweet.lower().split(" ")
	p_true = 1
	p_false = 1
	for word in words:
		if word in dict.keys():
			print(word, ":true", dict[word][1], ",false", dict[word][0])
			if dict[word][1] > 0:
				p_true *= (dict[word][1] + 1) / (dict[word][0] + dict[word][1] + len(dict.keys()))
			else:
				p_true *= 1 / (dict[word][0] + dict[word][1] + len(dict.keys()))
			
			if dict[word][0] > 0:
				p_false *= (dict[word][0] + 1) / (dict[word][0] + dict[word][1] + len(dict.keys()))
			else:
				p_false *= 1 / (dict[word][0] + dict[word][1] + len(dict.keys()))
	print("==========ANALYSIS============")
	print("true:", p_true, ",false:", p_false,"\nthen:")
	if p_true > p_false:
		return True
	else:
		return False
	
