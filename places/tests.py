from django.test import TestCase

from accounts.models import CustomUser
from places.models import Place


class PlacesTests(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create_user('user1')
        self.user2 = CustomUser.objects.create_user('user2')

    def test_user_can_create_place(self):
        place = Place.objects.create(
            author=self.user1,
            name='test',
            description='test place',
            latitude=43.98,
            longitude=78.679,
        )
        self.assertTrue(
            self.user1.places.get(pk=place.id),
            "User doesn't have created place"
        )

    def test_place_fields_correct(self):
        name = 'test place'
        description = 'test description'
        lat = 43.98
        lng = 78.679
        place = Place.objects.create(
            author=self.user1,
            name=name,
            description=description,
            latitude=lat,
            longitude=lng,
        )
        created_place = Place.objects.get(pk=place.id)
        self.assertEqual(
            name, created_place.name, "Name doesn't match"
        )
        self.assertEqual(
            description, created_place.description, "Description doesn't match"
        )
        self.assertEqual(
            lat, created_place.latitude, "Latitude doesn't match"
        )
        self.assertEqual(
            lng, created_place.longitude, "Longitude doesn't match"
        )

    def test_user_cannot_see_places_of_another_user(self):
        Place.objects.create(
            author=self.user1,
            name='test',
            description='test place',
            latitude=43.98,
            longitude=78.679,
        )
        self.assertNotEqual(
            self.user2.places,
            self.user1.places,
            "User can see another user's place"
        )

    def test_user_can_see_their_places(self):
        place = Place.objects.create(
            author=self.user1,
            name='test',
            description='test place',
            latitude=43.98,
            longitude=78.679,
        )

        self.assertIn(
            place,
            self.user1.places.all(),
            "User can't see their places"
        )

    def test_user_can_see_all_their_places(self):
        places_count = 5
        for _ in range(places_count):
            Place.objects.create(
                author=self.user1,
                name='test',
                description='test place',
                latitude=43.98,
                longitude=78.679,
            )
        self.assertEqual(
            self.user1.places.all().count(),
            places_count,
            "User doesn't see all places"
        )
