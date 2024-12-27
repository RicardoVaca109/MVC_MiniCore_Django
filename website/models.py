from django.db import models

# Create your models here.
# Model employees o Empleados
class Employees(models.Model):
    name_employee = models.CharField(max_length=50)
    last_name_employee = models.CharField(max_length=50)
    
    def __str__(self):
        return(f"{self.name_employee} {self.last_name_employee}")
    
# Model Department o departamentos
class Departments(models.Model):
    name_department = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.name_department}")
    
# Model  Spent o gasto 
class Spent(models.Model):
    date_spent = models.DateField()
    description_spent = models.CharField(max_length=250)
    amount_spent = models.FloatField()
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)  
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"{self.description_spent} {self.amount_spent} {self.date_spent}"
    