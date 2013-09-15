from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from receipts.models import *

def goHome(request):
  return render(request, 'index.html')

def login(request):
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  user = auth.authenticate(username=username, password=password)
  if user is not None and user.is_active:
    auth.login(request, user)
    return HttpResponseRedirect("dashboard")
  else:
    return HttpResponseRedirect("invalid")

def logout(request):
  auth.logout(request) 
  return HttpResponseRedirect("/")

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect("dashboard")
  else:
    form = UserCreationForm()
  return render(request, "register.html", {'form': form})

def dashboard(request):
  return render(request, 'dashboard.html')

# populate table in request page
def receipts(request):
  receipt_list = list(Receipt.objects.all())
  group_list = list(Homies.objects.filter(dawgs__username__exact=
                                            request.user.username))
  return render(request, "receipts.html", {'group_list' : group_list, 
                          'receipt_list' : receipt_list})
# create new receipt
def newreceipt(request):
  title = request.POST.get('title')
  date = request.POST.get('date')
  totalPrice = request.POST.get('totalPrice')
  category = request.POST.get('category')
  owner = Dawg.objects.get(username=request.user.username)
  groups = Homies.objects.get(id=request.POST.get('groups'))
  r = Receipt(title=title, date=date, totalPrice=totalPrice, category=category)
  r.save()
  r.owner.add(owner)
  r.groups.add(groups)
  r.save()
  return HttpResponseRedirect("receipts")


