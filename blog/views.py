from django.shortcuts import render
from django.views.generic import ListView , DetailView
from roommseters.models import Roommset
from roommseters.filters import RoommsetFilter
from django.core.paginator import Paginator
# Create your views here.
# view show all the sekeer room list form the database
def rommseterslist(request):
    obj = Roommset.objects.filter(type_seeker ='seeker')
    form = RoommsetFilter(request.GET,queryset=Roommset.objects.filter(type_seeker ='seeker'))
    obj = form.qs
    paginator = Paginator(obj, 25) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html',{'form':form,'object_list':page_obj})