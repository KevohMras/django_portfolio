from django.http import HttpResponse
from django.template import loader

def portfolio(request):
  return render(request, 'portfolio.html')