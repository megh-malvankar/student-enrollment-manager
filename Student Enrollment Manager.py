# ==========================================
# Student Enrollment Manager
# ==========================================

import pandas as pd
import numpy as np
import os
from groq import Groq

# =========================
# Load API Key from .env
# =========================
API_KEY = "GROQ_API_KEY='your_api_key_here'"  # ⚠ keep hidden in real project

client = Groq(api_key=API_KEY)

# =========================
# AI FUNCTION
# =========================
def generate_ai_insights(student_summary):
    try:
        prompt = f"""
        Analyze the student data and provide:
        - Scholarship suggestions
        - Placement readiness
        - Improvement tips

        Data:
        {student_summary}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ API Error: {str(e)}"


# =========================
# CLASSIFICATION FUNCTION
# =========================
def classify_students(students):
    result = {}

    for sid, data in students.items():
        program = data["program"].lower()

        if "ai" in program or "ml" in program:
            result[sid] = "Eligible for Placement"
        elif "data" in program:
            result[sid] = "Eligible for Scholarship"
        else:
            result[sid] = "Needs Counselling"

    return result


# =========================
# MAIN CLASS
# =========================
class StudentManager:

    def __init__(self):
        self.students = {}
        self.file_name = "students_data.xlsx"
        self.load_data()

    # =========================
    # LOAD DATA
    # =========================
    def load_data(self):
        try:
            df = pd.read_excel(self.file_name)
            for _, row in df.iterrows():
                self.students[str(row["ID"])] = {
                    "name": row["Name"],
                    "qualification": row["Qualification"],
                    "program": row["Program"]
                }
            print("✅ Data loaded successfully!")

        except FileNotFoundError:
            print("⚠ No previous data found.")

        except PermissionError:
            print("❌ Close Excel file (students_data.xlsx) and try again!")

    # =========================
    # ADD STUDENT
    # =========================
    def add_student(self):
        sid = input("Enter Student ID: ").strip()

        if sid in self.students:
            print("❌ ID already exists!")
            return

        name = input("Enter Name: ").strip()
        qual = input("Enter Qualification: ").strip()
        prog = input("Enter Program: ").strip()

        if not sid or not name or not prog:
            print("❌ Invalid input!")
            return

        self.students[sid] = {
            "name": name,
            "qualification": qual,
            "program": prog
        }

        print("✅ Student added!")
        self.export_to_excel()

    # =========================
    # VIEW
    # =========================
    def view_students(self):
        if not self.students:
            print("⚠ No records.")
            return

        for sid, data in self.students.items():
            print(f"\nID: {sid}")
            print(f"Name: {data['name']}")
            print(f"Qualification: {data['qualification']}")
            print(f"Program: {data['program']}")

    # =========================
    # SEARCH
    # =========================
    def search_student(self):
        sid = input("Enter ID: ").strip()

        if sid in self.students:
            print(self.students[sid])
        else:
            print("❌ Not found!")

    # =========================
    # UPDATE (FIXED)
    # =========================
    def update_student(self):
        sid = input("Enter ID: ").strip()

        if sid not in self.students:
            print("❌ Not found!")
            return

        name = input("New Name: ").strip()
        qual = input("New Qualification: ").strip()
        prog = input("New Program: ").strip()

        if name:
            self.students[sid]["name"] = name
        if qual:
            self.students[sid]["qualification"] = qual
        if prog:
            self.students[sid]["program"] = prog

        print("✅ Updated!")
        self.export_to_excel()

    # =========================
    # DELETE
    # =========================
    def delete_student(self):
        sid = input("Enter ID: ").strip()

        if sid in self.students:
            del self.students[sid]
            print("✅ Deleted!")
            self.export_to_excel()
        else:
            print("❌ Not found!")

    # =========================
    # EXPORT
    # =========================
    def export_to_excel(self):
        try:
            df = pd.DataFrame([
                {
                    "ID": sid,
                    "Name": data["name"],
                    "Qualification": data["qualification"],
                    "Program": data["program"]
                }
                for sid, data in self.students.items()
            ])

            df.to_excel(self.file_name, index=False)

        except PermissionError:
            print("❌ Close Excel file before saving!")

    # =========================
    # ANALYSIS
    # =========================
    def analyze_data(self):
        if not self.students:
            print("⚠ No data.")
            return

        programs = [d["program"] for d in self.students.values()]
        arr = np.array(programs)

        unique, counts = np.unique(arr, return_counts=True)

        print("\n📊 Program Analysis:")
        for u, c in zip(unique, counts):
            print(f"{u}: {c}")

    # =========================
    # AI
    # =========================
    def ai_insights(self):
        if not self.students:
            print("⚠ No data.")
            return

        summary = ""
        for sid, data in self.students.items():
            summary += f"{sid} - {data['program']}\n"

        print("\n🤖 AI Insights:\n")
        print(generate_ai_insights(summary))

    # =========================
    # CLASSIFY
    # =========================
    def classify(self):
        result = classify_students(self.students)

        print("\n📌 Classification:")
        for sid, status in result.items():
            print(sid, "→", status)

    # =========================
    # MENU
    # =========================
    def menu(self):
        while True:
            print("\n1 Add 2 View 3 Search 4 Update 5 Delete 6 Analyze 7 AI 8 Classify 9 Exit")
            ch = input("Choice: ")

            if ch == "1":
                self.add_student()
            elif ch == "2":
                self.view_students()
            elif ch == "3":
                self.search_student()
            elif ch == "4":
                self.update_student()
            elif ch == "5":
                self.delete_student()
            elif ch == "6":
                self.analyze_data()
            elif ch == "7":
                self.ai_insights()
            elif ch == "8":
                self.classify()
            elif ch == "9":
                print("Exiting...")
                break
            else:
                print("❌ Invalid choice!")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app = StudentManager()
    app.menu()