from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key = '73909c1432024857afbe16806b538f64')
    top = newsapi.get_top_headlines(sources = 'bbc-news')

    l1 = top['articles']
    desc = []
    news = []
    news = []
    img = []

    for i in range(len(l1)):
        f1 = l1[i]
        news.append(f1['title'])
        desc.append(f1['description'])
        img.append(f1['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'index.html', context ={"mylist":mylist})