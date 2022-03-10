import unittest
from datetime import date

from assignment import Assignment
from task_list import TaskList


class TestAddTask(unittest.TestCase):
    def test_add_taks_in_task_list(self):
        task = Assignment('Learn Python')
        task_list = TaskList()

        task_list.add_task(task)
        self.assertIn(task, task_list.get_tasks())


class TestGetTasks(unittest.TestCase):
    def test_return_list_of_added_tasks(self):
        task = Assignment('Learn Python')
        task_2 = Assignment('Learn JavaScript')

        task_list = TaskList()

        task_list.add_task(task)
        task_list.add_task(task_2)

        self.assertEqual(task_list.get_tasks(), [task, task_2])


class TestGetLateTasks(unittest.TestCase):
    def test_get_late_task(self):
        dt_td = date.today()

        dt_1 = date(2022, 2, 14)
        dt_2 = date(2022, 3, 8)
        dt_3 = date(2022, 1, 3)
        dt_4 = date(2022, 12, 31)
        dt_5 = date(2022, 4, 28)

        task = Assignment('Learn Python', date=dt_1)
        task_2 = Assignment('Learn JavaScript', date=dt_2)
        task_3 = Assignment('Learn Node.JS', date=dt_3)
        task_4 = Assignment('Learn Ruby', date=dt_4)
        task_5 = Assignment('Learn Django', date=dt_5)

        task_list = TaskList()
        task_list.add_task(task)
        task_list.add_task(task_2)
        task_list.add_task(task_3)
        task_list.add_task(task_4)
        task_list.add_task(task_5)

        late_tasks = []

        for task in task_list.get_tasks():
            if dt_td > task.date:
                late_tasks.append(task)

        self.assertEqual(task_list.get_late_tasks(), late_tasks)


class TestGetTasksForDay(unittest.TestCase):
    def test_get_tasks_for_day(self):
        dt_td = date.today()

        dt_1 = date(2022, 2, 14)
        dt_2 = date(2022, 3, 8)
        dt_3 = date(2022, 1, 3)
        dt_4 = date(2022, 3, 8)
        dt_5 = date(2022, 4, 28)

        task = Assignment('Learn Python', date=dt_1)
        task_2 = Assignment('Learn JavaScript', date=dt_2)
        task_3 = Assignment('Learn Node.JS', date=dt_3)
        task_4 = Assignment('Learn Ruby', date=dt_4)
        task_5 = Assignment('Learn Django', date=dt_5)

        task_list = TaskList()
        task_list.add_task(task)
        task_list.add_task(task_2)
        task_list.add_task(task_3)
        task_list.add_task(task_4)
        task_list.add_task(task_5)

        day_tasks = []

        for task in task_list.get_tasks():
            if dt_td == task.date:
                day_tasks.append(task)

        self.assertEqual(task_list.get_tasks_for_today(), day_tasks)


unittest.main()
