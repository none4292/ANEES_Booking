from django.shortcuts import render , redirect 
from django.views.generic import ListView , DetailView , CreateView
from .models import Roommset , PropertyReview
from .froms import PropertyReviewForm
from django.views.generic.edit import FormMixin
from .filters import RoommsetFilter
from django.urls import reverse
from django.core.paginator import Paginator
from accounts.models import Proflie
# Create your views here.

# get all rommseters if type_seeker owner and add the paginator and fliter 
def rommseterslist(request):
    obj = Roommset.objects.filter(type_seeker ='owner')
    form = RoommsetFilter(request.GET,queryset=Roommset.objects.filter(type_seeker ='owner'))
    obj = form.qs
    paginator = Paginator(obj , 25) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'roommseters/roommset_list.html',{'form':form,'object_list':page_obj})
# get the one room by id as primerykey to lookup and get the reviews for that room and user sekeer info and add the review
def RoomDetail(request,id):
    obj = Roommset.objects.get(id=id)
    reviews = PropertyReview.objects.filter(property=obj)
    user_info = Proflie.objects.get(user = obj.seeker)
    form = PropertyReviewForm()
    if request.method == 'POST':
        form = PropertyReviewForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.property = obj 
            myform.save()
    return render(request,'roommseters/roommset_detail.html',{'object':obj,'reviews':reviews,'form':form,'info':user_info})

#cbv -- create -- list -- detail --- edit 
#the view for add new Proprety and save it
class NewProperty(CreateView):
    model = Roommset
    fields = ['title','description','price','place','image', 'gender','lifestaly','type_seeker','avablie_at']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.seeker = request.user
            myform.save()
            
            if myform.type_seeker == "seeker":
                return redirect(reverse('blog:serachers_list'))
            else:
                return redirect(reverse('roommseters:room_list'))
                
                
