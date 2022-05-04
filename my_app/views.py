from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')


def variables_view(request):

    variables = {
        'first_name': 'John',
        'last_name': 'Williams',
        'playlist': ['Hedwig\'s Theme', 'Journey to the Island']
    }

    return render(request, 'my_app/variables.html', context=variables)