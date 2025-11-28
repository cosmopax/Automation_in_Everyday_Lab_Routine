# Automation in Everyday Laboratory Routine (WS 25/26)

**MSc Chemistry | University of Vienna**

Welcome to the digital headquarters for your practical course. This repository hosts the software tools and submission system for the semester.

## 🏁 How to Submit Your Work (Step-by-Step)

If you have never used GitHub before, follow these instructions exactly.

### Step 1: Get the Repository
1.  Open your **Terminal** (Mac/Linux) or **Git Bash** (Windows).
2.  Copy and paste this command to download the course files:
    \`\`\`bash
    git clone https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine.git
    \`\`\`
3.  Enter the folder:
    \`\`\`bash
    cd Automation_in_Everyday_Lab_Routine
    \`\`\`

### Step 2: Create Your Folder
Do not create folders manually. Use our setup wizard to avoid naming errors.
1.  In the same terminal, run:
    \`\`\`bash
    python3 setup_submission.py
    \`\`\`
2.  Follow the prompts (Enter your Name, Track, etc.).
3.  The script will create a specific folder for you inside \`students_deliverables/\`.

### Step 3: Add Your Files
1.  Open the repository folder on your computer (in Finder or Explorer).
2.  Navigate to \`students_deliverables\` -> \`25WS\` -> \`[group_protocols OR individual_achievement]\`.
3.  Find **your** folder (created in Step 2).
4.  Paste your PDF Protocol or Python Code inside that folder.

### Step 4: Submit (Push)
Go back to your terminal and run these three commands:
\`\`\`bash
git add .
git commit -m "My Submission"
git push origin main
\`\`\`

---

## 📂 Repository Structure

* **\`setup_submission.py\`**: The tool you run in Step 2.
* **\`docs/\`**: Detailed guides if you get stuck.
* **\`students_deliverables/\`**: Where your work lives.

---
*Need Help? Check the \`docs/\` folder or ask a TA.*
