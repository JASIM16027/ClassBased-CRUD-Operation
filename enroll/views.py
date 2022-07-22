from django.shortcuts import render
from .forms import StudentAddForm
from .models import User
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.
class UserAddShowView(TemplateView):
    template_name ='enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentAddForm()
        stud = User.objects.all()
        context ={'form': form, 'student': stud}
        return context

    def post(self, request):
        if request.method=='POST':
            form = StudentAddForm(request.POST)
            if form.is_valid():
                name = form.clean_data['name']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password'];
                reg = User(name=name,email=email, password=password)
                reg.save()
        return HttpResponseRedirect('/')


#this class will update / edit
class UserUpdateView(View):
    def get(self,request,update_id):
        upd = User.objects.get(pk=update_id)
        form = StudentAddForm(instance=upd)
        return render(request,'enroll/updatestudent.html',{'form':form})
    def post(self,request,update_id):
        if request.method=="POST":
            upd = User.objects.get(pk=update_id)
            form = StudentAddForm(request.POST,instance=upd)
            if form.is_valid():
                form.save()
        return render(request,'enroll/updatestudent.html',{'form':form})
        #return HttpResponseRedirect('/')

class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    
# this class will delete data
def delete_data(request,id):
    if request.method=='POST':
        dlt = User.objects.get(pk=id)
        dlt.delete()
    return HttpResponseRedirect('/')