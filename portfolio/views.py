from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def portfolio(request):
  return render(request, "portfolio.html")

def data(request):
  return render(request, "data.html")


def add(request):
  return render(request, 'form.html')

def data(request):
  return render(request, 'data.html')