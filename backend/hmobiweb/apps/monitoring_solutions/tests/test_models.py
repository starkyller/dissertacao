from django.test import TestCase

from apps.monitoring_solutions.models import (
    MonitoringCategory, SolutionObjective, Solution
)


class MonitoringCategoryTestCase(TestCase):
    def setUp(self):
        MonitoringCategory.objects.create(designation="XPTO")

    def test_properties(self):
        category = MonitoringCategory.objects.get(designation="XPTO")

        self.assertEqual(category.designation, "XPTO")
        self.assertEqual(category.__str__(), "XPTO")
        self.assertNotEqual(category.slug, None)

    def test_db_objects_numbers(self):
        # there should be 6 objects present

        obj_count = MonitoringCategory.objects.count()
        self.assertEqual(obj_count, 6)


class SolutionObjectiveTestCase(TestCase):
    def setUp(self):
        SolutionObjective.objects.create(designation="Train with Yoda")

    def test_properties(self):
        solutionObj = SolutionObjective.objects.get(
            designation="Train with Yoda")

        self.assertEqual(solutionObj.designation, "Train with Yoda")
        self.assertEqual(solutionObj.__str__(), "Train with Yoda")
        self.assertNotEqual(solutionObj.slug, None)

    def test_db_objects_numbers(self):
        # there should be 3 objects present

        obj_count = SolutionObjective.objects.count()
        self.assertEqual(obj_count, 3)


class SolutionTestCase(TestCase):
    def setUp(self):
        self._emptyString = ""

        self._monitoringCat = MonitoringCategory.objects.first()  # Health
        self._solutionObj = SolutionObjective.objects.first()  # Fall Detection
        self._name = "XPTO FALL"
        self._description = "The best description ever written"
        
        try:
            solution1 = Solution(
                name=self._name,
                description=self._description,
                category=self._monitoringCat,
                objective=self._solutionObj,
            )

            solution1.save()

        except:
            self.fail('Creation of Address object failed.')

    def test_properties(self):
        solutionObj = Solution.objects.first()

        self.assertEqual(solutionObj.__str__(), self._name)

        self.assertNotEqual(solutionObj.name, self._emptyString)
        self.assertEqual(solutionObj.name, self._name)

        self.assertNotEqual(solutionObj.description, self._emptyString)
        self.assertEqual(solutionObj.description, self._description)

        self.assertNotEqual(
            solutionObj.category.designation, self._emptyString)
        self.assertEqual(solutionObj.category.designation, "Health")

        self.assertNotEqual(
            solutionObj.objective.designation, self._emptyString)
        self.assertEqual(solutionObj.objective.designation, "Fall Detection")
