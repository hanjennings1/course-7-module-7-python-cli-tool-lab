# Module Lab: Building a Python Command-Line Interface Tool
**Completed Sept 10, 2026** 

## Overview

This is a Python Command-Line Interface (CLI) tool for managing tasks assigned to users. It uses `argparse` to handle command-line commands and object-oriented classes (`Task` and `User`) to model the underlying data.

The tool supports two commands:

- `add-task` --> add a task to a user's task list
- `complete-task` --> mark one of a user's tasks as complete

## Project Structure

```
lib/
├── __init__.py
├── cli_tool.py     # CLI entry point and command logic
└── models.py       # Task and User classes
testing/
├── __init__.py
└── test_cli_tool.py
Pipfile
pytest.ini
README.md
```

## Setup

Clone the repository and install dependencies:

```bash
git clone <this-repo-url>
cd course-7-module-7-python-cli-tool-lab
pipenv install
pipenv shell
```

Confirm Python is installed:

```bash
python --version
```

## Usage

Run the CLI using Python's module flag from the project root:

### Add a task

```bash
python3 -m lib.cli_tool add-task Alice "Submit report"
```

Output:
```
📌 Task 'Submit report' added to Alice.
```

### Complete a task

```bash
python3 -m lib.cli_tool complete-task Alice "Submit report"
```

Output:
```
✅ Task 'Submit report' completed.
```

### Error handling

If the user doesn't exist:
```
❌ User not found.
```

If the task title doesn't match any of the user's tasks:
```
❌ Task not found.
```

### Help menu

Running the tool with no command shows usage help:

```bash
python3 -m lib.cli_tool
```

## Important Note on State

The `users` dictionary in `cli_tool.py` is stored **in memory only** — it is not saved to a file or database. This means:

- State is shared correctly *within a single script or process* (e.g., adding a task and then completing it in the same Python session).
- State is **not** shared between separate terminal commands. Running `add-task` and then `complete-task` as two individual CLI invocations will **not** work, because each command starts a fresh process with an empty `users` dictionary.

This is expected behavior for this version of the tool — it does not implement persistence (e.g., saving to a JSON file or database).

## Design

- **`Task`** (`lib/models.py`) - represents a single task with a `title` and `completed` status. Includes a `complete()` method that marks it done and prints a confirmation message.
- **`User`** (`lib/models.py`) — represents a user with a `name` and a list of `tasks`. Includes:
  - `add_task(task)` — adds a task to the user's list and prints a confirmation.
  - `get_task_by_title(title)` - searches the user's tasks by title and returns the matching `Task`, or `None` if not found.
- **CLI (`lib/cli_tool.py`)** - uses `argparse` with subparsers to route `add-task` and `complete-task` commands to their corresponding functions, which operate on the `Task`/`User` classes.

## Running Tests

Tests are located in `testing/test_cli_tool.py` and use `pytest`.

```bash
pipenv run pytest testing/test_cli_tool.py
```

Expected output:
```
2 passed
```

## Learning Goals Demonstrated

- Building modular, user-friendly CLI applications using `argparse`
- Applying object-oriented programming (OOP) to model real-world objects (`Task`, `User`)
- Validating input and providing clear terminal feedback
- Structuring a CLI project for maintainability (`lib/` and `testing/` separation)