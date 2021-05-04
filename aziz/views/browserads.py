from django.shortcuts import render

def browserads(request):
    return render(request, "home/browserads.html")