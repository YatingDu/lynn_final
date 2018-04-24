from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):

    if request.method =='POST':
        item = request.POST.get('item')
        address = request.POST.get( "address")
        return render(request, 'order/home_page.html',{'item':item,'address':address})


    return render(request, 'order/home_page.html')
