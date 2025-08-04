import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import todo

def setup_function():
    # Clear task list before each test
    todo.tasks.clear()

def test_add_task():
    tasks = todo.add_task("Test Task")
    assert "Test Task" in tasks

def test_remove_task():
    todo.add_task("Temp Task")
    todo.remove_task(0)
    assert "Temp Task" not in todo.list_tasks()

def test_list_tasks_is_list():
    assert isinstance(todo.list_tasks(), list)

