from django.shortcuts import render
from.models import Hotel
# Create your views here.




from . models import Rating,Hotel

from django.contrib.auth.models import User

from .forms import ReviewForm


def give_review(request,pk):
    if request.method=="POST":
        required_hotel=Hotel.objects.get(pk=pk)
        form =  ReviewForm(request.POST)
        form.instance.user=request.user
        form.instance.hotel= required_hotel
        if form.is_valid():
            form.save()
        
        return render(request,'thank.html')

        
        
        

        
    else:
        form =  ReviewForm()

    return render(request,'review.html',{'form':form})
