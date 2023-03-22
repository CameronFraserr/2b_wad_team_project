import tempfile
from django.test import TestCase
from .models import University, UserProfile, Accommodation, Review
from django.contrib.auth.models import User
from dorm_detective_app.models import University
from django.db import migrations, models
from django.apps import apps
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db.migrations.executor import MigrationExecutor
from .models import Accommodation, University

class UniversityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(name='University of Test', latitude=37.7749, longitude=-122.4194)

    def test_name_max_length(self):
        university = University.objects.get(id=1)
        max_length = university._meta.get_field('name').max_length
        self.assertEquals(max_length, 128)

    def test_longitude_min_value(self):
        university = University.objects.get(id=1)
        min_value = university._meta.get_field('longitude').validators[1].limit_value
        self.assertEquals(min_value, -180.0)

    # Adding more tests for the University model as needed

class UserProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpass')
        UserProfile.objects.create(user=user, current_student=True)

    def test_current_student_default_value(self):
        user_profile = UserProfile.objects.get(id=1)
        default_value = user_profile._meta.get_field('current_student').default
        self.assertEquals(default_value, False)

    # Adding more tests for the UserProfile model as needed

class UniversityModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        University.objects.create(name='Test University', latitude=37.7749, longitude=-122.4194, description='Test Description', website='https://testuniversity.com')

    def test_description_default_value(self):
        university = University.objects.get(id=1)
        default_value = university._meta.get_field('description').default
        self.assertEquals(default_value, 'Description')

    def test_latitude_default_value(self):
        university = University.objects.get(id=1)
        default_value = university._meta.get_field('latitude').default
        self.assertEquals(default_value, 0)

    def test_longitude_default_value(self):
        university = University.objects.get(id=1)
        default_value = university._meta.get_field('longitude').default
        self.assertEquals(default_value, 0)

    def test_picture_upload_to(self):
        university = University.objects.get(id=1)
        upload_to = university._meta.get_field('picture').upload_to
        self.assertEquals(upload_to, 'university_images')

    def test_website_blank(self):
        university = University.objects.get(id=1)
        self.assertEquals(university.website, '')

    # Adding more tests for the University model as needed



class UniversityModelTestCase(TestCase):
    def test_latitude_field(self):
        university = University.objects.create(name='Test University', latitude=37.7749, longitude=-122.4194)
        self.assertIsInstance(university.latitude, decimal.Decimal)
        self.assertEqual(university.latitude.as_tuple().exponent, -6)

    def test_longitude_field(self):
        university = University.objects.create(name='Test University', latitude=37.7749, longitude=-122.4194)
        self.assertIsInstance(university.longitude, decimal.Decimal)
        self.assertEqual(university.longitude.as_tuple().exponent, -9)



class UniversityModelTestCase(TestCase):
    def test_latitude_range(self):
        with self.assertRaises(ValidationError):
            University.objects.create(name='Test University', latitude=100, longitude=-122.4194)

        with self.assertRaises(ValidationError):
            University.objects.create(name='Test University', latitude=-100, longitude=-122.4194)

    def test_longitude_range(self):
        with self.assertRaises(ValidationError):
            University.objects.create(name='Test University', latitude=37.7749, longitude=200)

        with self.assertRaises(ValidationError):
            University.objects.create(name='Test University', latitude=37.7749, longitude=-200)



class UniversityModelTestCase(TestCase):
    def test_default_latitude(self):
        university = University.objects.create(name='Test University')
        self.assertEqual(university.latitude, 0)

    def test_default_longitude(self):
        university = University.objects.create(name='Test University')
        self.assertEqual(university.longitude, 0)


class MigrationTestCase(TestCase):
    migrate_from = 'dorm_detective_app.0001_initial'
    migrate_to = 'dorm_detective_app.0002_add_fields_to_university'

    def setUp(self):
        self.app = apps.get_containing_app_config(type('TempConfig', (object,), {'label': 'dorm_detective_app'}).__dict__['label'])
        self.old_apps = self.app.apps
        self.app.apps = self.new_apps = apps.all_models.copy()

    def tearDown(self):
        self.app.apps = self.old_apps

    def test_add_description_field(self):
        university_model = self.new_apps['dorm_detective_app']['University']
        self.assertIn('description', university_model._meta.get_fields())

    def test_add_picture_field(self):
        university_model = self.new_apps['dorm_detective_app']['University']
        self.assertIn('picture', university_model._meta.get_fields())

    def test_add_website_field(self):
        university_model = self.new_apps['dorm_detective_app']['University']
        self.assertIn('website', university_model._meta.get_fields())


class MigrationTestCase(TestCase):
    
    def test_latitude_max_value_validator(self):
        max_value = University._meta.get_field('latitude').validators[0].limit_value
        self.assertEqual(max_value, 90.0)

    def test_latitude_min_value_validator(self):
        min_value = University._meta.get_field('latitude').validators[1].limit_value
        self.assertEqual(min_value, -90.0)

    def test_longitude_max_value_validator(self):
        max_value = University._meta.get_field('longitude').validators[0].limit_value
        self.assertEqual(max_value, 180.0)

    def test_longitude_min_value_validator(self):
        min_value = University._meta.get_field('longitude').validators[1].limit_value
        self.assertEqual(min_value, -180.0)

    def test_latitude_default_value(self):
        default_value = University._meta.get_field('latitude').default
        self.assertEqual(default_value, 0)

    def test_longitude_default_value(self):
        default_value = University._meta.get_field('longitude').default
        self.assertEqual(default_value, 0)


class UniversityModelTests(TestCase):
    
    def test_picture_upload_to_directory(self):
        university = University.objects.create(name='Test University')
        picture = SimpleUploadedFile('test.png', b'file_content', content_type='image/png')
        university.picture = picture
        university.save()
        self.assertEqual(university.picture.path, 'media/university_images/test.png')

class UserProfileModelTests(TestCase):
    
    def test_current_student_default_value(self):
        user = UserProfile.objects.create(email='test@example.com')
        self.assertEqual(user.current_student, True)
        
class AccommodationModelTests(TestCase):
    
    def test_rent_min_max_validation(self):
        university = University.objects.create(name='Test University')
        accommodation = Accommodation.objects.create(name='Test Accommodation', university=university, rent_min=100, rent_max=50)
        with self.assertRaises(ValidationError):
            accommodation.clean_fields()
            
class ReviewModelTests(TestCase):
    
    def test_rating_min_max_validation(self):
        university = University.objects.create(name='Test University')
        accommodation = Accommodation.objects.create(name='Test Accommodation', university=university)
        user = UserProfile.objects.create(email='test@example.com')
        review = Review.objects.create(title='Test Review', description='Test Description', accommodation=accommodation, user=user, rating=0)
        with self.assertRaises(ValidationError):
            review.clean_fields()
            
    def test_review_likes_initial_value(self):
        university = University.objects.create(name='Test University')
        accommodation = Accommodation.objects.create(name='Test Accommodation', university=university)
        user = UserProfile.objects.create(email='test@example.com')
        review = Review.objects.create(title='Test Review', description='Test Description', accommodation=accommodation, user=user)
        self.assertEqual(review.likes, 0)
        
    def test_review_picture_upload_to_directory(self):
        university = University.objects.create(name='Test University')
        accommodation = Accommodation.objects.create(name='Test Accommodation', university=university)
        user = UserProfile.objects.create(email='test@example.com')
        picture = SimpleUploadedFile('test.png', b'file_content', content_type='image/png')
        review = Review.objects.create(title='Test Review', description='Test Description', accommodation=accommodation, user=user, picture=picture)
        self.assertEqual(review.picture.path, 'media/review_images/test.png')


class UniversityModelTest(TestCase):
    def test_upload_image(self):
        university = University.objects.create(name='Test University')
        with tempfile.NamedTemporaryFile(suffix='.jpg') as f:
            image = SimpleUploadedFile(name='test_image.jpg', content=f.read(), content_type='image/jpeg')
            university.picture = image
            university.save()
            self.assertTrue(university.picture)

class UserProfileModelTest(TestCase):
    def test_create_userprofile(self):
        userprofile = UserProfile.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.assertEqual(userprofile.username, 'testuser')
        self.assertEqual(userprofile.email, 'testuser@example.com')
        self.assertEqual(userprofile.password, 'testpassword')

class AccommodationModelTest(TestCase):
    def setUp(self):
        self.university = University.objects.create(name='Test University')
        self.accommodation = Accommodation.objects.create(
            name='Test Accommodation',
            description='Test Description',
            latitude=0,
            longitude=0,
            rent_min=100,
            rent_max=200,
            university=self.university
        )

    def test_create_accommodation(self):
        self.assertEqual(self.accommodation.name, 'Test Accommodation')
        self.assertEqual(self.accommodation.description, 'Test Description')
        self.assertEqual(self.accommodation.latitude, 0)
        self.assertEqual(self.accommodation.longitude, 0)
        self.assertEqual(self.accommodation.rent_min, 100)
        self.assertEqual(self.accommodation.rent_max, 200)
        self.assertEqual(self.accommodation.university, self.university)

    def test_unique_accommodation(self):
        accommodation2 = Accommodation(
            name='Test Accommodation',
            description='Test Description',
            latitude=0,
            longitude=0,
            rent_min=100,
            rent_max=200,
            university=self.university
        )
        with self.assertRaises(Exception):
            accommodation2.save()

class ReviewModelTest(TestCase):
    def setUp(self):
        self.university = University.objects.create(name='Test University')
        self.accommodation = Accommodation.objects.create(
            name='Test Accommodation',
            description='Test Description',
            latitude=0,
            longitude=0,
            rent_min=100,
            rent_max=200,
            university=self.university
        )
        self.userprofile = UserProfile.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_create_review(self):
        review = Review.objects.create(
            title='Test Title',
            description='Test Description',
            likes=10,
            rating=3,
            accommodation=self.accommodation,
            user=self.userprofile
        )
        self.assertEqual(review.title, 'Test Title')
        self.assertEqual(review.description, 'Test Description')
        self.assertEqual(review.likes, 10)
        self.assertEqual(review.rating, 3)
        self.assertEqual(review.accommodation, self.accommodation)
        self.assertEqual(review.user, self.userprofile)

    def test_create_review_invalid_rating(self):
        with self.assertRaises(Exception):
            review = Review.objects.create(
                title='Test Title',
                description='Test Description',
                likes=10,
                rating=6,
                accommodation=self.accommodation,
                user=self.userprofile
            )

class UniversityViewTest(TestCase):
    def setUp(self):
        self.university = University.objects.create(name='Test University')
        self.url = reverse('university', args=[self.university.id]);


class MigrationTestCase(TestCase):
    
    def setUp(self):
        self.migration = __import__('dorm_detective_app.migrations.0003_accommodation', fromlist=['Migration'])
        self.migration_instance = self.migration.Migration()

    def test_dependencies(self):
        self.assertEqual(self.migration_instance.dependencies, [('dorm_detective_app', '0002_auto_20230309_1558')])

    def test_operations(self):
        self.assertEqual(len(self.migration_instance.operations), 1)
        self.assertIsInstance(self.migration_instance.operations[0], migrations.CreateModel)

    def test_create_model_fields(self):
        model = self.migration_instance.operations[0].model_name
        fields = apps.get_model('dorm_detective_app', model)._meta.fields
        field_names = [field.name for field in fields]
        self.assertEqual(len(fields), 8)
        self.assertIn('id', field_names)
        self.assertIn('name', field_names)
        self.assertIn('description', field_names)
        self.assertIn('latitude', field_names)
        self.assertIn('longitude', field_names)
        self.assertIn('rent_min', field_names)
        self.assertIn('rent_max', field_names)
        self.assertIn('avg_rating', field_names)
        self.assertIn('reviews_no', field_names)
        self.assertIn('university', field_names)

    def test_create_model_options(self):
        model = self.migration_instance.operations[0].model_name
        unique_together = apps.get_model('dorm_detective_app', model)._meta.unique_together
        self.assertEqual(len(unique_together), 1)
        self.assertEqual(unique_together[0], ('university', 'name'))

    def test_create_model_field_types(self):
        model = self.migration_instance.operations[0].model_name
        fields = apps.get_model('dorm_detective_app', model)._meta.fields
        self.assertIsInstance(fields[0], models.AutoField)
        self.assertIsInstance(fields[1], models.CharField)
        self.assertIsInstance(fields[2], models.CharField)
        self.assertIsInstance(fields[3], models.DecimalField)
        self.assertIsInstance(fields[4], models.DecimalField)
        self.assertIsInstance(fields[5], models.DecimalField)
        self.assertIsInstance(fields[6], models.DecimalField)
        self.assertIsInstance(fields[7], models.IntegerField)

    def test_create_model_validators(self):
        model = self.migration_instance.operations[0].model_name
        fields = apps.get_model('dorm_detective_app', model)._meta.fields
        for field in fields:
            if field.validators:
                for validator in field.validators:
                    self.assertIsInstance(validator, django.core.validators.BaseValidator)

    def test_create_model_fk(self):
        model = self.migration_instance.operations[0].model_name
        fields = apps.get_model('dorm_detective_app', model)._meta.fields
        self.assertIsInstance(fields[-1], models.ForeignKey)
        self.assertEqual(fields[-1].remote_field.model.__name__, 'University')

    def test_create_model_field_null(self):
        model = self.migration_instance.operations[0].model_name
        fields = apps.get_model('dorm_detective_app', model)._meta.fields
        self.assertTrue(fields[5].null)
        self.assertTrue(fields[6].null)
        self.assertTrue(fields[7].null)
                            

class AccommodationModelTest(TestCase):
    
    def setUp(self):
        self.university = University.objects.create(name='Test University')
    
    def test_name_max_length(self):
        name = 'a' * 129
        accommodation = Accommodation(name=name, university=self.university)
        with self.assertRaises(ValidationError):
            accommodation.full_clean()
    
    def test_name_unique_together_with_university(self):
        name = 'Test Accommodation'
        Accommodation.objects.create(name=name, university=self.university)
        accommodation = Accommodation(name=name, university=self.university)
        with self.assertRaises(ValidationError):
            accommodation.full_clean()
