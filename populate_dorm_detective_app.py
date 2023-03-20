import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dorm_detective.settings')

django.setup()

from dorm_detective_app.models import University, UserProfile


def populate():
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
                        Russell Group[7] and the Guild of European Research-Intensive Universities."""
        },
        'University of Strathclyde': {
            'latitude': 55.862194, 'longitude': -4.242386, 'website': 'https://www.strath.ac.uk/',
            'description': """The University of Strathclyde is a public research university located in
                            Glasgow, Scotland. Founded in 1796 as the Andersonian Institute, it is Glasgow's 
                            second-oldest university."""
        },
        'Glasgow Caledonian University': {
            'latitude': 55.866883, 'longitude': -4.250399, 'website': 'https://www.gcu.ac.uk/',
            'description': """Glasgow Caledonian University, informally GCU, Caledonian or Caley, is a
                            public university in Glasgow, Scotland. It was formed in 1993 by the merger of The Queen's College,
                            Glasgow and Glasgow Polytechnic."""
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
