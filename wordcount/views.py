from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'Hola':'Hi there'})

def eggs(request):
    return HttpResponse('<h1>eggs</h1>')

def count(request):
    fulltext =request.GET['textareaname']
    wordslist= fulltext.split()
    worddict={}
    for word in wordslist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordslist),
    'worddict':sortedwords})
