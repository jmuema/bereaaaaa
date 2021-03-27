from django.shortcuts import render

# Create your views here.
def web(request):

    return render(request, 'website/index.html')