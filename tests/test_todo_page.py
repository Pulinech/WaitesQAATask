from selene.support.shared import browser
from pages.todo_page import TodoPage

link = "https://todomvc.com/examples/react/#/"


def test_add_tasks_mark_them_and_check_marks():
    browser.open_url(link)
    pg = TodoPage()
    pg.prepare_test_data(["a", "b", "c"], ["b"])
    pg.create_tasks()
    pg.should_be_created_tasks()
    pg.mark_next_tasks()
    pg.should_be_active_tasks()
    pg.should_be_completed_tasks()
