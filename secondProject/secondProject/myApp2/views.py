from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp2.forms import StudentForm
# Create your views here.
def hello(request):
	return HttpResponse('now ur in myApp2')

def register(request):
	if request.method=='POST':
		form = StudentForm(request.POST)
		form.save()
		return redirect('/myapp2/register')
	form = StudentForm()
	return render(request,'myApp2/register.html',{'form':form})