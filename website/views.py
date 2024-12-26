from django.shortcuts import render

# Function to define 
def home_panel(request):
    return render(request, 'homepanel.html', {})
