from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This Data Is Our Assumption       { Actual Data Coming From Database Only...}'
    D={'assumption':data,'age':'SANJU age is 22','job':'We need to Get a Job as a Software Developer'}
    return render(request,'data_render.html',context=D)
