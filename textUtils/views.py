# This file is created by Sucheta

from django.http import HttpResponse, HttpRequest
#from django.http import request
from django.shortcuts import render, redirect

# Code for displaying text home.txt in home page
# def index(request):
#     f=open('textUtils/home.txt', 'r')
#     file_content = f.read()
#     f.close()
#     return HttpResponse(file_content, content_type="text/plain")

# def about(request):
#     return HttpResponse('''<h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Tutorials </a> </h1>''')

def index(request):
    return render(request, 'index.html')
    

def analyze(request):
    #get the text-input text
    djtext = request.POST.get('text','default')
    analyzed=djtext

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')    
    newlineremover = request.POST.get('newlineremover','off')    
    extraspaceremover = request.POST.get('extraspaceremover','off')    
    charctercounter = request.POST.get('charctercounter','off')    

    #Check which checkbox is on
    if removepunc=='on':

        punctuations= '''.?!,:;-_()[]{}<>""'/*&#~\@^|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
            
    if fullcaps=='on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose':'Changed to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!='\r':
                analyzed += char
        params = {'purpose':'Removed NewLines', 'analyzed_text':analyzed}
        djtext = analyzed    

    if(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed += char
        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}
        djtext = analyzed
    
    if(charctercounter=='on'):
        char_count = 0
        for char in djtext:
            print(char)
            if char!=" " and char!='\r' and char!='\n':
                char_count += 1

        params = {'purpose':'Text utils', 'analyzed_text':analyzed, 'Characters':char_count}
    

    if(charctercounter=='off'):
        char_count = 0   
        
    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on' and charctercounter!='on'):
        return HttpResponse('Error-Please select any operation and try again')

        
    return render(request, 'analyze.html',params)
    


    

def ex1(request):
    s = '''<h2>Navigation Bar<br></h2>
    <tr><td>Code with Harry </td><td><a href="https://www.youtube.com/@CodeWithHarry">Click here</a> </td>  </tr>
    <tr><td> </td><td> </td> </tr>
    '''
    return HttpResponse(s)

def capfirst(request):
    return HttpResponse("Capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'> back </a>")

def charcount(request):
    return HttpResponse("charcount")






