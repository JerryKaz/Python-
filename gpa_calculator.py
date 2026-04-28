import customtkinter as ctk
from tkinter import ttk, messagebox

# --- CONFIGURATION & STYLING ---
UPSA_BLUE = "#002147"
UPSA_GOLD = "#FFD700"
DARK_GREY = "#2B2B2B"

# Grade Point Mapping
GRADE_MAP = {
    "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5,
    "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0
}


class GPACalculatorLogic:
    """Handles the mathematical calculations and data storage."""

    def __init__(self):
        self.courses = []

    def add_course(self, name, credits, grade):
        # Convert letter grade to points if necessary
        try:
            if grade.upper() in GRADE_MAP:
                gp = GRADE_MAP[grade.upper()]
            else:
                gp = float(grade)

            credits = float(credits)
            self.courses.append({
                "name": name,
                "credits": credits,
                "grade_point": gp,
                "display_grade": grade.upper()
            })
            return True
        except ValueError:
            return False

    def calculate_results(self):
        total_credits = sum(c['credits'] for c in self.courses)
        total_points = sum(c['grade_point'] * c['credits'] for c in self.courses)

        gpa = total_points / total_credits if total_credits > 0 else 0.0
        return total_credits, round(gpa, 2)

    def clear_data(self):
        self.courses = []


class GPACalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.logic = GPACalculatorLogic()

        # Window Setup
        self.title("UPSA Student Dashboard - GPA Calculator")
        self.geometry("800x700")
        ctk.set_appearance_mode("light")

        # UI Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Middle section expands

        self.create_header()
        self.create_input_section()
        self.create_table_section()
        self.create_footer_section()

    def create_header(self):
        header = ctk.CTkFrame(self, fg_color=UPSA_BLUE, height=80, corner_radius=0)
        header.grid(row=0, column=0, sticky="nsew", pady=(0, 20))

        title = ctk.CTkLabel(header, text="STUDENT GPA DASHBOARD",
                             font=ctk.CTkFont(size=24, weight="bold"), text_color="white")
        title.place(relx=0.5, rely=0.5, anchor="center")

    def create_input_section(self):
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.grid(row=1, column=0, padx=40, sticky="nsew")
        input_frame.grid_columnconfigure((0, 1, 2), weight=1)

        # Course Name
        ctk.CTkLabel(input_frame, text="Course Name", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        self.entry_name = ctk.CTkEntry(input_frame, placeholder_text="e.g. Data Structures", width=200)
        self.entry_name.grid(row=1, column=0, padx=10, pady=10)

        # Credit Hours
        ctk.CTkLabel(input_frame, text="Credit Hours", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10,
                                                                                        pady=5)
        self.entry_credits = ctk.CTkEntry(input_frame, placeholder_text="e.g. 3", width=100)
        self.entry_credits.grid(row=1, column=1, padx=10, pady=10)

        # Grade
        ctk.CTkLabel(input_frame, text="Grade (Letter/Point)", font=("Arial", 12, "bold")).grid(row=0, column=2,
                                                                                                padx=10, pady=5)
        self.entry_grade = ctk.CTkComboBox(input_frame, values=["A", "B+", "B", "C+", "C", "D+", "D", "F"], width=120)
        self.entry_grade.grid(row=1, column=2, padx=10, pady=10)

        # Add Button
        self.btn_add = ctk.CTkButton(input_frame, text="Add Course", fg_color=UPSA_BLUE,
                                     hover_color="#003366", command=self.add_course_event)
        self.btn_add.grid(row=1, column=3, padx=10, pady=10)

    def create_table_section(self):
        # Table Container
        table_frame = ctk.CTkFrame(self, fg_color="white", border_width=2, border_color="#E0E0E0")
        table_frame.grid(row=2, column=0, padx=40, pady=20, sticky="nsew")

        # Style for Treeview (Modern Look)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", fieldbackground="white", rowheight=30, font=("Arial", 11))
        style.configure("Treeview.Heading", background="#F2F2F2", font=("Arial", 12, "bold"))
        style.map("Treeview", background=[('selected', UPSA_BLUE)])

        self.tree = ttk.Treeview(table_frame, columns=("Name", "Credits", "Grade", "Points"), show="headings")
        self.tree.heading("Name", text="COURSE NAME")
        self.tree.heading("Credits", text="CREDITS")
        self.tree.heading("Grade", text="GRADE")
        self.tree.heading("Points", text="GRADE POINTS")

        self.tree.column("Name", width=300)
        self.tree.column("Credits", width=100, anchor="center")
        self.tree.column("Grade", width=100, anchor="center")
        self.tree.column("Points", width=120, anchor="center")

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

    def create_footer_section(self):
        footer_frame = ctk.CTkFrame(self, fg_color="#F8F8F8", height=120, corner_radius=10)
        footer_frame.grid(row=3, column=0, padx=40, pady=(0, 30), sticky="nsew")

        # GPA Display
        self.lbl_total_credits = ctk.CTkLabel(footer_frame, text="Total Credits: 0", font=("Arial", 16))
        self.lbl_total_credits.pack(side="left", padx=30)

        self.lbl_gpa = ctk.CTkLabel(footer_frame, text="GPA: 0.00", font=("Arial", 28, "bold"), text_color=UPSA_BLUE)
        self.lbl_gpa.pack(side="left", expand=True)

        # Reset Button
        btn_clear = ctk.CTkButton(footer_frame, text="Clear All", fg_color="#CC0000",
                                  hover_color="#990000", width=100, command=self.reset_app)
        btn_clear.pack(side="right", padx=30)

    # --- LOGIC HANDLERS ---
    def add_course_event(self):
        name = self.entry_name.get()
        credits = self.entry_credits.get()
        grade = self.entry_grade.get()

        if not name or not credits or not grade:
            messagebox.showwarning("Input Error", "Please fill in all fields.")
            return

        success = self.logic.add_course(name, credits, grade)

        if success:
            # Update UI Table
            gp = GRADE_MAP.get(grade.upper(), grade)
            self.tree.insert("", "end", values=(name, credits, grade.upper(), gp))

            # Update Results
            self.update_results()

            # Clear Inputs
            self.entry_name.delete(0, 'end')
            self.entry_credits.delete(0, 'end')
        else:
            messagebox.showerror("Error", "Invalid Credits or Grade Point value.")

    def update_results(self):
        total_credits, gpa = self.logic.calculate_results()
        self.lbl_total_credits.configure(text=f"Total Credits: {total_credits}")
        self.lbl_gpa.configure(text=f"GPA: {gpa:.2f}")

    def reset_app(self):
        if messagebox.askyesno("Reset", "Are you sure you want to clear all data?"):
            self.logic.clear_data()
            for item in self.tree.get_children():
                self.tree.delete(item)
            self.update_results()
            self.entry_name.delete(0, 'end')
            self.entry_credits.delete(0, 'end')


if __name__ == "__main__":
    app = GPACalculatorApp()
    app.mainloop()