# 02. Submission Guide

## 1. Initialize Your Workspace
We have provided a tool to set up your folder structure automatically.

1. Open your terminal in the repository root.
2. Run the setup wizard:
   ```bash
   python setup_submission.py
   ```
3. Enter your **Name**, **Module**, and **Track** when prompted.

This will create a directory at `students_deliverables/25WS/<Your_Name>` with the following subfolders:
- `group_protocols/`: For your Experiment 1-7 PDFs.
- `individual_achievement/`: For your Module 8 Capstone project.

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
