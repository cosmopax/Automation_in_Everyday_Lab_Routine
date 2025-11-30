# 02. Submission Guide

## 1. Who Submits? (Read Carefully)

### 🧪 Group Protocols (Experiments 1-7)
*   **Rule:** **ONLY ONE** student per group should submit the protocol.
*   **Action:** Designate a "Group Representative" to run the setup wizard and push the files.
*   **Naming:** The wizard will ask for ALL group members' names to include in the folder name.

### 🎓 Individual Capstone (Module 8)
*   **Rule:** **EVERY** student must submit their own folder.
*   **Action:** You are responsible for your own submission.

## 2. Initialize Your Workspace
We have provided a tool to set up your folder structure automatically.

1. Open your terminal in the repository root.
2. Run the setup wizard:
   ```bash
   python setup_submission.py
   ```
3. Follow the prompts to select **Group Protocol** or **Individual Capstone**.

This will create a directory in `students_deliverables/25WS/` with the correct naming convention.

## 2. Submitting Your Work

### Step 1: Add your files
Place your PDF reports or code into the appropriate subfolders.

### Step 2: Commit your changes
```bash
git add students_deliverables
git commit -m "Add report for Experiment X"
```

### Step 3: Push to GitHub
```bash
git push origin main
```

## 3. Verification
Go to your GitHub repository page and check that your files are visible in the `students_deliverables` folder.
