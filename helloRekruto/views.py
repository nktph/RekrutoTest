from django.shortcuts import render

# Create your views here.
def helloRekruto(request):

    name = request.GET.get('name')
    message = request.GET.get('message')

    if not name and not message:
        name="Rekruto"
        message="Давай дружить"

    return render(request, 'hello.html',{'name':name, 'message':message})