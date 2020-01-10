from django.http import HttpResponse
from django.shortcuts import render
import operator
import string

def homepage(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET["full_text"]
    
    striped_text = full_text.strip()
    no_punc_text = striped_text.translate(striped_text.maketrans("", "", string.punctuation))

    word_list = no_punc_text.split()
    word_dictionary = {}

    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1

    count = len(word_list)
    
    word_dict_oredered = {k: v for k, v in sorted(word_dictionary.items(), key=lambda item: item[1], reverse=True)}
    print(word_dict_oredered)
    return render(request, 'count.html', {'full_text':full_text, 'count':count, 'sorted_list':word_dict_oredered})

    #sorted_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    #return render(request, 'count.html', {'full_text':full_text, 'count':count, 'sorted_list':sorted_list})

def about(request):
    return render(request, 'about.html')
