import customtkinter as ctk
import math

# Basic settings
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ModernCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")
        self.geometry("400x650")
        self.resizable(False, False)

        self.expression = ""

        # --- Display Screen ---
        self.entry = ctk.CTkEntry(self, placeholder_text="0", height=80, corner_radius=10,
                                  font=("Orbitron", 32), justify="right", fg_color="#1e1e1e")
        self.entry.pack(padx=20, pady=(30, 10), fill="x")

        # --- Button Frame ---
        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Button definitions (Label, Row, Col, Color Type)
        # Types: "num" (grey), "op" (orange), "sci" (blue), "clear" (red)
        buttons = [
            ('sin', 0, 0, 'sci'), ('cos', 0, 1, 'sci'), ('tan', 0, 2, 'sci'), ('log', 0, 3, 'sci'),
            ('√', 1, 0, 'sci'), ('^', 1, 1, 'sci'), ('(', 1, 2, 'sci'), (')', 1, 3, 'sci'),
            ('C', 2, 0, 'clear'), ('DEL', 2, 1, 'clear'), ('π', 2, 2, 'sci'), ('/', 2, 3, 'op'),
            ('7', 3, 0, 'num'), ('8', 3, 1, 'num'), ('9', 3, 2, 'num'), ('*', 3, 3, 'op'),
            ('4', 4, 0, 'num'), ('5', 4, 1, 'num'), ('6', 4, 2, 'num'), ('-', 4, 3, 'op'),
            ('1', 5, 0, 'num'), ('2', 5, 1, 'num'), ('3', 5, 2, 'num'), ('+', 5, 3, 'op'),
            ('0', 6, 0, 'num'), ('.', 6, 1, 'num'), ('=', 6, 2, 'equal')
        ]

        # Configure grid
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)

        for (text, row, col, style) in buttons:
            self.create_button(text, row, col, style)

    def create_button(self, text, row, col, style):
        # Color schemes
        colors = {
            "num": ("#3d3d3d", "#505050"),
            "op": ("#ff9500", "#ffaa33"),
            "sci": ("#2b2b2b", "#3b3b3b"),
            "clear": ("#ff3b30", "#ff5e57"),
            "equal": ("#34c759", "#4cd964")
        }

        fg_color, hover_color = colors.get(style)

        # Handle the '=' button stretching across two columns
        columnspan = 2 if text == '=' else 1

        btn = ctk.CTkButton(self.button_frame, text=text, corner_radius=10,
                            font=("Arial", 18, "bold"),
                            fg_color=fg_color, hover_color=hover_color,
                            height=60, width=0,
                            command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, columnspan=columnspan, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        current_text = self.entry.get()

        if char == "C":
            self.entry.delete(0, ctk.END)
        elif char == "DEL":
            self.entry.delete(len(current_text) - 1, ctk.END)
        elif char == "=":
            try:
                # Prepare string for math evaluation
                res = current_text.replace('√', 'math.sqrt')
                res = res.replace('^', '**')
                res = res.replace('π', 'math.pi')
                res = res.replace('sin', 'math.sin(math.radians')
                res = res.replace('cos', 'math.cos(math.radians')
                res = res.replace('tan', 'math.tan(math.radians')

                # Close brackets for trig functions if they were opened
                open_bracket_count = res.count('(')
                close_bracket_count = res.count(')')
                if open_bracket_count > close_bracket_count:
                    res += ')' * (open_bracket_count - close_bracket_count)

                output = eval(res)
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, str(round(output, 8)))
            except Exception:
                self.entry.delete(0, ctk.END)
                self.entry.insert(0, "Error")
        else:
            # For sin/cos/tan, automatically add a bracket
            if char in ['sin', 'cos', 'tan']:
                self.entry.insert(ctk.END, char + "(")
            else:
                self.entry.insert(ctk.END, char)


if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()