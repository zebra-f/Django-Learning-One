from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')


def variables_view(request):

    variables = {
        'first_name': 'John',
        'last_name': 'Williams',
        'playlist': ['Hedwig\'s Theme', 'Journey to the Island', 'Out to Sea', 'Binary Sunset'],
        'movies_playlist': {
            'Harry Potter': ['Hedwig\'s Theme', 'Harry\'s Wondrous World', 'Christmas at Hogwarts'],
            'Jurassic Park': ['Journey to the Island'],
            'Jaws': ['Out to Sea'],
            'Star Wars': ['Binary Sunset', 'Princess Leia\'s Theme']
        },
        'playing': False
    }

    return render(request, 'my_app/variables.html', context=variables)