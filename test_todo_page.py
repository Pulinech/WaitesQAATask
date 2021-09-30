from .pages.todo_page import TodoPage
import time


def test_add_tasks_mark_them_and_check_marks(browser):
    link = "https://todomvc.com/examples/react/#/"
    page = TodoPage(browser, link)
    page.open()
    page.create_task_list_and_mark_list(["a", "b", "c"],  ["b1"])
    page.create_tasks()
    time.sleep(2)
    page.mark_next_tasks()
    time.sleep(2)
    page.should_be_active_tasks()
    time.sleep(2)
    page.should_be_completed_tasks()
    time.sleep(2)
