import os
import sys

def main():
    print("=========================================")
    print("   Lab 4.0 Submission Setup Wizard       ")
    print("=========================================")
    print("Welcome to the Digital Lab. Let's set up your workspace.\n")

    # 1. Gather Info
    try:
        name = input("Enter your Full Name (e.g., Marie_Curie): ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            sys.exit(1)
        
        module = input("Enter your Module (e.g., M1, M2, Advanced): ").strip()
        if not module:
            module = "General"
            
        track = input("Enter your Track (e.g., Synthesis, Analytics, Automation): ").strip()
        if not track:
            track = "General"

    except KeyboardInterrupt:
        print("\nSetup cancelled.")
        sys.exit(0)

    # 2. Define Path
    # Target: students_deliverables/25WS/<Name>
    # Subfolders: group_protocols, individual_achievement
    base_dir = "students_deliverables"
    semester_dir = os.path.join(base_dir, "25WS")
    student_dir = os.path.join(semester_dir, name)
    
    group_protocols_dir = os.path.join(student_dir, "group_protocols")
    individual_achievement_dir = os.path.join(student_dir, "individual_achievement")

    # 3. Create Directories
    print(f"\nCreating workspace at: {student_dir}...")
    try:
        os.makedirs(group_protocols_dir, exist_ok=True)
        os.makedirs(individual_achievement_dir, exist_ok=True)
        
        # Create a placeholder README for the student
        readme_path = os.path.join(student_dir, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# Submission for {name}\n")
            f.write(f"**Module:** {module}\n")
            f.write(f"**Track:** {track}\n\n")
            f.write("## Folder Structure\n")
            f.write("- **group_protocols/**: Place your Exp 1-7 PDFs here.\n")
            f.write("- **individual_achievement/**: Place your Module 8 Capstone here.\n")
            
        print("✔ Folder structure created.")
        print("✔ Placeholder README.md created.")

    except Exception as e:
        print(f"Error creating directories: {e}")
        sys.exit(1)

    # 4. Final Instructions
    print("\n" + "="*40)
    print("           SETUP COMPLETE")
    print("="*40)
    print("To finalize your setup, execute the following commands in your terminal:\n")
    print(f"  git add {base_dir}")
    print(f"  git commit -m \"Setup submission folder for {name}\"")
    print("  git push origin main")
    print("\nGood luck with your experiments!")
    print("="*40)

if __name__ == "__main__":
    main()
