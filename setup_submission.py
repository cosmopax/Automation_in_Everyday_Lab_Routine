import os
import sys

def main():
    print("=========================================")
    print("   Lab 4.0 Submission Setup Wizard       ")
    print("=========================================")
    print("Welcome to the Digital Lab.")
    print("This tool will set up your submission folder with the correct naming convention.\n")

    print("Select Submission Type:")
    print("1. Group Protocol (Experiments 1-7)")
    print("2. Individual Capstone (Module 8)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()

    base_dir = "students_deliverables"
    semester_dir = os.path.join(base_dir, "25WS")
    
    target_path = ""
    folder_name = ""

    if choice == "1":
        # --- GROUP PROTOCOL LOGIC ---
        print("\n" + "!"*50)
        print("⚠️  IMPORTANT: ONLY ONE GROUP MEMBER SHOULD PERFORM THIS SUBMISSION!")
        print("   Designate one representative to create and push this folder.")
        print("!"*50 + "\n")
        
        print("Enter the Last Names of ALL group members (separated by spaces):")
        names_input = input("> ").strip()
        if not names_input:
            print("Error: Names cannot be empty.")
            sys.exit(1)
            
        # Clean and format names
        names = [n.strip().capitalize() for n in names_input.split() if n.strip()]
        names_str = "_".join(names)
        
        # Naming: 25WS_Protocol_Name1_Name2_Name3_Group
        folder_name = f"25WS_Protocol_{names_str}_Group"
        target_path = os.path.join(semester_dir, "group_protocols", folder_name)
        
    elif choice == "2":
        # --- INDIVIDUAL CAPSTONE LOGIC ---
        print("\n--- Individual Capstone Setup ---")
        
        last_name = input("Enter your Last Name: ").strip().capitalize()
        first_name = input("Enter your First Name: ").strip().capitalize()
        
        if not last_name or not first_name:
            print("Error: Names cannot be empty.")
            sys.exit(1)
            
        print("\nSelect Track:")
        print("A. Code")
        print("B. System Design")
        print("C. Theory")
        track = input("Enter Option (A/B/C): ").strip().upper()
        if track not in ["A", "B", "C"]:
            print("Invalid track. Defaulting to 'X'.")
            track = "X"
            
        title = input("Enter a short Title for your work (No spaces, use_underscores): ").strip()
        if not title:
            title = "Project"
            
        # Naming: 25WS_LastName_FirstName_OptionX_Title
        folder_name = f"25WS_{last_name}_{first_name}_Option{track}_{title}"
        target_path = os.path.join(semester_dir, "individual_achievement", folder_name)
        
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    # --- EXECUTION ---
    print(f"\nCreating workspace at: {target_path}...")
    
    try:
        os.makedirs(target_path, exist_ok=True)
        
        # Create a placeholder README
        readme_path = os.path.join(target_path, "README.md")
        with open(readme_path, "w") as f:
            f.write(f"# Submission: {folder_name}\n\n")
            if choice == "1":
                f.write("## Group Protocol\n")
                f.write("Place your PDF report here.\n")
            else:
                f.write("## Individual Capstone\n")
                f.write("Place your code, design docs, or paper here.\n")
                
        print("✔ Folder structure created.")
        print("✔ Placeholder README.md created.")

    except Exception as e:
        print(f"Error creating directories: {e}")
        sys.exit(1)

    # --- FINAL INSTRUCTIONS ---
    print("\n" + "="*40)
    print("           SETUP COMPLETE")
    print("="*40)
    print("To finalize, execute the following commands:\n")
    print(f"  git add {base_dir}")
    print(f"  git commit -m \"Setup submission for {folder_name}\"")
    print("  git push origin main")
    print("\nGood luck!")
    print("="*40)

if __name__ == "__main__":
    main()
