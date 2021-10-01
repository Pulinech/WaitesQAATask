from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class TodoPage(BasePage):
    def prepare_test_data(self, task_list, mark_tasks=[], delay=0):
        self.task_list = task_list
        self.mark_tasks = mark_tasks
        self.active_tasks = [i for i in task_list if i not in mark_tasks]
        self.delay = delay

    def create_tasks(self):
        time.sleep(self.delay)
        task_input = self.is_element_present(By.CSS_SELECTOR, ".new-todo")
        assert task_input, "Can't find input for tasks"
        task_input.click()
        tl_len = len(self.task_list)
        for i in range(tl_len):
            task_input.send_keys(self.task_list[i])
            task_input.send_keys(Keys.RETURN)
        time.sleep(self.delay)

    def mark_next_tasks(self):
        mt_len = len(self.mark_tasks)
        for i in range(mt_len):
            task = self.is_element_present(By.XPATH,
                                           f"//*[label='{self.mark_tasks[i]}']/input[contains(@class,'toggle')]")
            assert task, f"There is no task '{self.mark_tasks[i]}' to mark it"
            task.click()
        time.sleep(self.delay)

    def should_be_created_tasks(self, task_list=[]):
        if task_list:
            list = task_list
        else:
            list = self.task_list
        tl_len = len(list)
        for i in range(tl_len):
            assert self.is_element_present(By.CSS_SELECTOR, f".edit[value='{list[i]}']"), \
                f"Task '{list[i]}' should be created in todo list"
        time.sleep(self.delay)

    def should_be_active_tasks(self, active_tasks=[]):
        if active_tasks:
            list = active_tasks
        else:
            list = self.active_tasks
        active_link = self.browser.find_element_by_link_text("Active")
        active_link.click()
        at_len = len(list)
        for i in range(at_len):
            assert self.is_element_present(By.CSS_SELECTOR, f".edit[value='{list[i]}']"),\
                f"Task '{list[i]}' should be active"
        time.sleep(self.delay)

    def should_be_completed_tasks(self, mark_tasks=[]):
        if mark_tasks:
            list = mark_tasks
        else:
            list = self.mark_tasks
        complete_link = self.browser.find_element_by_link_text("Completed")
        complete_link.click()
        ct_len = len(list)
        for i in range(ct_len):
            assert self.is_element_present(By.CSS_SELECTOR, f".edit[value='{list[i]}']"),\
                f"Task '{list[i]}' should be completed"
        time.sleep(self.delay)
