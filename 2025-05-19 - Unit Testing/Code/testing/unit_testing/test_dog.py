from object_types.animals import Dog
from unittest import TestCase


class DogUnitTest(TestCase):

    def test_dog_init(self):
        dog = Dog("Luna", "Labrador")
        self.assertEqual("Luna", dog.name, "dog name is wrong")
        self.assertEqual("Labrador", dog.breed, "dog breed is wrong")
        self.assertEqual(100, dog.energy_level, "dog energy level is wrong")

    def test_walk(self):
        dog = Dog("Luna", "Labrador")
        self.assertEqual(100, dog.energy_level, "dog energy wrong")
        dog.walk(20)
        self.assertEqual(80, dog.energy_level, "dog energy wrong")
        dog.walk(120)
        self.assertEqual(80, dog.energy_level, "dog energy wrong")

    def test_rest(self):
        dog = Dog("Luna", "Labrador")
        self.assertEqual(100, dog.energy_level, "dog energy wrong")
        dog.rest(1)
        self.assertEqual(160, dog.energy_level, "dog energy wrong")
        dog.rest(2)
        self.assertEqual(280, dog.energy_level, "dog energy wrong")


