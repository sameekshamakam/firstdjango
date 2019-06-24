from django.shortcuts import render,redirect
from .forms import BookForm,SearchForm,ModelBookForm
from newhome.models import Book
from django.contrib import messages
#from django.utils import timezone

# Create your views here.
def form_view(request):
    msg=''
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            book=Book(
                name=form.cleaned_data.get('name'),
                #pur_date=form.cleaned_data.get('purchase_date'),
                #Publication=form.cleaned_data.get('publication'),
                book_author=form.cleaned_data.get('book_author')
            )
            book.save()
            msg='book added successfully!!!'
        else:
            msg = form.errors
    else:
        form=BookForm()
    return render(request,'form.html',{'msg':msg,'forms':form})

def html_form(request):
    value=''
    if request.method == "POST":
        value=request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        return render(request,'design.html')

def model_view(request):
    msg=''
    if request.method=='POST':
        form=ModelBookForm(request.POST)
        if form.is_valid():
           
            form.save()
            msg='book added successfully!!!'
        else:
            msg = form.errors
    else:
        form=BookForm()
    return render(request,'form.html',{'msg':msg,'forms':form})


def booksearch(request):
    if request.method =='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            book=Book.objects.filter(name__contains=q)#purchase_date_Itetimezone.now->this can be added
            form=None
            return render(request,'showtables.html',{'book':book,'form':SearchForm})
    else:
        form=SearchForm()
        book=Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})

def deletebook(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Deleted #'+str(id)+'successfully!!!')
    return redirect('/')

def editbook(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        form=ModelBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'editbook.html',{'form':form})
    else:
        form=ModelBookForm(instance=book)
    return render(request,'editbook.html',{'form':form})

