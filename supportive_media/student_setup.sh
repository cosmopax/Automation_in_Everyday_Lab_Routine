#!/usr/bin/env bash
set -e

echo "=== Student project setup for 'Automation in Everyday Lab Routine' ==="
echo
echo "This script will:"
echo "  - clone your *fork* of the course repository,"
echo "  - create a correctly named project folder under courses_projects/<semester>/,"
echo "  - make an initial commit ready to push."
echo
echo "IMPORTANT:"
echo "  1) First, create a GitHub account and fork:"
echo "       https://github.com/cosmopax/Automation_in_Everyday_Lab_Routine"
echo "  2) Then run this script on your own machine (with git installed)."
echo

read -rp "Your GitHub username (the one that owns the fork): " GH_USER
if [ -z "${GH_USER}" ]; then
  echo "[ERROR] GitHub username cannot be empty."
  exit 1
fi

# Choose semester
echo
echo "Select your semester code:"
echo "  1) 25SS"
echo "  2) 25WS"
echo "  3) 26SS"
echo "  4) 26WS"
read -rp "Enter 1–4: " SEM_CHOICE

case "${SEM_CHOICE}" in
  1) SEM_CODE="25SS" ;;
  2) SEM_CODE="25WS" ;;
  3) SEM_CODE="26SS" ;;
  4) SEM_CODE="26WS" ;;
  *)
    echo "[ERROR] Invalid semester selection."
    exit 1
    ;;
esac

echo
read -rp "Your family name (Lastname): " LAST
read -rp "Your given name (Firstname): " FIRST
read -rp "Short project title (no slashes, can contain spaces): " TITLE

if [ -z "${LAST}" ] || [ -z "${FIRST}" ] || [ -z "${TITLE}" ]; then
  echo "[ERROR] Lastname, Firstname and Project title must all be non-empty."
  exit 1
fi

# Normalise: replace spaces in title with underscores
TITLE_SAFE=$(echo "${TITLE}" | tr ' ' '_' )
LAST_SAFE=$(echo "${LAST}" | tr ' ' '_' )
FIRST_SAFE=$(echo "${FIRST}" | tr ' ' '_' )

PROJECT_DIR_NAME="${SEM_CODE}_${LAST_SAFE}_${FIRST_SAFE}_${TITLE_SAFE}"

echo
echo "Your project folder will be named: ${PROJECT_DIR_NAME}"
echo

# Choose working directory
read -rp "Base directory to clone into (press Enter for ~/Desktop/projx): " BASE_DIR
if [ -z "${BASE_DIR}" ]; then
  BASE_DIR="${HOME}/Desktop/projx"
fi

mkdir -p "${BASE_DIR}"
cd "${BASE_DIR}"

REPO_DIR="Automation_in_Everyday_Lab_Routine"

if [ -d "${REPO_DIR}" ]; then
  echo "[INFO] Repository directory '${REPO_DIR}' already exists. Reusing it."
  cd "${REPO_DIR}"
  # Ensure we are on main and up to date with student's own fork
  git fetch origin || true
  git checkout main || git checkout -b main
  git pull --ff-only origin main || echo "[WARN] Could not fast-forward from origin/main; please check manually."
else
  echo "[INFO] Cloning your fork from GitHub (HTTPS) ..."
  echo "      URL: https://github.com/${GH_USER}/Automation_in_Everyday_Lab_Routine.git"
  echo
  echo "If prompted for username/password:"
  echo "  - Username: your GitHub username"
  echo "  - Password: a Personal Access Token (PAT) with 'repo' scope (NOT your normal password)"
  echo
  git clone "https://github.com/${GH_USER}/Automation_in_Everyday_Lab_Routine.git" "${REPO_DIR}"
  cd "${REPO_DIR}"
  git checkout main || git checkout -b main
fi

# Ensure semester folder exists
SEMESTER_PATH="courses_projects/${SEM_CODE}"
mkdir -p "${SEMESTER_PATH}"

TARGET_PATH="${SEMESTER_PATH}/${PROJECT_DIR_NAME}"

if [ -d "${TARGET_PATH}" ]; then
  echo "[INFO] Target project folder '${TARGET_PATH}' already exists."
else
  echo "[INFO] Creating project folder: ${TARGET_PATH}"
  mkdir -p "${TARGET_PATH}/src"
  # minimal README
  cat > "${TARGET_PATH}/README.md" <<EORD
# ${PROJECT_DIR_NAME}

Course: Automation in Everyday Lab Routine  
Semester: ${SEM_CODE}  

## Overview

Short summary of your project. Please describe:

- What problem you solve.
- Which experiment(s) (1–7) or lab context it relates to.
- How to run the code.

## How to run

Describe the commands required to run your code here, e.g.:

\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python src/main.py
\`\`\`
EORD
fi

echo
echo "[INFO] Adding and committing new/updated files ..."
git add "${SEMESTER_PATH}"

if git diff --cached --quiet; then
  echo "[INFO] No staged changes to commit (everything up to date)."
else
  git commit -m "Add or update student project folder ${PROJECT_DIR_NAME}" || {
    echo "[WARN] Commit failed (maybe no changes or commit hook)."
  }
fi

echo
echo "=== NEXT STEP (manual) ==="
echo "Run the following to push your changes to your fork:"
echo
echo "  cd \"${BASE_DIR}/${REPO_DIR}\""
echo "  git push origin main"
echo
echo "Git may ask you to log in. Use your GitHub username and a Personal Access Token (PAT)."
echo
echo "After pushing, open GitHub in the browser and create a Pull Request:"
echo "  - base: cosmopax/Automation_in_Everyday_Lab_Routine, branch: main"
echo "  - compare: ${GH_USER}/Automation_in_Everyday_Lab_Routine, branch: main"
echo
echo "Your folder '${PROJECT_DIR_NAME}' under courses_projects/${SEM_CODE}/ is your submission."
echo "======================================"
