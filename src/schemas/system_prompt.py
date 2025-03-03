from browser_use import Agent, SystemPrompt

class MySystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        existing_rules = super().important_rules()

        new_rules = """
        - ALWAYS CLICK ON BUTTONS HAVING THE TEXT SAME AS GIVEN IN THE TASK.
        - EACH URL MUST BE VALID AND HAVE CORRECT FORMAT.
        """
        return f'{existing_rules}\n{new_rules}'