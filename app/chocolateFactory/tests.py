from django.test import TestCase
from .models import OompaLoompa
from .serializers import OompaLoompaCreateSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import json
# Create your tests here.


class ModelTestCase(TestCase):
    """This class test suite for the OompaLoompa model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.ompaLoompa = OompaLoompa(
            name="OompaLoompa10",
            age=35,
            job="Caramels",
            height=0.95,
            weight=35.25,
            description="ASD"
        )

    def testModelCreateOompaLoompa(self):
        """Test the OompaLoompa model can create a OompaLoompa."""

        old_count = OompaLoompa.objects.count()
        self.ompaLoompa.save()
        new_count = OompaLoompa.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCaseCreate(TestCase):
    """This class test suite for the OompaLoompa create."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.client = APIClient()
        self.ompaLoompa = {
            "name": "OompaLoompa10",
            "age": 35,
            "job": "Caramels",
            "height": 0.85,
            "weight": 35.25,
            "description": "ASD"
        }
        self.response = self.client.post(
            reverse('listCreate'),
            self.ompaLoompa,
            format="json"
        )

    def testApiCreateOompaLoompa(self):
        """Test the api has OompaLoompa creation capability."""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class ModelTestCaseDetails(TestCase):
    """This class test suite for the OompaLoompa details."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.ompa1 = OompaLoompa.objects.create(
            name="OompaLoompa1",
            age=35,
            job="Caramels",
            height=0.95,
            weight=35.25,
            description="ASD"
        )

    def testApiGetOompaLoompa(self):
        """Test the api can get a given OompaLoompa."""

        oompaLoompa = OompaLoompa.objects.get(id=self.ompa1.id)
        serializerData = OompaLoompaCreateSerializer(oompaLoompa)
        response = self.client.get(
            reverse('details', kwargs={'pk': self.ompa1.id}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializerData.data)


class ModelTestCaseUpdate(TestCase):
    """This class test suite for the OompaLoompa update."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.ompa1 = OompaLoompa.objects.create(
            name="OompaLoompa2",
            age=39,
            job="Chocolate",
            height=0.95,
            weight=37.25,
            description="ASD"
        )
        self.ompa1Mod = {
            'name': "OompaLoompa2",
            'age': 45,
            'job': "Chocolate",
            'height': 1.26,
            'weight': 37.25,
            'description': 'Chocolate Manager'
        }

    def testApiUpdateOompaLoompa(self):
        """Test the api can update a given OompaLoompa."""

        response = self.client.put(
            reverse('details', kwargs={'pk': self.ompa1.pk}),
            data=json.dumps(self.ompa1Mod),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ModelTestCaseDelete(TestCase):
    """This class test suite for the OompaLoompa delete."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.ompa1 = OompaLoompa.objects.create(
            name="OompaLoompa2",
            age=39,
            job="Chocolate",
            height=0.95,
            weight=37.25,
            description="ASD"
        )

    def testApiDeleteOompaLoompa(self):
        """Test the api can delete a OompaLoompa."""

        oompaLoompa = OompaLoompa.objects.get(id=self.ompa1.id)
        response = self.client.delete(
            reverse('details', kwargs={'pk': oompaLoompa.id}),
            format='json', follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
