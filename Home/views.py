from django.shortcuts import render
def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("value1"))
            n2=eval(request.POST.get("value2"))
            opr=request.POST.get("opr")
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2 
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="invalid opretor"
    return render(request,"index.html",{'c':c})                    


# Create your views here.
