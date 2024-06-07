from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    message = f'''
    Path: {request.path} <br/ >
    Path: {request.META['REMOTE_ADDR']} <br/ >
    Path: {request.scheme} <br/ >
    Path: {request.method} <br/ >
    Path: {request.META['HTTP_USER_AGENT']} <br/ >
    '''
    return HttpResponse(message, content_type='text/html', charset='utf-8')
