from django.http import HttpResponse
def firstview(request):
    return HttpResponse('<h1>DJANGO APPLICATION ON AWS</h1>')