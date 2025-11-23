# Simple Study Tracker

## Overview of the Project
The **Simple Study Tracker** is a command-line application built in Python designed to help students and self-learners track their study sessions. The program allows users to log the subject they are studying and the duration of the session. It then processes this data to provide a real-time summary of total study time per subject, helping users visualize their productivity and time allocation.

## Features
* **Add Study Sessions:** Users can input a subject name and the duration of study in minutes.
* **Automatic Formatting:** Subject names are automatically capitalized (e.g., "math" becomes "Math") to ensure consistency.
* **Input Validation:** The system prevents errors by ensuring that the duration entered is a valid, positive whole number.
* **Summary View:** Displays a clean table showing the total aggregated time spent on each subject.
* **Grand Total:** Calculates the sum of all study time across all subjects.

## Technologies/Tools Used
* **Programming Language:** Python 3.x
* **Environment:** Any standard terminal or command prompt.

## Steps to Install & Run the Project

### Prerequisites
Ensure you have **Python 3** installed on your system. You can check this by running `python --version` in your terminal.

### Installation
1.  *Navigate to Target Directory:*
    Open the Command Prompt or PowerShell and navigate to the directory where you want the project folder to be created.
    bash
    cd Desktop
    

2.  *Clone the Repository:*
    Run the git clone command using the verified URL to download the entire project.
    bash
    git clone 

3.  *Navigate into the Project Folder:*
    bash
    cd Personal-Budget-Tracker-Project


### Running the Application
Run the script using the Python command:
```bash
python study_tracker.py

### Instructions for Testing
To verify the application is working correctly, follow these testing steps:

Launch the App: Run the script. You should see the "Main Menu".

Test Valid Input:

Choose option 1.

Enter subject: Math

Enter duration: 60

Result: Confirmation message should appear.

Test Data Aggregation:

Choose option 1 again.

Enter subject: math (lowercase).

Enter duration: 30

Result: The system should normalize this to "Math".

Test Error Handling:

Choose option 1.

Enter subject: History

Enter duration: abc (or a negative number).

Result: The program should display an error message and ask for the duration again.

Verify Summary:

Choose option 2.


Result: You should see "Math" with a total of 90 minutes (60+30) and "History" with its entered time.
