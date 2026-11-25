# Ex.03 Design a Website for Server Side Processing
## Date:15.11.2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
    <head>
        <title>churn calculator</title>
    </head>
    <body>
        <h1>Surya Narayana K R S-26017252</h1>
        <form method="POST">
            {%csrf_token%}
            <label>INITIAL: </label>
            <input type="number" name="Initialcust" value="{{Initialcust}}" ><br><br>
            <label>PRESENT: </label>
            <input type="number" name="Presentcust" value="{{Presentcust}}"><br><br>
            <label>CHURN_RATE: </label><input type="number" name="churn_rate" value="{{churn_rate}}"><br><br>
            <input type="submit" value="calculate">
            <input type="reset">
        </form>
        
    </body>
</html>

views.py

from django.shortcuts import render
def calculateChurnRate(request):
    Initialcust = float(request.POST.get('Initialcust', '0'))
    Presentcust = float(request.POST.get('Presentcust', '0'))
    churn_rate =  ((Initialcust - Presentcust) /Initialcust )*100 if request.method == 'POST' else 0
    print("Initialcust =",Initialcust)
    print("Presentcust =",Presentcust)
    print("churn_rate =",churn_rate)
    return render(request, 'yapp/sam.html',{'Initialcust': Initialcust, 'Presentcust': Presentcust, 'churn_rate': churn_rate })

urls.py

from django.contrib import admin
from django.urls import path
from yapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculateChurnRate,name='calculateChurnRate'),
]



```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (66).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (67).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
