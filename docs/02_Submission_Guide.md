# Phase 2: Delivering Your Work

We have automated the file organization for you. Follow these steps exactly to submit your work.

## Step 1: Clone YOUR Fork
1.  Open your terminal (or VS Code).
2.  Run this command (replace \`YOUR_USERNAME\` with your actual GitHub username):
    \`\`\`bash
    git clone https://github.com/YOUR_USERNAME/Automation_in_Everyday_Lab_Routine.git
    \`\`\`
3.  Enter the folder:
    \`\`\`bash
    cd Automation_in_Everyday_Lab_Routine
    \`\`\`

## Step 2: Run the Setup Wizard
Do not create folders manually. Use our tool to guarantee the correct naming convention.
Run:
\`\`\`bash
python3 setup_submission.py
\`\`\`
* **Follow the prompts:** Enter your Name, Module, and Track.
* **Result:** The script creates a correctly named folder inside \`students_deliverables/\`.

## Step 3: Add Your Work
1.  Locate the new folder created by the script (e.g., \`students_deliverables/25WS/group_protocols/...\`).
2.  **Paste** your PDF protocol or Python scripts into this folder.

## Step 4: Save and Push
Run these three commands to send your work to the cloud:
\`\`\`bash
git add .
git commit -m "Submission: [Your Name] Module [X]"
git push origin main
\`\`\`

## Step 5: Open a Pull Request (PR)
This notifies the instructors that your work is ready.
1.  Go to **your** repository on GitHub.com.
2.  You should see a yellow banner: *"This branch is 1 commit ahead..."*
3.  Click **Compare & pull request**.
4.  Title: "Submission: [Your Name]".
5.  Click **Create pull request**.

✅ **Done!** You have successfully delivered your work.
