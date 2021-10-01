from .pages.todo_page import TodoPage
import time


def test_add_tasks_mark_them_and_check_marks(browser):
    link = "https://todomvc.com/examples/react/#/"
    pg = TodoPage(browser, link)
    pg.open()
    # 2 seconds delays for visual review
    pg.prepare_test_data(["a", "b", "c"], ["b"], 2)
    pg.create_tasks()
    # should_be_*() methods created for testing, leave it empty or add some list values for test failure check
    pg.should_be_created_tasks()
    pg.mark_next_tasks()
    pg.should_be_active_tasks()
    pg.should_be_completed_tasks()
