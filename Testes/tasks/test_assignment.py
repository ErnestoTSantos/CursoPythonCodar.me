import unittest
from datetime import date, datetime

from assignment import Assignment


class TestConclude(unittest.TestCase):
    def test_conclude_task_switch_conclude_for_true(self):
        task = Assignment('Learn Python')
        task.conclude()
        self.assertEqual(task.completed, True)

    def test_conclude_tasks_keeps_completed_true(self):
        task = Assignment('Learn Python')
        task.conclude()
        self.assertEqual(task.completed, True)
        task.conclude()
        self.assertEqual(task.completed, True)


class TestDescription(unittest.TestCase):
    def test_add_description(self):
        task = Assignment('Learn Python')
        task.add_description('Estamos aprendendo sobre testes com python, isso é incrível!')  # noqa:E501
        self.assertEqual(task.description, 'Estamos aprendendo sobre testes com python, isso é incrível!')  # noqa:E501


class TestDeferNotification(unittest.TestCase):
    def test_defer_notification_in_X_minutes(self):
        dt_original = datetime(2022, 3, 8, 9, 30)
        task = Assignment('Learn Python', date_notification=dt_original)
        task.defer_notification(20)

        dt_expected = datetime(2022, 3, 8, 9, 50)
        self.assertEqual(task.date_notification, dt_expected)


class TestLateTask(unittest.TestCase):
    def test_late_task(self):
        dt_1 = date(2022, 2, 14)
        dt_2 = date(2022, 7, 10)

        task = Assignment('Learn Python', date=dt_1)
        task_2 = Assignment('Learn JavaScript', date=dt_2)

        self.assertEqual(task.late(), True)
        self.assertEqual(task_2.late(), False)


unittest.main()
