def add_session(sessions):
    print("\n--- Add New Session ---")
    
    subject = input("Enter subject (e.g., Math, History, Python): ").strip()
    
    while True:
        try:
            # Duration is stored in minutes
            duration_str = input("Enter duration in minutes (e.g., 60): ").strip()
            duration = int(duration_str)
            if duration <= 0:
                print("Duration must be a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for the duration.")
            
    # Normalize subject input (capitalizing first letter for consistency)
    subject = subject.capitalize() 

    # Create the session dictionary
    new_session = {'subject': subject, 'duration': duration}
    sessions.append(new_session)
    
    print(f"\nSession added: {subject} for {duration} minutes.")


def view_summary(sessions):
    """Calculates and displays the total study time per subject."""
    if not sessions:
        print("\nNo study sessions recorded yet.")
        return

    # Dictionary to hold total duration for each subject
    summary = {}
    
    # Calculate totals
    for session in sessions:
        subject = session['subject']
        duration = session['duration']
        
        # If the subject is already in the summary, add the duration
        # Otherwise, start the count for that subject
        summary[subject] = summary.get(subject, 0) + duration

    print("\n--- Study Summary (in minutes) ---")
    print("-" * 35)
    
    # Display results
    total_study_time = 0
    for subject, total_duration in summary.items():
        print(f"{subject:<20}: {total_duration:>10} min")
        total_study_time += total_duration
        
    print("-" * 35)
    print(f"{'TOTAL TIME':<20}: {total_study_time:>10} min")


def main():
    # List to store all study sessions (in-memory data)
    study_sessions = []
    
    print("Welcome to the Simple Study Tracker!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Add New Study Session")
        print("2. View Study Summary")
        print("3. Exit Tracker")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            add_session(study_sessions)
        elif choice == '2':
            view_summary(study_sessions)
        elif choice == '3':
            print("\nThank you for using the Study Tracker. Keep up the great work!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()