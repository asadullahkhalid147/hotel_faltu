from django.shortcuts import render,redirect
from express.models import Hotel

# Create your views here.

def home(request):
    if request.method =='POST':
        we_need = request.POST['needed_kyeword']
        hotel_list =  Hotel.objects.filter(hotel_name__contains=we_need)

    else:
        hotel_list=Hotel.objects.all()
    return render(request,'index.html', {'hotel_list':hotel_list})

def hotel_details(request,pk):
    required_hotel=Hotel.objects.get(pk=pk)
    return render(request,'details_view.html', {'required_hotel':required_hotel})
    



def booking(request,pk):
    if  not request.user.is_authenticated :
        return redirect('login_veiw')
    if request.method =='POST':
             required_hotel=Hotel.objects.get(pk=pk)
             required_hotel.customers.add(request.user)
             required_hotel.save() 
             return render(request,'go_home.html')

    else:
        return render(request,'hotel_booking.html')