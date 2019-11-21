from django.db import models
import csv
import math
import random
import json


class Profile(models.Model):
    date = models.TextField()
    retweets = models.TextField()
    favorites = models.TextField()
    text = models.TextField()
    # id = models.TextField(primary_key=True)
    flag = models.CharField(max_length=1, default='0')

    def __str__(self):
        return "" + self.date + " " + self.text


def loadCsv(filename):
    lines = csv.reader(open(r'gempa_bumi_2018.csv'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset


def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet):
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
        return [trainSet, copy]


def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
            separated[vector[-1]].append(vector)
            return separated


def mean(numbers):
    return sum(numbers)/float(len(numbers))


def stdev(numbers):
    avg = mean(numbers)
    variance = sum([pow(x-avg, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summarize(dataset):
    summaries = [(mean(attribute), stdev(attribute))
                 for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
        return summaries
