from django.shortcuts import render
from .tasks import *

def index(request):
    if request.method == 'POST':
        x = request.POST.get('n1')
        y = request.POST.get('n2')
        z = add.delay(x, y)
        print('z: ', z)
        return render(request, 'index.html', {'z':z.get()})
    return render(request, 'index.html')

def stud(request, count):
    if count:
        # for i in range(count):
        add_stud.apply_async(args=[count])
        return render(request, 'stud.html', {'msg': 'students added'})
    return render(request, 'stud.html')

def delete(request):
    delete_stud.delay()
    return render(request, 'stud.html', {'msg': 'students deleted'})