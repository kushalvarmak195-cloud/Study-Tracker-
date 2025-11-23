# Project Statement

## Problem Statement
Students and self-learners often struggle to manage their study time effectively across multiple subjects. Without a clear record of how much time is dedicated to specific topics, it is difficult to identify imbalances in study habits, leading to over-studying some areas while neglecting others. A simple, distraction-free tool is needed to quantify effort and provide immediate feedback on time allocation.

## Scope of the Project
The Simple Study Tracker is a command-line utility designed for quick data entry and immediate summarization during a single user session.
* **In Scope:**
    * Text-based user interface for navigation.
    * In-memory storage of study sessions (lists and dictionaries).
    * Logic to aggregate time based on subject names.
    * Input validation to ensure data integrity (preventing crashes from invalid numbers).
* **Out of Scope:**
    * Persistent storage (saving data to a database or file after the program closes).
    * Graphical User Interface (GUI).
    * Date-specific tracking (calendars or timestamps).

## Target Users
* **University/College Students:** Who need to balance study time across different semester courses.
* **Self-Learners:** Individuals learning new skills (e.g., coding, languages) who want to track their dedication.
* **Exam Candidates:** Students preparing for competitive exams requiring strict time management per section.

## High-Level Features
1.  **Session Recording:** Allows the user to input a subject name and a specific duration in minutes.
2.  **Smart Aggregation:** Automatically groups sessions by subject and calculates the total time spent on each, regardless of how many separate sessions were logged.
3.  **Input Sanitization:** Handles user errors gracefully by rejecting non-numeric inputs for duration and normalizing subject names (e.g., capitalizing inputs).
4.  **Summary Dashboard:** Displays a clean, readable console table showing individual subject totals and the grand total of all study time.