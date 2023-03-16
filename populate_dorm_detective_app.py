import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorm_detective.settings')

django.setup()

from dorm_detective_app.models import University, UserProfile


def populate():
    universities = {
        'University of Glasgow': {
            'latitude': 55.872107, 'longitude': -4.288219, 'website': 'https://www.gla.ac.uk/',
            'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean laoreet mattis justo, non efficitur velit. Nunc sem elit, placerat non sollicitudin in, accumsan rutrum metus. Quisque commodo sodales est, eget cursus orci faucibus nec. Suspendisse odio leo."
        },
        'University of Strathclyde': {
            'latitude': 55.862194, 'longitude': -4.242386, 'website': 'https://www.strath.ac.uk/',
            'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean laoreet mattis justo, non efficitur velit. Nunc sem elit, placerat non sollicitudin in, accumsan rutrum metus. Quisque commodo sodales est, eget cursus orci faucibus nec. Suspendisse odio leo."
        },
        'Glasgow Caledonian University': {
            'latitude': 55.866883, 'longitude': -4.250399, 'website': 'https://www.gcu.ac.uk/',
            'description': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean laoreet mattis justo, non efficitur velit. Nunc sem elit, placerat non sollicitudin in, accumsan rutrum metus. Quisque commodo sodales est, eget cursus orci faucibus nec. Suspendisse odio leo."
        },
    }

    for university, uni_data in universities.items():
        uni = add_university(university, uni_data['latitude'], uni_data['longitude'],uni_data['description'], uni_data['website'])

    for uni in University.objects.all():
        print(f'- {uni}')


def add_university(name, latitude, longitude, description, website):
    uni = University.objects.get_or_create(name=name)[0]
    uni.latitude = latitude
    uni.longitude = longitude
    uni.description = description
    uni.website = website
    uni.save()

    return uni


if __name__ == '__main__':
    print('Running the population script...')
    populate()
