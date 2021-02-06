from django.shortcuts import render, HttpResponse
from Home import textUtil

# Create your views here.
def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        textValue = request.POST.get('txtArea')
        task = request.POST.get('taskName')
        if(textValue and len(textValue) > 0):
            if(task == 'removePunch'):
                task ='Removing Punctuations'
                result = textUtil.removePunctuations(textValue)
            elif(task == 'upperCase'):
                task ='Converting into UpperCase'
                result = textUtil.ConverUpperCase(textValue)
            elif(task == 'beautifyData'):
                task ='Beautifying Data'
                result = textUtil.beautifyJson(textValue)
            elif(task == 'lowerCase'):
                task ='Converting into LowerCase'
                result = textUtil.ConvertLowerCase(textValue)
    return render(request, 'result.html',{'result':result, 'task': task})
