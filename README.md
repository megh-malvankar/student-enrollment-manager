# 🎓 Student Enrollment Manager

A Python-based student enrollment management system that allows users to add, view, search, update, and delete student records. The project uses **Pandas** for Excel-based data storage, **NumPy** for enrollment analysis, and the **Groq API** for AI-powered student insights and classification.

## 📌 Project Overview

The **Student Enrollment Manager** is a menu-driven Python application designed to simplify student record management.

The application stores student information such as:

* Student ID
* Name
* Qualification
* Program

Student data is stored persistently in an Excel file (`students_data.xlsx`), allowing records to be loaded automatically when the application starts.

The project also includes data analysis using NumPy and AI functionality through the Groq API.

## ✨ Features

### 👨‍🎓 Student Management

* Add new student records
* Prevent duplicate Student IDs
* View all student records
* Search students by ID
* Update student information
* Delete individual student records

### 📊 Data Analysis

* Analyze students by program
* Count students enrolled in each program
* Use NumPy arrays and `np.unique()` for analysis

### 🤖 AI-Powered Features

* Generate AI-based student insights
* Provide scholarship suggestions
* Evaluate placement readiness
* Provide improvement tips
* Classify students based on their program

### 💾 Excel Data Storage

* Uses Pandas to read and write Excel files
* Automatically saves changes to `students_data.xlsx`
* Loads existing records when the application starts

### 🛡️ Validation & Error Handling

* Prevents duplicate Student IDs
* Validates required fields
* Handles missing Excel files
* Handles Excel file permission errors

## 🛠️ Technologies Used

| Technology     | Purpose                                         |
| -------------- | ----------------------------------------------- |
| **Python**     | Core programming language                       |
| **Pandas**     | Excel data handling and management              |
| **NumPy**      | Data analysis and program-wise counting         |
| **OpenPyXL**   | Excel file support                              |
| **Groq API**   | AI-generated student insights                   |
| **Python OOP** | Application structure using classes and methods |

## 📁 Project Structure

```text
Student_Enrollment_Manager_Project/
│
├── main.py
├── student_ai_utils.py
├── .env
├── students_data.xlsx
└── README.md
```

> `students_data.xlsx` is generated/updated by the application when student data is saved.

## ⚙️ Installation

### 1. Clone the Repository

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/megh-malvankar/student-enrollment-manager.git
cd student-enrollment-manager
```

### 2. Install Required Libraries

```bash
pip install pandas numpy openpyxl groq python-dotenv
```

### 3. Configure the Groq API

Create a `.env` file in the project directory:

```env
API_KEY=YOUR_GROQ_API_KEY
```

Replace `YOUR_GROQ_API_KEY` with your own Groq API key.

**⚠️ Security:** Never upload your real API key or `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
students_data.xlsx
__pycache__/
```

### 4. Run the Application

```bash
python main.py
```


## 🧑‍💻 Application Workflow

```text
Start
  │
  ▼
Load Student Data from Excel
  │
  ▼
Display Menu
  │
  ├── Add Student
  │
  ├── View Students
  │
  ├── Search Student
  │
  ├── Update Student
  │
  ├── Delete Student
  │
  ├── Analyze Data
  │
  ├── Generate AI Insights
  │
  ├── Classify Students
  │
  └── Exit
  │
  ▼
Save Updated Data to Excel
```

## 📊 Example Data

| ID  | Name  | Qualification | Program          |
| --- | ----- | ------------- | ---------------- |
| 101 | Rahul | B.Sc          | Data Science     |
| 102 | Priya | B.Tech        | AI               |
| 103 | Amit  | BCA           | Machine Learning |

## 🤖 AI Classification

The classification module categorizes students based on their enrolled program.

```text
AI / ML
   ↓
Eligible for Placement

Data
   ↓
Eligible for Scholarship

Other Programs
   ↓
Needs Counselling
```

## 📈 NumPy Analysis

The application extracts student programs and converts them into a NumPy array.

It then uses:

```python
np.unique(arr, return_counts=True)
```

to calculate the number of students enrolled in each program.

Example:

```text
📊 Program Analysis:

AI: 2
Data Science: 3
Machine Learning: 1
```

## 🔄 CRUD Operations

The project implements core student record management operations:

* **Create** → Add student
* **Read** → View/Search student
* **Update** → Modify student details
* **Delete** → Remove student

All changes are written back to the Excel file.

## 🔐 Security

The Groq API key should be stored in `.env` rather than directly inside the Python source code.

Add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
students_data.xlsx
```

This prevents sensitive credentials and local data files from being accidentally committed to GitHub.

## 🎯 Project Objectives

* Practice Python fundamentals and Object-Oriented Programming
* Implement CRUD-based data management
* Work with Excel files using Pandas
* Perform basic data analysis using NumPy
* Create and use a custom Python module
* Integrate an external AI API
* Implement validation and exception handling
* Build a practical menu-driven application

## 🚀 Future Enhancements

Possible future improvements include:

* Graphical User Interface (GUI)
* SQLite/MySQL database integration
* Advanced student performance analytics
* Authentication and user roles
* Data visualization with Matplotlib
* Advanced AI-based student recommendations
* Export reports in PDF format

## 👨‍💻 Author

**Megh Malvankar**

Developed as a Python/Data Analytics capstone project.

## 📄 License

This project is intended for educational and portfolio purposes.
