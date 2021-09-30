from .base_page import BasePage
from .locators import TodoPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TodoPage(BasePage):
    def create_task_list_and_mark_list(self, task_list, mark_tasks):
        self.task_list = task_list
        self.mark_tasks = mark_tasks
        self.active_tasks = [i for i in task_list if i not in mark_tasks]

    def create_tasks(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".new-todo"), "Can't find input for tasks"
        task_input = self.browser.find_element(By.CSS_SELECTOR, ".new-todo")
        task_input.click()
        tl_len = len(self.task_list)
        for i in range(tl_len):
            task_input.send_keys(self.task_list[i])
            task_input.send_keys(Keys.RETURN)

    def mark_next_tasks(self):
        mt_len = len(self.mark_tasks)
        for i in range(mt_len):
            task = self.browser.find_elements(By.XPATH, f"//*[label='{self.mark_tasks[i]}']/input[contains(@class,'toggle')]")
            assert task, f"There is no task {self.mark_tasks[i]}"
            task[0].click()

    def should_be_active_tasks(self):
        active_link = self.browser.find_element_by_link_text("Active")
        active_link.click()
        at_len = len(self.active_tasks)
        for i in range(at_len):
            check_at = self.is_element_present(By.CSS_SELECTOR, f".edit[value='{self.active_tasks[i]}']")
            assert check_at, f"Task {self.active_tasks[i]} should be active"

    def should_be_completed_tasks(self):
        complete_link = self.browser.find_element_by_link_text("Completed")
        complete_link.click()
        ct_len = len(self.mark_tasks)
        for i in range(ct_len):
            check_ct = self.is_element_present(By.CSS_SELECTOR, f".edit[value='{self.mark_tasks[i]}']")
            assert check_ct, f"Task {self.mark_tasks[i]} should be completed"
