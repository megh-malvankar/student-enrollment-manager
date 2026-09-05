---
name: student-enrollment-manager
description: Skills and technologies demonstrated by the Student Enrollment Manager project.
---

# Student Enrollment Manager --- Skills

## Project Overview
A Python-based student enrollment management application that demonstrates student record management, Excel data handling, NumPy-based analysis, custom Python modules, and Groq API-powered Generative AI features.

## Core Skills

**1. Python**
* Core programming language used to build the application.
* Uses functions, classes, methods, dictionaries, loops, conditionals, and user input.
* Uses `if __name__ == "__main__":` as the application entry point.

**2. Object-Oriented Programming (OOP)**
* Implements the StudentManager class.
* Uses a constructor with `__init__()`.
* Organizes student operations into class methods.
* Uses an object instance to run the application.

**3. Pandas**
* Reads student records from Excel using `pandas.read_excel()`.
* Converts student records into a DataFrame.
* Writes updated records to Excel using `DataFrame.to_excel()`.

**4. NumPy**
* Converts program data into NumPy arrays.
* Uses `np.unique()` to calculate program-wise student counts.
* Supports basic enrollment data analysis.

**5. Excel Data Management**
* Uses `students_data.xlsx` for persistent student data storage.
* Loads existing records when the application starts.
* Saves changes after adding, updating, or deleting records.

**6. CRUD Operations**
* Create — Add student
* Read — View and search students
* Update — Modify student details
* Delete — Remove student records

**7. Generative AI**
* Integrates the Groq API with an LLM.
* Generates student-related insights from enrollment data.
* Provides scholarship suggestions, placement-readiness guidance, and improvement tips.

**8. API Integration**
* Uses the Groq Python client to communicate with an external AI API.
* Sends structured student information through an API request.
* Processes and displays the API response.

**9. Custom Python Modules**
* Separates AI functionality into `student_ai_utils.py`.
* Uses custom functions: `generate_ai_insights()`, `classify_students()`.
* Imports these functions into the main application.

**10. Data Validation**
* Checks for duplicate Student IDs before adding a record.
* Validates required student fields.
* Uses `.strip()` to clean user input.

**11. Exception Handling**
* Handles missing Excel files with `FileNotFoundError`.
* Handles Groq API exceptions.
* The final version can handle Excel `PermissionError` when the workbook is locked.

**12. Rule-Based Classification**
* Students are classified according to their enrolled program:
  * AI / ML → Eligible for Placement
  * Data-related programs → Eligible for Scholarship
  * Other programs → Needs Counselling

## Libraries and Tools

| Technology | Usage |
| :--- | :--- |
| **Python** | Application development |
| **Pandas** | Data processing and Excel operations |
| **NumPy** | Enrollment analysis |
| **OpenPyXL** | Excel file support |
| **Groq** | Generative AI API integration |
| **python-dotenv** | Environment variable management |

## Technical Concepts Demonstrated
Python Programming | Object-Oriented Programming | Data Structures | Dictionary-based data management | Excel Data Processing | Data Analysis | CRUD Operations | API Integration | Generative AI | Custom Python Modules | Input Validation | Exception Handling | Rule-Based Classification

## Security Best Practice
API credentials should be stored in a `.env` file rather than hard-coded in Python source code.

Example `.env` file:
```env
API_KEY=YOUR_GROQ_API_KEY
