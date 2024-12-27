from django.shortcuts import render
from django.db.models import Sum
from .models import Employees, Departments, Spent

def home_panel(request):
    
    start_date = request.GET.get('start_date')  
    end_date = request.GET.get('end_date')     

    
    employees = Employees.objects.all()
    departments = Departments.objects.all()
    spent = Spent.objects.all()

   
    if start_date and end_date:
        department_expenses = Spent.objects.filter(
            date_spent__range=[start_date, end_date]
        ).values(
            'department__name_department'
        ).annotate(
            total_spent=Sum('amount_spent')
        ).order_by('-total_spent')
    else:
        
        department_expenses = []

    return render(request, 'homepanel.html', {
        'employees': employees,
        'departments': departments,
        'spent': spent,
        'department_expenses': department_expenses,
        'start_date': start_date,
        'end_date': end_date,
    })
