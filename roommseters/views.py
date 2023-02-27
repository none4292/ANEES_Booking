from django.shortcuts import render , redirect 
from django.views.generic import ListView , DetailView , CreateView
from .models import Roommset , PropertyReview
from .froms import PropertyReviewForm
from django.views.generic.edit import FormMixin
from .filters import RoommsetFilter
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.

def rommseterslist(request):
    obj = Roommset.objects.filter(type_seeker ='seracher')
    form = RoommsetFilter(request.GET,queryset=Roommset.objects.filter(type_seeker ='seracher'))
    obj = form.qs
    paginator = Paginator(obj, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'roommseters/roommset_list.html',{'form':form,'object_list':page_obj})
def RoomDetail(request,id):
    obj = Roommset.objects.get(id=id)
    reviews = PropertyReview.objects.filter(property=obj)
    form = PropertyReviewForm()
    if request.method == 'POST':
        myform = PropertyReviewForm(request.POST)
        if form.is_valid():
            myform.author = request.user 
            myform.property = obj 
            myform.save()
    return render(request,'roommseters/roommset_detail.html',{'object':obj,'reviews':reviews,'form':form})



class NewProperty(CreateView):
    model = Roommset
    fields = ['title','description','price','place','image', 'gender','lifestaly','type_seeker']


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.seeker = request.user
            myform.save()
            return redirect(reverse('roommseters:room_list'))
