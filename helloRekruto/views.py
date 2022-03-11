from django.shortcuts import render

# Create your views here.
def helloRekruto(request):

    name = request.GET.get('name')
    message = request.GET.get('message')

    if not name:
        name="Rekruto"

    if not message:
        message="Давай дружить"

    return render(request, 'hello.html',{'name':name, 'message':message})