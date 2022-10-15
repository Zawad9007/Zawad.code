from django.shortcuts import render,HttpResponse

# Create your views here.
def index(reqeust):
    return HttpResponse('this is home page')
def about(reqeust):
    return HttpResponse('this is about page')