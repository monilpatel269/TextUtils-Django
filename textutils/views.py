from ssl import Purpose
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def analyse(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    allinone = request.POST.get('allinone','off')
    
    punctuatuions = '''!()-[];:'"\/,<>.?@#$%^&*_~'''
    if removepunc == "on":
         analysed = ""
         cnt = 0
         for char in djtext:
             if char not in punctuatuions:
                analysed = analysed + char
                if char!=" ":
                    cnt+=1
            
         params = {'purpose':'Removed punctuations', 'analysed_text': analysed,'chars':cnt}
         djtext=analysed
        #  return render(request,'analyse.html',params)
    
    if(fullcaps=='on'):
        analysed=""
        cnt = 0
        for char in djtext:
            analysed = analysed + char.upper()
            if char!=" ":
                cnt+=1 
        
        params = {'purpose':'changed to upper case', 'analysed_text': analysed,'chars':cnt}
        djtext=analysed
        # return render(request,'analyse.html',params)            
    
    if(newlineremover=='on'):
        analysed=""
        cnt = 0
        for char in djtext:
            if char !='\n' and char not in punctuatuions and char!="\r":
                analysed = analysed + char.upper()
                if char!=" ":
                    cnt+=1

        params = {'purpose':'changed to upper case and new line removed', 'analysed_text': analysed,'chars':cnt}
        djtext=analysed
        # return render(request,'analyse.html',params)
    
    if(extraspaceremover=='on'):
        analysed=""
        cnt = 0
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1] == " ") and char!="\r":
                analysed = analysed + char.upper()
                if char!=" ":
                    cnt+=1

        params = {'purpose':'changed to upper case and extra space removed', 'analysed_text': analysed,'chars':cnt}
        djtext=analysed
        # return render(request,'analyse.html',params)
    
    if(allinone=='on'):
        analysed=""
        cnt = 0
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1] == " ") and char!='\n' and char not in punctuatuions and char!="\r":
                analysed = analysed + char.upper()
                if char!=" ":
                    cnt+=1

        params = {'purpose':'Everything Applied', 'analysed_text': analysed,'chars':cnt}
        djtext=analysed
        # return render(request,'analyse.html',params)
    
    if(removepunc!="on" and newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on" and allinone!="on"):
        cnt=0
        params = {'purpose':'Select atleast one option','analysed_text':'Error','chars':cnt}
        return render(request,'analyse.html',params)
    # else:
    #     return HttpResponse("Error")

    return render(request,'analyse.html',params)