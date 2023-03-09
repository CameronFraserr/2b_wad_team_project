import django
from dorm_detective_app.models import University, UserProfile

django.setup()


def populate():
    universities = {
        'University of Glasgow': {
            'latitude': 55.872107, 'longitude': -4.288219,
        },
        'University of Strathclyde': {
            'latitude': 55.862194, 'longitude': -4.242386,
        },
        'Glasgow Caledonian University': {
            'latitude': 55.866883, 'longitude': -4.250399},
    }

    for university, uni_data in universities.items():
        uni = add_university(university, uni_data['latitude'], uni_data['longitude'])

    for uni in University.objects.all():
        print(f'- {uni}')


def add_university(name, latitude, longitude):
    uni = University.objects.get_or_create(name=name)[0]
    uni.latitude = latitude
    uni.longitude = longitude
    uni.save()

    return uni
