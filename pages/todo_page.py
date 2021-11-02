from selene.support.shared.jquery_style import s, ss
from selene import have
from selene import by


class TodoPage:

    def __init__(self):
        self.task_list = []
        self.mark_tasks = []
        self.active_tasks = []
        self.todo_items = ss("//div[@class='view']/label")

    def prepare_test_data(self, task_list, mark_tasks=[]):
        self.task_list = task_list
        self.mark_tasks = mark_tasks
        self.active_tasks = [i for i in task_list if i not in mark_tasks]

    def create_tasks(self):
        for i in range(len(self.task_list)):
            s(".new-todo").set_value(self.task_list[i]).press_enter()

    def mark_next_tasks(self):
        for i in range(len(self.mark_tasks)):
            s(f"//div[@class='view']/label[contains(text(), '{self.mark_tasks[i]}')]/preceding-sibling::input").click()

    def should_be_created_tasks(self):
        for i in range(len(self.task_list)):
            self.todo_items[i].should(have.text(self.task_list[i]))

    def should_be_active_tasks(self):
        s(by.link_text("Active")).click()
        for i in range(len(self.active_tasks)):
            self.todo_items[i].should(have.text(self.active_tasks[i]))

    def should_be_completed_tasks(self):
        s(by.link_text("Completed")).click()
        for i in range(len(self.mark_tasks)):
            self.todo_items[i].should(have.text(self.mark_tasks[i]))
