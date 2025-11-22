# 25WS – Programming Assignments

All programming assignments for the winter term 25WS are submitted via GitHub.

Your work will **not** go directly into the teacher’s repository.  
Instead, you get your own copy (“fork”), work there, and then submit a **Pull Request (PR)**.

---

## 1. Create a GitHub account

1. Go to **https://github.com**.
2. Click **Sign up**.
3. Choose:
   - a **username**,
   - an **email address**,
   - a **password**.
4. Confirm your email address (GitHub sends you a mail with a confirmation link).

---

## 2. Fork the course repository

1. Open the course repository in your browser:  
   `https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine`
2. Log in to your GitHub account (top-right).
3. At the top-right of the page, click **Fork**.
4. GitHub creates your own copy at:  
   `https://github.com/<your-username>/Automation_in_Everyday_Lab_Routine`

You now own this fork and can change it without needing permission.

---

## 3. Select the correct branch in your fork

1. In your fork, near the top-left you see a branch selector (often shows `main`).
2. Click it and choose **`course_scripts`**.
3. If you do **not** see `course_scripts`:
   - Click **Sync fork** (if GitHub offers this) to update your fork from the original repo.
   - Then try the branch selector again and choose `course_scripts`.

All work for this course must be done on **your `course_scripts` branch**.

---

## 4. Create your personal assignment folder

Folder structure convention:

`25WS/<Surname_Firstname>/<TaskName>/`

Examples:

- `25WS/Schimpl_Patrick/task1_hello_world/`
- `25WS/Schimpl_Patrick/task2_loops/`

### Steps (via the GitHub web interface)

1. Make sure you are in **your fork**, branch **`course_scripts`**.
2. Click **Add file → Create new file**.
3. In the file name field, type for example:  
   `25WS/Schimpl_Patrick/task1_hello_world/main.py`
   - GitHub will automatically create the missing folders
     (`25WS`, `Schimpl_Patrick`, `task1_hello_world`).
4. Paste your Python (or other) code into the large text area.
5. At the bottom:
   - Commit message: e.g. `Add task 1 solution`
   - Select **Commit directly to the course_scripts branch**.
   - Click **Commit changes**.

Repeat this to add more files to the same folder (e.g. input files, README, etc.).

---

## 5. Update your solution later

To improve or fix your code:

1. Open the file in your fork.
2. Click the **pencil (edit)** icon.
3. Change the code.
4. Scroll down, write a short commit message (e.g. `Fix bug in task 1`) and click **Commit changes**.

All changes are stored as a history of commits in your fork.

---

## 6. Submit your work as a Pull Request (PR)

When you are ready to hand in a task, you create a **Pull Request** from your fork to the teacher’s repository.

1. In your fork (`https://github.com/<your-username>/Automation_in_Everyday_Lab_Routine`),
   make sure branch `course_scripts` is selected.
2. Click the **Contribute** button (if visible) and then **Open pull request**,  
   or go to the **Pull requests** tab and click **New pull request**.
3. Set:
   - **base repository**: `cosmopax/Automation_in_Everyday_Lab_Routine`
   - **base branch**: `course_scripts`
   - **head repository**: `your-username/Automation_in_Everyday_Lab_Routine`
   - **compare branch**: `course_scripts`
4. GitHub shows a list of changed files.  
   You should only see files under:  
   `25WS/<Surname_Firstname>/…`
5. Click **Create pull request**.
6. Title suggestion:  
   `Task 1 – <Surname Firstname>`
7. In the description, write short instructions on how to run your code and anything special you want to mention.

This pull request is your official submission. The teacher can see your work, comment on it, and optionally merge it.

---

## 7. Updating after feedback

If you receive feedback and need to change something:

1. Go back to your fork and edit the files on branch `course_scripts` as before.
2. Commit your changes.
3. The existing pull request automatically updates with your new commits.  
   You do **not** need to create a new pull request for the same task.
