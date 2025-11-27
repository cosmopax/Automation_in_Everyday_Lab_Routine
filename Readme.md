# Automation in Everyday Laboratory Routine (WS 25/26)

**MSc Chemistry | University of Vienna**

Welcome to the digital headquarters for your practical course. This repository hosts the software tools and submission system for the semester.

## 🏁 Getting Started (Zero Experience Required)

We use a simplified **Single-Branch Workflow**. You do not need to manage multiple branches.

1.  **[Phase 1: Setup & Forking](docs/01_Setup_and_Fork.md)**
    * *How to create an account and get your own copy of this repo.*
2.  **[Phase 2: Submission Guide](docs/02_Submission_Guide.md)**
    * *How to use the auto-setup tool and deliver your PDF/Code.*

---

## 🛠️ The "Zero-Friction" Setup Tool

To avoid naming errors, **do not create folders manually.**
We provide a Python wizard (\`setup_submission.py\`) that generates the strict folder structure required for grading.

**Usage:**
\`\`\`bash
# Inside your cloned repository
python3 setup_submission.py
\`\`\`
*Follow the on-screen prompts to set up your Group Protocol or Capstone Project folder.*

---

## 📂 Repository Structure

* **\`docs/\`**: Instructional guides for students.
* **\`students_deliverables/\`**: The submission archive.
    * \`25WS/group_protocols/\`: For Exp 1-7 PDFs.
    * \`25WS/individual_achievement/\`: For Module 8 Capstones.
* **\`setup_submission.py\`**: The automated folder generator.

---
*For technical issues, please open an Issue in this repository.*
