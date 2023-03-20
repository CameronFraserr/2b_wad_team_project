import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorm_detective.settings')

django.setup()

from dorm_detective_app.models import University, Accommodation, UserProfile


def populate():
    uofg_accommodations = [
        {'name': 'Finnieston Avenue',
         'description': """Finnieston Avenue is a shared accommodation managed by the University of Glasgow and is located in the West End of Glasgow.
                    \n\n
                    It provides 300 shared and en-suite rooms for both Undergraduate and Post-graduate students pursing degrees at the University of Glasgow.""",
         'latitude': 25.213212,
         'longitude': 12.232324,
         'rent_max': 150.23,
         'rent_min': 113.23,
         }
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
            'accommodations': uofg_accommodations,
        },
        'University of Strathclyde': {
            'latitude': 55.862194, 'longitude': -4.242386, 'website': 'https://www.strath.ac.uk/',
            'description': """The University of Strathclyde is a public research university located in
                            Glasgow, Scotland. Founded in 1796 as the Andersonian Institute, it is Glasgow's 
                            second-oldest university.""",
            'accommodations': [],
        },
        'Glasgow Caledonian University': {
            'latitude': 55.866883, 'longitude': -4.250399, 'website': 'https://www.gcu.ac.uk/',
            'description': """Glasgow Caledonian University, informally GCU, Caledonian or Caley, is a
                            public university in Glasgow, Scotland. It was formed in 1993 by the merger of The Queen's College,
                            Glasgow and Glasgow Polytechnic.""",
            'accommodations': [],
        },
    }

    for university, uni_data in universities.items():
        uni = add_university(university, uni_data['latitude'], uni_data['longitude'],uni_data['description'], uni_data['website'])
        for a in uni_data['accommodations']:
            add_accommodation(uni, a['name'], a['description'], a['latitude'], a['longitude'], a['rent_max'], a['rent_min'])

    for uni in University.objects.all():
        print(f'- {uni}')

    for acc in Accommodation.objects.all():
        print(f'- {acc}')


def add_university(name, latitude, longitude, description, website):
    uni = University.objects.get_or_create(name=name)[0]
    uni.latitude = latitude
    uni.longitude = longitude
    uni.description = description
    uni.website = website
    uni.save()

    return uni


def add_accommodation(uni, name, description, latitude, longitude, rent_max, rent_min):
    accom = Accommodation.objects.get_or_create(university=uni, name=name)[0]
    accom.description = description
    accom.latitude = latitude
    accom.longitude = longitude
    accom.rent_max = rent_max
    accom.rent_min = rent_min
    accom.save()

    return accom


if __name__ == '__main__':
    print('Running the population script...')
    populate()
