prob_tweet_as_disaster = ?
prob_tweet_not_disaster = ?

disaster_dict = ?
not_disaster_dict = ?

def naive_bayes(tweet) :
	tweet_split = tweet.split()
	prob_disaster = calc_disaster(tweet_split)
	prob_not_disaster = calc_not_disaster(tweet_split)

	if (prob_disaster >= prob_not_disaster) :
		return True
	else:
		return False



def calc_not_disaster(data):
	prob = 1
	for word in data:
		if word in (not_disaster_dict.keys()):
			pembilang = not_disaster_dict[word] + 1
			d = len(not_disaster_dict) + len(data)
			penyebut = len(not_disaster_dict) + d
			prob *= (pembilang/penyebut)
		else :
			pembilang = 1
			d = len(not_disaster_dict) + len(data)
			penyebut = len(not_disaster_dict) + d
			prob *= (pembilang/penyebut)

	return (prob*prob_tweet_not_disaster)

def calc_disaster(data):
	prob = 1
	for word in data:
		d = len(disaster_dict) + len(data)
		penyebut = len(disaster_dict) + d

		if word in (disaster_dict.keys()):
			pembilang = disaster_dict[word] + 1
			prob *= (pembilang/penyebut)
		else :
			pembilang = 1
			prob *= (pembilang/penyebut)

	return (prob*prob_tweet_as_disaster)