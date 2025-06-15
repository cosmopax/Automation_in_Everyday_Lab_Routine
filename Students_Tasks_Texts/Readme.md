# Automation in Everyday Lab Routine: Course Repository

Welcome to the official GitHub repository for the "Applied Programming in the Lab" practical course. This repository is the central hub for all programming tasks, essential resources, and code submissions. Your journey into the realm of digital lab assistance begins here.

---

## I. Course Vision & Objective

In the contemporary scientific landscape, proficiency in programming has transcended its status as a niche skill, evolving into a fundamental component of effective laboratory practice. The systematic automation of experimental protocols, the precise acquisition of empirical data, and the subsequent sophisticated analysis of results are increasingly predicated upon the ability to script and meticulously control instrumentation. This segment of the practical course is meticulously designed to impart these essential programming skills, guiding you through the process of constructing integral components of a cutting-edge digital lab assistant.

[cite_start]This course is intrinsically linked to the broader vision of the **Omni-Lab Assistant**, an ambitious concept for a powerful, accessible, and open-source AI companion engineered to revolutionize workflows in biological and organic chemistry laboratories. [cite_start]The modules and tasks you undertake in this course are foundational elements of this grander design, contributing directly to the realization of a seamless, hands-free lab experience.

---

## II. Repository Structure

This repository is organized to provide all the materials necessary for your programming coursework:

* **`README.md` (This File):** Provides overarching guidelines, essential setup instructions, and critical information for navigating the course.
* **`setup_environment.sh`:** A comprehensive script designed to automate the installation of all necessary system tools, libraries, and foundational AI models for both macOS and Ubuntu.
* **`Student_Lab_Automation_Tasks.md`:** A detailed compendium outlining all programming assignments, categorized by complexity.
* **`Lab_Automation_Tasks.csv`:** A machine-readable version of the tasks, useful for programmatic access or quick overview.
* **`chemical_data_fetcher.py`:** An illustrative Python script serving as a foundational example for chemical data retrieval, demonstrating key concepts and libraries used in the course.


###
* **`core/`, `services/`, `utils/`, `tests/`, `docs/`, `data/sops/`:** Core directories for the modular Omni-Lab Assistant architecture that your projects will contribute to.
* **`prompting_database/`:** A dedicated directory for advanced prompt engineering contributions (see Section VI).

---

## III. Getting Started: Your Foolproof Setup Guide

To ensure a smooth and productive learning experience, meticulously follow these steps to set up your local development environment.

### Prerequisites

Before you begin, ensure you have:
* An active internet connection.
* Administrator privileges on your machine (necessary for system-level software installations).
* A **GitHub Account**. If you don't have one, create it now at [https://github.com/join](https://github.com/join).
* A **GitHub Personal Access Token (PAT)**. This is crucial for securely pushing your code to the repository without using your password every time.
    1.  Go to GitHub -> `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`.
    2.  Click `Generate new token (classic)`.
    3.  Give it a descriptive name (e.g., "LabAutomationCourse").
    4.  Set an expiration date (e.g., 90 days or longer for the duration of the course).
    5.  Grant it **`repo`** scope (full control of private repositories).
    6.  Click `Generate token`. **Copy the token immediately! You won't see it again.** Store it securely.

### 1. Install Git & A Code Editor

**Git** is indispensable for version control and interacting with GitHub.
**A Code Editor** is essential for writing and managing your scripts.

**For macOS (using Homebrew):**
```bash
/bin/bash -c "$(curl -fsSL [https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh](https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh))"
brew install git
For Ubuntu/Linux:
Bash

sudo apt update
sudo apt install -y git
Recommended Code Editor: We strongly recommend Visual Studio Code (VS Code) due to its versatility, extensive extensions for Python and Git, and user-friendly interface. Download and install it from https://code.visualstudio.com/download.
	•	As a Fallback: If you encounter issues with VS Code or prefer a simpler approach, you can use built-in text editors like nano (command-line), TextEdit (macOS), or gedit (Ubuntu). However, for programming, VS Code is highly advantageous.
2. Clone the Repository
First, clone this repository to your local machine. This command will download the entire project structure, including all subfolders and files, into a new directory named Automation_in_Everyday_Lab_Routine in your current terminal location.
Bash

git clone [https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine.git](https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine.git)
cd Automation_in_Everyday_Lab_Routine
(Note for the curious: You might have heard about issues with downloading repositories containing folders. This concern typically arises when trying to download individual subfolders via web interfaces, not when using git clone. Git is designed to handle hierarchical folder structures seamlessly, so you're good to go!)
3. Run the Setup Script
A robust setup_environment.sh script is provided to install all necessary system tools and Python libraries. It is meticulously designed for cross-platform compatibility with macOS (using Homebrew) and Ubuntu (using APT).
This script will:
	•	Install or update essential system-level dependencies required for various programming tasks, including tools for cheminformatics, image processing, and text recognition.
	•	Create a dedicated Python virtual environment (venv) within the project directory. This isolates all project dependencies, preventing conflicts with other Python projects on your system.
	•	Install all required Python packages into this virtual environment, as specified in requirements.txt.
	•	Compile OSRA (Optical Structure Recognition Application) from source, which is a crucial tool for chemical structure recognition from images. This process can be time-consuming, so please be patient.
Run the script from the root of your cloned repository:
Bash

bash setup_environment.sh
	•	Heads up for Linux users: This script will prompt you for your sudo password to install system packages via apt.
	•	Heads up for macOS users: Ensure Homebrew is installed. The script will guide you if it's missing.
Upon successful completion, you will see a venv directory created within your project.
4. Configure Your OpenAI API Key (CRITICAL!)
The MeSciA core orchestrator relies on a Large Language Model (LLM) service. For this course, we will use OpenAI's models via their API. The assistant will not function without your personal OpenAI API key.
Follow these steps precisely:
	1	Navigate to the project directory:Bash  cd ~/Automation_in_Everyday_Lab_Routine # Or wherever you cloned it
	2	   
	3	Copy the example environment file to a new .env file:Bash  cp .env.example .env
	4	   
	5	Open the new .env file with a text editor (e.g., nano or VS Code):Bash  nano .env
	6	# OR if using VS Code:
	7	# code .env
	8	   
	9	Edit the file: Replace sk-... with your actual OpenAI API key.# OpenAI API Key for LLM service
	10	OPENAI_API_KEY="sk-YOUR_ACTUAL_API_KEY_HERE"
	11	   
	12	Save and Exit:
	◦	For nano: Press Ctrl + X, then Y, then Enter.
	◦	For VS Code: Press Ctrl + S (or Cmd + S on macOS), then close the file.
5. Activate the Python Virtual Environment
Before you start working on any task or running any script, you must activate the virtual environment. This ensures you are using the correct Python interpreter and libraries installed by the setup_environment.sh script.
Bash

source venv/bin/activate
Your terminal prompt should now be prefixed with (venv), indicating the environment is active. To exit the environment when you are done, simply type:
Bash

deactivate#


6. Try the Example Script: chemical_data_fetcher.py
This script demonstrates basic chemical data retrieval from PubChem and local file generation. It's a great way to verify your setup.
First, ensure your virtual environment is active (you should see (venv) in your prompt).
Bash

# Ensure you are in the project root directory
cd ~/Automation_in_Everyday_Lab_Routine

# Run the script
python chemical_data_fetcher.py
The script will prompt you to enter a "Compound name or CAS". Try typing:
	•	caffeine
	•	aspirin
	•	ethanol
	•	2C-B (note the custom override for this compound mentioned in the script, relevant for medicinal neurochemistry interests)
The script will:
	•	Fetch details from PubChem (molecular weight, formula, synonyms).
	•	Generate 3D PDB and MOL files in the ligands/ and chemdraw/ directories, respectively.
	•	Generate a 2D image (.png) of the structure in the images/ directory.
	•	Log the information to an Excel file (neurochem.xlsx).
Observe the output in your terminal and check the newly created directories (ligands, chemdraw, images) and the neurochem.xlsx file for the generated data. Press Ctrl + C or type exit to quit the script.

IV. Course Structure & Programming Tasks
This repository serves as the central hub for all programming assignments. The tasks are meticulously categorized into three distinct tiers based on their complexity and time commitment:
	•	Mini (M-Series): Short, focused exercises designed to introduce a specific concept or library. These are excellent for building foundational skills.
	•	Medium (E-Series): More involved tasks that require the integration of several concepts to solve a practical lab-related problem, fostering a deeper understanding of system integration.
	•	Experiment (X-Series): Comprehensive projects that simulate a real-world lab automation challenge, demanding robust design, sophisticated implementation, and thorough documentation. These tasks represent significant contributions to the Omni-Lab Assistant's features.
You can find a detailed list of all programming assignments in Student_Lab_Automation_Tasks.md.
Coursework Requirements
Adherence to best coding practices is paramount:
	•	Clean Code: Write readable, well-organized, and self-documenting code.
	•	Add Comments: Eloquently explain complex parts of your code, outlining the functionality of your functions and critical logic.
	•	Modular Structure: Design your scripts and functions with reusability and modularity in mind.
Project Work:
	•	Group Project: Each student group is required to successfully complete one programming task designated as an 'Experiment' length project. This project will form a significant part of your practical assessment.
	•	Individual & Pair Assignments (Substitutive): As an alternative to answering the theoretical questions associated with one of the practical, hands-on experiments, you may opt to complete programming tasks. The requirements are as follows:
	◦	Individuals: May complete one or two 'Mini' tasks. The precise number will be determined in consultation with the course instructor, contingent upon the number of questions being substituted and the complexity of the chosen task(s).
	◦	Pairs: May complete one or two 'Medium' tasks under the same substitutive conditions.
Proposing Your Own Project: Students are enthusiastically encouraged to propose their own programming projects. These proposals will be rigorously evaluated for their relevance to the course's core themes of automation and their suitability in scope. Please discuss your innovative idea with the instructor before commencing development.

V. Code Submission Workflow: A Foolproof GitHub Guide
It is mandatory for all students to submit their completed scripts via this GitHub repository. This practice not only ensures proper version control and facilitates grading but also fosters a shared repository of knowledge from which all participants can learn. Follow this workflow meticulously.
Step 1: Create Your Personal Folder
To avoid file conflicts and maintain an organized repository, each student or group must create a personal folder at the root of the repository.
	•	For individuals: Use the format lastname_firstname_ss_25 (e.g., Huber_Anna_ss_25).
	•	For groups: Use the format group_X_project_name_ss_25 (e.g., group_3_safety_copilot_ss_25).
Command to create your folder (replace with your actual name/group):
Bash

# Ensure you are in the Automation_in_Everyday_Lab_Routine directory
cd ~/Automation_in_Everyday_Lab_Routine 

# Create your personal folder
mkdir your_lastname_your_firstname_ss_25 
# Example: mkdir Huber_Anna_ss_25
Step 2: Create Your Personal README.md within Your Folder
Inside your newly created personal folder, you must include a README.md file. This file will:
	•	Provide an overview of the scripts you have submitted for the course.
	•	Explain how to run your scripts.
	•	List any specific dependencies your scripts might have beyond those installed by setup_environment.sh.
	•	Include any additional information or reflections you deem relevant to your work.
	•	For prompt engineering contributions (see Section VI), list the filenames of your prompt templates here.
Command to create your personal README.md (replace with your actual folder name):
Bash

# Navigate into your personal folder
cd your_lastname_your_firstname_ss_25

# Create the README.md file (you can then edit it with your preferred code editor)
touch README.md
# Example: touch Huber_Anna_ss_25/README.md
Step 3: Naming Convention for Your Scripts
All scripts you submit must follow a clear and consistent naming convention to facilitate organization and review:
	•	For Programming Tasks: surname_firstname_task_number_own_title.fileending
	◦	Example: Huber_Anna_M1_ChemCalculator.py
	◦	Example: Schmidt_Max_E5_MolSimilaritySearch.py
	•	For Prompt Engineering Contributions: (See Section VI for detailed rules)
	◦	Example: Huber_Anna_DR_RetrosynthesisAgent_GPT4_Universal.md
Place all your code for a given task inside your personal folder.
Step 4: The Feature Branch Workflow (Your Submission Protocol)
Never commit your work directly to the main branch. Always work within a feature branch. This ensures proper version control, facilitates feedback, and prevents conflicts.
	1	Pull Latest Changes: Before starting any new work, always ensure your local repository is up-to-date with the main branch of the origin repository. This prevents merge conflicts. Bash  # Ensure you are in the root directory of the cloned repository
	2	cd ~/Automation_in_Everyday_Lab_Routine 
	3	git pull origin main
	4	   
	5	Create a New Branch: Create a new branch for the task you are working on. Name it descriptively, preferably following a task_category.task_id_lastname_firstname pattern. Bash  # Syntax: git checkout -b <branch-name>
	6	git checkout -b task_M1_Huber_Anna
	7	# Example for a Medium task: git checkout -b task_E1_Schmidt_Max
	8	# Example for an Experiment task: git checkout -b task_X1_Group3_SafetyCoPilot
	9	   
	10	Work on Your Task: Write your code, save your files within your personal folder, and thoroughly test your script.
	11	Add and Commit Your Changes: Stage your changes and commit them with a meaningful and descriptive message. Use the "feat:" prefix for new features, or "fix:" for bug fixes. Bash  # Add all changes within your personal folder
	12	git add your_lastname_your_firstname_ss_25/
	13	# Example: git add Huber_Anna_ss_25/
	14	
	15	# Commit with a descriptive message
	16	# Syntax: git commit -m "type: Brief description of work"
	17	git commit -m "feat: Implement M1 Command-Line Chemist's Calculator"
	18	# Example: git commit -m "fix: Corrected error in E5 MolSimilaritySearch logic"
	19	   
	20	Push Your Branch to GitHub: Upload your local branch to the GitHub repository. Bash  # Syntax: git push origin <branch-name>
	21	git push origin task_M1_Huber_Anna
	22	# Replace `task_M1_Huber_Anna` with your actual branch name
	23	   
Step 5: Create a Pull Request (PR)
A Pull Request (PR) is the formal mechanism to submit your work for review and grading.
	1	Go to the repository page on GitHub: https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine
	2	You should observe a prominent yellow banner indicating your recently pushed branch. Click the "Compare & pull request" button next to your branch name.
	3	Give your PR a clear and concise title (e.g., "Submission: Task M1 - Command-Line Chemist's Calculator").
	4	In the description box, briefly explain your work, explicitly mention which task you completed (e.g., "Completed Mini Task M.1"), and include any relevant notes for the instructor.
	5	On the right-hand side, add @cosmopax as a Reviewer.
	6	Click "Create pull request".
Your work is now officially submitted for review. Any feedback, including grades, will be provided directly on the Pull Request page.

VI. Prompt Engineering Contributions: The prompting_database
For students interested in the emerging field of Large Language Model (LLM) prompt engineering, or as an alternative component of a programming task, you are invited to contribute to the prompting_database/ folder. This initiative recognizes the critical role of well-crafted prompts in shaping the behavior and performance of AI models.
Purpose: This directory is intended to host:
	•	Prompt Templates: Reusable structures for guiding LLMs to perform specific tasks.
	•	Custom Instructions: Detailed directives that define the persona or specific constraints for an LLM.
	•	System Prompts: Foundational instructions that establish the LLM's role and operational principles within a defined context.
Contribution as a Task: High-quality contributions to the prompting_database/ will be considered as part of your programming task assessment, or as a fraction thereof, depending on their complexity, utility, and originality. This offers a unique opportunity to engage with cutting-edge AI concepts directly.
Naming Convention for Prompt Files: To maintain organization, your prompt files must adhere to the following strict nomenclature:
surname_firstname_prompting_mode_function_goal_primary_targeted_model_or_universal.fileending
	•	surname_firstname: Your last name and first name (e.g., Huber_Anna).
	•	prompting_mode: One of the following, reflecting the primary objective/style:
	◦	DR (Deep Research): For prompts designed to elicit comprehensive, detailed, and thoroughly referenced information.
	◦	Automation (Automation): For prompts aimed at automating specific lab tasks, controlling tools, or generating scripts.
	◦	Agentic (Agentic Behavior): For prompts that enable an LLM to exhibit autonomous, multi-step problem-solving or tool-use capabilities.
	•	function_goal: A concise description of the prompt's purpose or the function it aims to achieve (e.g., RetrosynthesisAgent, SafetyCheck, DataCleaner).
	•	primary_targeted_model_or_universal: The specific LLM(s) the prompt is optimized for (e.g., GPT4, Gemma2, Mistral7B) or Universal if designed to be broadly applicable across various models.
	•	fileending: Use .md for Markdown or .txt for plain text.
Example Filenames:
	•	Huber_Anna_DR_MolecularProperties_GPT4_Universal.md
	•	Schmidt_Max_Automation_ELNEntryFormatter_Phi3Mini.txt
	•	Mayer_Lena_Agentic_ReactionPlanner_Mistral7B.md
Submission: Place your prompt files directly into the prompting_database/ folder within the main repository. Remember to list the filenames of your prompt contributions in your personal README.md file (in your surname_firstname_ss_25/ folder).

VII. Best Practices & Troubleshooting
Best Practices
	•	Continuous Commits: Commit your changes frequently with descriptive messages. This creates a clear history of your work and makes it easier to revert if something goes awry.
	•	Test Thoroughly: Before pushing your code and creating a Pull Request, run your scripts multiple times with various inputs to ensure they function as expected and handle edge cases gracefully.
	•	Ask for Help: Don't hesitate to reach out to the instructor or your peers if you're stuck. Collaboration and asking questions are key aspects of learning programming.
Troubleshooting Common Issues
	•	"Error: Could not connect to the orchestrator." (when running services/voice/interaction.py):
	◦	Cause: The FastAPI orchestrator server (core/orchestrator.py) is not running. The interaction.pyclient needs the server to be active to communicate with it.
	◦	Solution: Open a separate terminal window. In this new terminal, activate your virtual environment (source venv/bin/activate) and start the orchestrator first:Bash  uvicorn core.orchestrator:app --reload
	◦	    Keep this terminal running. Then, in your original terminal (with the venv active), run python services/voice/interaction.py.
	•	OSRA Compilation Errors:
	◦	Cause: OSRA compilation can be sensitive to missing build tools or specific library versions. The setup_environment.sh script attempts to install all known dependencies.
	◦	Solution:
	▪	Ensure your system's package manager (Homebrew on macOS, APT on Ubuntu) is updated: brew update or sudo apt update.
	▪	Check the error messages in your terminal very carefully. They often point to a specific missing package or a configuration issue. You might need to manually install a dependency that the script missed for your specific system configuration.
	▪	Ensure graphicsmagick, potrace, netpbm are correctly installed and discoverable by OSRA's configure script.
	•	Python Package Installation Errors (pip install -r requirements.txt fails):
	◦	Cause: Network issues, corrupted packages, or missing system libraries required by a Python package's compilation process (e.g., PyAudio often needs portaudio development headers).
	◦	Solution:
	▪	Verify your internet connection.
	▪	Clear pip's cache: pip cache purge.
	▪	Ensure all system dependencies listed in the setup_environment.sh section were installed correctly. For PyAudio, specifically check portaudio (brew install portaudio on macOS, sudo apt install portaudio19-dev on Ubuntu).
	▪	Try installing packages individually to pinpoint the problematic one: pip install <package_name>.
	•	ModuleNotFoundError: No module named 'X':
	◦	Cause: You are not in the correct Python virtual environment, or the required package failed to install.
	◦	Solution: Ensure you have activated your venv by running source venv/bin/activate. If the problem persists, try reinstalling the missing package: pip install <missing_module_name>.

VIII. Recommended Learning Resources
For those less versed in programming, or simply seeking to deepen their understanding, the following resources are highly recommended:
General Programming & Python Basics
	•	Python Official Tutorial: The foundational guide to Python. Start with the basics of syntax, data types, and control flow.
	◦	https://docs.python.org/3/tutorial/
	•	Automate the Boring Stuff with Python: A practical, beginner-friendly book that focuses on real-world automation tasks. Excellent for building foundational scripting skills.
	◦	https://automatetheboringstuff.com/
Git & GitHub
	•	Git Handbook (GitHub Guides): A clear and concise introduction to Git concepts and commands.
	◦	https://guides.github.com/introduction/git-handbook/
	•	Learn Git Branching: An interactive tutorial to master Git branching, which is crucial for the Pull Request workflow.
	◦	https://learngitbranching.js.org/
Chemical & Biological Informatics Libraries
	•	RDKit Documentation: The official documentation for the RDKit cheminformatics toolkit. Essential for chemical structure manipulation and property calculations.
	◦	https://rdkit.readthedocs.io/en/latest/ 
	•	Biopython Tutorial: Learn how to work with DNA, RNA, and protein sequences, access biological databases, and perform common bioinformatics tasks.
	◦	https://biopython.org/docs/latest/Tutorial/index.html
	•	PubChemPy Documentation: Guide for interacting with the PubChem database.
	◦	https://pubchempy.readthedocs.io/en/latest/
Machine Learning & AI Fundamentals (Optional Deep Dive)
	•	Hugging Face transformers Library Documentation: If you delve into LLM fine-tuning, this is the go-to resource.
	◦	https://huggingface.co/docs/transformers/index
	•	"The Illustrated Transformer" by Jay Alammar: A beautifully visual explanation of the Transformer architecture, fundamental to modern LLMs.
	◦	http://jalammar.github.io/illustrated-transformer/

Enjoy the course, and let's automate the lab together!
