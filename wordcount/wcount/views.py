from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def homepage(requests):
 #   return HttpResponse('<h1>Home Page</h1>')

#def about(requests):
   # return HttpResponse('<h1>about</h1>')

#def count(requests):
 #   return HttpResponse('<h1>count</h1>')    

def homepage(requests):
    return render(requests,'wcount/homepage.html')

def about(requests):
    return render(requests,'wcount/about.html')

def count(requests):

   fulltext=requests.GET['text']
   counter = len(fulltext.split()) 
   # return render(requests,"wcount/count.html",{'fulltext':fulltext,'counter':counter}) 
   word_dict={}
   for w in fulltext.split():
      if w in word_dict:
         word_dict[w] +=1
      else:
         word_dict[w] = 1
   word_count_list= [(w,word_dict[w]) for w in word_dict]
   return render(requests,'wcount/count.html',{'text':fulltext,'count':counter,'word_dict':word_dict,'word_count_list':word_count_list})
      
