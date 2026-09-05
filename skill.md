# Skills & Technologies

## Project

**Student Enrollment Manager**

A Python-based student enrollment management application that
demonstrates student record management, Excel data handling, NumPy-based
analysis, custom Python modules, and Groq API-powered Generative AI
features.

------------------------------------------------------------------------

## Core Skills

### 1. Python

-   Core programming language used to build the application.
-   Uses functions, classes, methods, dictionaries, loops, conditionals,
    and user input.
-   Uses `if __name__ == "__main__":` as the application entry point.

### 2. Object-Oriented Programming (OOP)

-   Implements a `StudentManager` class.
-   Uses a constructor with `__init__()`.
-   Organizes student operations into class methods.
-   Uses an object instance to run the application.

### 3. Pandas

-   Reads student records from Excel using `pandas.read_excel()`.
-   Converts student records into a DataFrame.
-   Writes updated records back to Excel using `DataFrame.to_excel()`.

### 4. NumPy

-   Converts program data into NumPy arrays.
-   Uses `np.unique()` to calculate program-wise student counts.
-   Supports basic data analysis of enrollment information.

### 5. Excel Data Management

-   Uses `students_data.xlsx` for persistent student data storage.
-   Loads existing records when the application starts.
-   Saves changes after adding, updating, or deleting records.

### 6. CRUD Operations

The application implements core student record management operations:

-   **Create** --- Add Student
-   **Read** --- View and Search Students
-   **Update** --- Modify Student Details
-   **Delete** --- Remove Student Records

### 7. Generative AI

-   Integrates the Groq API with an LLM.
-   Generates student-related insights from enrollment data.
-   Provides:
    -   Scholarship suggestions
    -   Placement readiness
    -   Improvement tips

### 8. API Integration

-   Uses the Groq Python client to communicate with an external AI API.
-   Sends structured student information through an API request.
-   Processes the API response and displays AI-generated insights.

### 9. Custom Python Modules

-   Separates AI functionality into `student_ai_utils.py`.
-   Uses custom functions:
    -   `generate_ai_insights()`
    -   `classify_students()`
-   Imports these functions into the main application.

### 10. Data Validation

-   Checks for duplicate Student IDs before adding a record.
-   Validates required student fields.
-   Uses `.strip()` to clean user input.

### 11. Exception Handling

-   Handles missing Excel files with `FileNotFoundError`.
-   Handles Groq API exceptions.
-   Handles Excel permission errors when implemented in the final
    version.

### 12. Rule-Based Classification

Students are classified based on their enrolled program:

-   **AI / ML** → Eligible for Placement
-   **Data-related programs** → Eligible for Scholarship
-   **Other programs** → Needs Counselling

------------------------------------------------------------------------

## Libraries & Tools

  Technology      Usage
  --------------- --------------------------------------
  Python          Application development
  Pandas          Data processing and Excel operations
  NumPy           Enrollment analysis
  OpenPyXL        Excel file support
  Groq            Generative AI API integration
  python-dotenv   Environment variable management

------------------------------------------------------------------------

## Key Technical Concepts Demonstrated

-   Python Programming
-   Object-Oriented Programming
-   Data Structures
-   Dictionary-based data management
-   File Handling
-   Excel Data Processing
-   Data Analysis
-   CRUD Operations
-   API Integration
-   Generative AI
-   Custom Modules
-   Input Validation
-   Exception Handling
-   Rule-Based Classification

------------------------------------------------------------------------

## Project Skills Summary

**Python \| Object-Oriented Programming \| Pandas \| NumPy \| Excel \|
Data Analysis \| CRUD Operations \| Generative AI \| API Integration \|
Custom Python Modules \| Data Validation \| Exception Handling**

------------------------------------------------------------------------

## Security Best Practice

API credentials should be stored in a `.env` file rather than hard-coded
in Python source code.

Example:

``` env
API_KEY=YOUR_GROQ_API_KEY
```

The `.env` file should be excluded from GitHub using `.gitignore`.

``` gitignore
.env
__pycache__/
students_data.xlsx
```

**Never commit or publish a real API key.**
