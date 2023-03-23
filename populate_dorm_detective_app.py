import random

import django
import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorm_detective.settings')

django.setup()

from dorm_detective_app.models import University, Accommodation, UserProfile, User, Review


def populate():
    POPULATION_RESOURCES = 'population_script_resources/'

    users = [
        {'username': "NOTABOT",
         'password': "123asd1vgfA",
         'student': True,
         },
        {'username': "CHATGPT",
         'password': "NEW_SKYNET123",
         'student': True,
         }
    ]

    murano_revs = [
        {'title': "WOW!",
         'description': "AMAZING PLACE! Will surely come back there next year.",
         'likes': 4,
         'rating': 5,
         },
    ]

    student_apart_revs = [
        {'title': "Close to Uni",
         'description': "Very close to the University, but that's about it.",
         'likes': 2,
         'rating': 4,
         },
        {'title': "Crap!",
         'description': "Toilets were very dirty.",
         'likes': 0,
         'rating': 1,
         },
    ]

    finn_avenue_revs = [
        {'title': "Scam!",
         'description': "This place doesn't even exist anymore!? Please take it down, it's only confusing people!",
         'likes': 1,
         'rating': 1,
         },
    ]

    uofg_accommodations = [
        {'name': 'Student Apartments',
         'description': """Student Apartments offers self-catered undergraduate student houses and student flats based 
         in traditional tenement buildings which are typically located in close proximity to the University.""",
         'latitude': 55.874358,
         'longitude': -4.287646,
         'rent_max': 144.83,
         'rent_min': 115.36,
         'revs': student_apart_revs,
         'image_path': POPULATION_RESOURCES + 'student_apart.jpg'
         },
        {'name': 'Murano Street Student Village',
         'description': """Murano Street Student Village is our largest residence and provides self-catered accommodation 
         for undergraduate students. The self-contained flats comprise of single study bedrooms, a common living/kitchen area, 
         bathroom and toilet facilities.""",
         'latitude': 55.882591,
         'longitude': -4.276740,
         'rent_max': 134.47,
         'rent_min': 134.47,
         'revs': murano_revs,
         'image_path': POPULATION_RESOURCES + 'murano.jfif'
         }
    ]

    uofst_accommodations = [
        {'name': 'Finnieston Avenue',
         'description': """Finnieston Avenue is a shared accommodation managed by the University of Strathclyde and is located in the West End of Glasgow.
                \n\n
                It provides 300 shared and en-suite rooms for both Undergraduate and Post-graduate students pursing degrees at the University of Strathclyde.""",
         'latitude': 25.213212,
         'longitude': 12.232324,
         'rent_max': 150.23,
         'rent_min': 113.23,
         'revs': finn_avenue_revs,
         'image_path': POPULATION_RESOURCES + 'finniestion_avenue.jpg'
         },
    ]

    uofcal_accommodations = [
        {'name': 'Caledonian Court',
         'description': """Our ‘village within the city’, Caledonian Court, is the perfect place to live if you’re 
         looking for that home-from-home atmosphere. Living at Caledonian Court is an ideal way to make friends 
         with people from all over the world, and our international community includes students from places such as Nigeria, 
         China, Greece, France, Germany and America.""",
         'latitude': 55.868409,
         'longitude': -4.248446,
         'rent_max': 160.23,
         'rent_min': 110.23,
         'revs': [],
         'image_path': POPULATION_RESOURCES + 'caledonian_court.jfif',
         },
    ]

    universities = {
        'University of Glasgow': {
            'latitude': 55.872107, 'longitude': -4.288219, 'website': 'https://www.gla.ac.uk/',
            'description': """The University of Glasgow (abbreviated as Glas. in post-nominals; Scottish Gaelic: Oilthigh
                        Ghlaschu[4]) is a public research university in Glasgow, Scotland. Founded by papal bull in 1451
                        [O.S. 1450],[5] it is the fourth-oldest university in the English-speaking world and one of
                        Scotland's four ancient universities. Along with the universities of Edinburgh, Aberdeen, and St
                        Andrews, the university was part of the Scottish Enlightenment during the 18th century.
                        \n\n
                        In common with universities of the pre-modern era, Glasgow originally educated students
                        primarily from wealthy backgrounds; however, it became a pioneer[citation needed] in British
                        higher education in the 19th century by also providing for the needs of students from the
                        growing urban and commercial middle class. Glasgow University served all of these students by
                        preparing them for professions: law, medicine, civil service, teaching, and the church. It also
                        trained smaller but growing numbers for careers in science and engineering.[6] The annual income
                        of the institution for 2021–22 was £923.6 million of which £196.1 million was from research
                        grants and contracts, with an expenditure of £998.5 million.[1] The university has the
                        sixth-largest endowment of any university in the UK. It is a member of Universitas 21, the
                        Russell Group[7] and the Guild of European Research-Intensive Universities.""",
            'synopsis': """The University of Glasgow is a public research university in Glasgow, Scotland. Founded by papal bull in 1451
                        [O.S. 1450],[5] it is the fourth-oldest university in the English-speaking world and one of
                        Scotland's four ancient universities.""",
            'accommodations': uofg_accommodations,
            'image_path': POPULATION_RESOURCES + 'glasgow.jpg',
        },
        'University of Strathclyde': {
            'latitude': 55.862194, 'longitude': -4.242386, 'website': 'https://www.strath.ac.uk/',
            'description': """The University of Strathclyde is a public research university located in
                            Glasgow, Scotland. Founded in 1796 as the Andersonian Institute, it is Glasgow's 
                            second-oldest university.""",
            'synopsis': """The University of Strathclyde is a public research university located in
                            Glasgow, Scotland. Founded in 1796 as the Andersonian Institute, it is Glasgow's 
                            second-oldest university.""",
            'accommodations': uofst_accommodations,
            'image_path': POPULATION_RESOURCES + "strathclyde.jpg"
        },
        'Glasgow Caledonian University': {
            'latitude': 55.866883, 'longitude': -4.250399, 'website': 'https://www.gcu.ac.uk/',
            'description': """Glasgow Caledonian University, informally GCU, Caledonian or Caley, is a
                            public university in Glasgow, Scotland. It was formed in 1993 by the merger of The Queen's College,
                            Glasgow and Glasgow Polytechnic.""",
            'synopsis': """Glasgow Caledonian University, informally GCU, Caledonian or Caley, is a
                            public university in Glasgow, Scotland. It was formed in 1993 by the merger of The Queen's College,
                            Glasgow and Glasgow Polytechnic.""",
            'accommodations': uofcal_accommodations,
            'image_path': POPULATION_RESOURCES + "caledonian.jpg"
        },
    }

    user_profs = []

    for user in users:
        user_profs.append(add_user(user['username'], user['password'], user['student']))

    for university, uni_data in universities.items():
        uni = add_university(university, uni_data['latitude'], uni_data['longitude'], uni_data['description'],
                             uni_data['website'], uni_data['synopsis'], uni_data['image_path'])
        for a in uni_data['accommodations']:
            accom = add_accommodation(uni, a['name'], a['description'], a['latitude'], a['longitude'], a['rent_max'],
                                      a['rent_min'], a['image_path'])
            for rev in a['revs']:
                add_review(accom, rev['title'], rev['description'], rev['likes'], rev['rating'],
                           random.choice(user_profs))

    for uni in University.objects.all():
        print(f'- {uni}')

    for acc in Accommodation.objects.all():
        print(f'- {acc}')


def add_university(name, latitude, longitude, description, website, synopsis, img):
    uni = University.objects.get_or_create(name=name)[0]
    uni.latitude = latitude
    uni.longitude = longitude
    uni.description = description
    uni.website = website
    uni.synopsis = synopsis
    uni.picture = img
    uni.save()

    return uni


def add_accommodation(uni, name, description, latitude, longitude, rent_max, rent_min, img):
    accom = Accommodation.objects.get_or_create(university=uni, name=name)[0]
    accom.description = description
    accom.latitude = latitude
    accom.longitude = longitude
    accom.rent_max = rent_max
    accom.rent_min = rent_min
    accom.picture = img
    accom.save()

    return accom


def add_user(username, password, is_student):
    user = User.objects.get_or_create(username=username, password=password)[0]
    user.save()
    user_profile = UserProfile.objects.get_or_create(user=user, current_student=is_student)[0]
    user_profile.save()

    return user_profile


def add_review(accommodation, title, description, likes, rating, user):
    rev = Review.objects.get_or_create(accommodation=accommodation, user=user)[0]
    rev.title = title
    rev.description = description
    rev.likes = likes
    rev.rating = rating
    rev.datetime = timezone.now()
    rev.save()

    return rev


if __name__ == '__main__':
    print('Running the population script...')
    populate()
