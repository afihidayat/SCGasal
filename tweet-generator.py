import twitter, json

def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 200,since='2017-01-01',until='2017-12-30')
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
    except:
        print("Something went wrong")
        return None
    return ([{"id":status.id,"text":status.text,"date":status.created_at,"location":status.location} for status in tweets_fetched])

def writeToFile(path,data):
    file = open(path, "a+")
    file.write('[\n')
    for dictionary in data: 
        dict_to_json = json.dumps(dictionary)
        file.write(dict_to_json + ",\n")
    file.write(']')
# initialize api instance
twitter_api = twitter.Api(consumer_key='IlZ0a3CpHmi3kUxFJcyla0wI1',
    consumer_secret='FLLLQDYPAoox8scyDh5a4bpe97H6OGnlhXY8WnQNaJVuuNwupC',
    access_token_key='103190390-O3YasEybxMuQs4eGuVo7Cty0GYkCQuVmrU8u8deq',
    access_token_secret='FbbiRSgBDky3A4jHyuid2Fbxo72AGMwiiy76p37IvNmka')
search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)
writeToFile('kumpulan_tweet/2017.json',testDataSet)