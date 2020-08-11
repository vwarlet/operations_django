from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, a,b):
    som = a + b
    sub = a - b
    mul = a * b
    div = a / b

    str_som = '<h1>{} + {} = {}</h1>'.format(a,b,som)
    str_sub = '<h1>{} - {} = {}</h1>'.format(a,b,sub)
    str_mul = '<h1>{} * {} = {}</h1>'.format(a,b,mul)
    str_div = '<h1>{} / {} = {}</h1>'.format(a,b,div)
    result = str_som + str_sub + str_mul + str_div

    return HttpResponse(result)