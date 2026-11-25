from django.shortcuts import render
def calculateChurnRate(request):
    Initialcust = float(request.POST.get('Initialcust', '0'))
    Presentcust = float(request.POST.get('Presentcust', '0'))
    churn_rate =  ((Initialcust - Presentcust) /Initialcust )*100 if request.method == 'POST' else 0
    print("Initialcust =",Initialcust)
    print("Presentcust =",Presentcust)
    print("churn_rate =",churn_rate)
    return render(request, 'yapp/sam.html',{'Initialcust': Initialcust, 'Presentcust': Presentcust, 'churn_rate': churn_rate })
