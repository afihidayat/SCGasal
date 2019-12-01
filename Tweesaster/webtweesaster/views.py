from django.shortcuts import render
from .convert_csv_to_json import open_csv
from webtweesaster.models import Profile
from django.shortcuts import HttpResponse
from django.core.exceptions import *

dict = {}
sampah = ["ada", "terjadi", "lagi"]
prob_disaster = 0.0
prob_not_disaster = 0.0
total_data = 0.0

class counter():
	alldata = Profile.objects.all()
	for each in alldata:
		total_data += 1
		text = each.text.lower().split(" ")
		flag = each.flag
		if (flag == "1"):
			prob_disaster += 1.0
		else :
			prob_not_disaster += 1.0
		for word in text:
			if flag != "flag":
				if word in dict:
					dict[word][int(flag)] += 1
				else:
					dict.update({word: [0, 0]})
					dict[word][int(flag)] += 1
	prob_disaster = prob_disaster / total_data
	prob_not_disaster = prob_not_disaster / total_data


def home(request):
	Profile.objects.all().delete()
	open_csv()
	counter()
	for word in dict.keys():
		if dict[word][1] > 0 :
			print(word, dict[word][1])
	return render(request, 'home.html')


def search(request):
	if request.method == 'POST':
		data = request.POST.get('textfield')
		result = analyze(data)
		print(result)
		context = {
			'result':result,
			'data':data,
			}
		return render(request, 'result.html', context)
	else:
		return render(request, 'home.html')


def analyze(tweet):
	words = tweet.lower().split(" ")
	p_true = 1
	p_false = 1
	word_not_exist = 0
	for word in words:
		if word not in dict.keys():
			word_not_exist += 1
	for word in words:
		if word in dict.keys():
			p_true *= (dict[word][1] + 1) / (len(dict.keys()) + len(dict.keys()) + word_not_exist)
			p_false *= (dict[word][0] + 1) / (len(dict.keys()) + len(dict.keys()) + word_not_exist)
		else:
			p_true *= (0 + 1) / (len(dict.keys()) + len(dict.keys()) + word_not_exist)
			p_false *= (0 + 1) / (len(dict.keys()) + len(dict.keys()) + word_not_exist)
	p_true *= prob_disaster
	p_false *= prob_not_disaster
	print("==========ANALYSIS============")
	print("true:", p_true, ",false:", p_false,"\nthen:")
	if p_true > p_false:
		return True
	else:
		return False