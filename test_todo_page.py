from .pages.todo_page import TodoPage
import time


def test_add_tasks_mark_them_and_check_marks(browser):
    link = "https://todomvc.com/examples/react/#/"
    pg = TodoPage(browser, link)
    pg.open()
    pg.prepare_test_data(["a", "b", "c"], ["b"])
    # 2 seconds delays for visual review
    time.sleep(2)

    pg.create_tasks()
    # should_*() methods created for testing, leave it empty or add some list values for test check
    pg.should_be_created_tasks()
    time.sleep(2)

    pg.mark_next_tasks()
    time.sleep(2)

    pg.should_be_active_tasks()
    time.sleep(2)

    pg.should_be_completed_tasks()
    time.sleep(2)
