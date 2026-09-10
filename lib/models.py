# Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, title):
        # Assign the title
        self.title = title
        # Set completed to False
        self.completed = False

    def complete(self):
        # Mark the task as complete
        self.completed = True
        # Print a confirmation message
        print(f"✅ Task '{self.title}' completed.")


# Define the User class
# Each user has a name and a list of tasks
# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name
        # Initialize an empty list of tasks
        self.tasks = []

    def add_task(self, task):
        # Add the task to the user's task list
        self.tasks.append(task)
        # Print a message confirming the task was added
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search for a task by its title in the user's task list
        for task in self.task:
        # Return the matching task or None
            if task.title == title:
                return task
        return None