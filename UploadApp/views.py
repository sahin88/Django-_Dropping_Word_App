from django.shortcuts import render
from .models import Keys
from .forms  import KeysForm
import json 
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import ListView
import os

def count_list_function(list_items):
    empty_dict={}
    for list_item in list_items:
        list_item=list_item.strip()
        if list_item not in empty_dict:
            empty_dict[list_item]=1
        else:
            empty_dict[list_item]+=1
    return empty_dict
        

def validate_extension_function(name):
    accepted_extensions=['.pdf','.docx']
    file_extension = os.path.splitext(name)[1]
    if file_extension not in accepted_extensions:
        return False
    return True


def validate_keywords_function(keywords):
    treshold=5
    if len(keywords.split())>treshold:
        return False
    return True


def keyword_compare_function(list_1, list_2):
    compare = lambda x, y: count_list_function(x) == count_list_function(y)
    return compare(list_1, list_2)



def home (request):
    return render(request, 'home.html',{})

    



def downloads(request):
    keywords_query_sets=Keys.objects.all()
    return render(request, 'downloads.html',{'keywords_query_sets': keywords_query_sets})





   
def update_keyword_list_func(request):
    user_data=json.loads(request.body)
    id_from_user= int(user_data['keyword_list_id'])
    
    keys = Keys.objects.get(id=id_from_user)
    if not keyword_compare_function(keys.keys,user_data['keyword_update_list']):  
        return JsonResponse({'success':'false','message':'You are not allowed to change,edit or add items !'}, safe=False)

    keys.keys=user_data['keyword_update_list']
    keys.save()
    return  JsonResponse({'success':'true','message':'Keywords has been succesfully re-ordered !'}, safe=False)


   
def saveUpload(request):
    if request.method == 'POST':
        keys_form=KeysForm(request.POST,request.FILES)
        if not keys_form.is_valid():
            return  render(request, 'home.html',{'form':keys_form})
        keyword_from_user=request.POST.get('keywords')
        if not validate_keywords_function(keyword_from_user):
            messages.error(request, 'The Number of keywords exceeded the max value!')
            return  render(request, 'home.html',{'form':keys_form})

        file=request.FILES['document']
        file_name=file.name
        if not validate_extension_function(file_name):
            messages.error(request, 'You have uploaded a file, whose extension is not supported!')
            return  render(request, 'home.html',{'form':keys_form})

        new_document_object = Keys.objects.create(keys= keyword_from_user.split(), docfile =file)
        messages.success(request, 'Form submitted successfully!')
        return  render(request, 'home.html',{'form':keys_form})




class KeysListView(ListView):
	model=Keys
	template_name='downloads.html'
	context_object_name='keywords_query_sets'
	paginate_by=3




        
