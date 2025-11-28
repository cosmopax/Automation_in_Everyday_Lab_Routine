#!/usr/bin/env python3
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✅ Created: {path}")
        return True
    except Exception as e:
        print(f"❌ Error creating {path}: {e}")
        return False

def create_readme(path, name, title, track):
    content = f"""# {title}
**Student:** {name}
**Track:** {track}
**Semester:** WS 25/26

## Project Abstract
[Replace this text with a brief description of your work]
"""
    try:
        with open(os.path.join(path, "README.md"), "w") as f:
            f.write(content)
        print(f"✅ Created: README.md inside project folder")
    except Exception as e:
        print(f"❌ Error creating README: {e}")

def main():
    clear_screen()
    print("==================================================")
    print("   AUTOMATION LAB: SUBMISSION SETUP WIZARD")
    print("==================================================")
    
    last_name = input("Enter your Last Name (e.g., Schimpl): ").strip()
    first_name = input("Enter your First Name (e.g., Patrick): ").strip()
    
    print("\nSelect your Module:")
    print("1. Group Protocol (Exp 1-7)")
    print("2. Individual Capstone (Module 8)")
    mode = input("Selection [1/2]: ").strip()

    base_path = "students_deliverables/25WS"
    
    if mode == "1":
        print("\n--- Group Protocol Setup ---")
        partners = input("Enter Last Names of ALL group members (comma separated): ").strip()
        folder_name = f"25WS_Protocol_{last_name}_{first_name}_Group"
        target_dir = os.path.join(base_path, "group_protocols", folder_name)
        track_name = "Group Protocol"
        project_title = "Lab Journal Exp 1-7"
        
    elif mode == "2":
        print("\n--- Capstone Project Setup ---")
        print("A - Code | B - System Design | C - Theory")
        track = input("Track [A/B/C]: ").upper().strip()
        title = input("Project Title (No spaces): ").strip()
        track_map = {'A': 'OptionA', 'B': 'OptionB', 'C': 'OptionC'}
        
        if track in track_map:
            folder_name = f"25WS_{last_name}_{first_name}_{track_map[track]}_{title}"
            target_dir = os.path.join(base_path, "individual_achievement", folder_name)
            track_name = f"Capstone Track {track}"
            project_title = title
        else:
            print("Invalid Track.")
            return

    print(f"\nCreating Folder: {target_dir}")
    if input("Proceed? [y/n]: ").lower() == 'y':
        if create_folder(target_dir):
            create_readme(target_dir, f"{first_name} {last_name}", project_title, track_name)
            print("\n🎉 SUCCESS! Your folder is ready.")
            print(f"👉 Move your files into: {target_dir}")
            print("👉 Then use 'git add', 'git commit', 'git push'.")

if __name__ == "__main__":
    main()
