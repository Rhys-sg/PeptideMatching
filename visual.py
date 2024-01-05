import tkinter as tk
from tkinter import ttk, filedialog

class CustomButton:
    def __init__(self, canvas, text, command, x, y, width, height, color="black", hover_color="grey"):
        self.canvas = canvas
        self.button = self.create_button(text, command, x, y, width, height, color, hover_color)

    def create_button(self, text, command, x, y, width, height, color, hover_color):
        # Create a rounded rectangle
        self.rectangle = self.canvas.create_rectangle(x, y, x + width, y + height, outline=color, width=2, fill="white")
        self.text = self.canvas.create_text(x + width/2, y + height/2, text=text, fill=color, font=("Helvetica", 10))

        # Bind events for hovering
        self.canvas.tag_bind(self.rectangle, '<Enter>', lambda event: self.on_enter(hover_color))
        self.canvas.tag_bind(self.rectangle, '<Leave>', lambda event: self.on_leave(color))
        self.canvas.tag_bind(self.text, '<Enter>', lambda event: self.on_enter(hover_color))
        self.canvas.tag_bind(self.text, '<Leave>', lambda event: self.on_leave(color))

        # Bind click event
        self.canvas.tag_bind(self.rectangle, '<Button-1>', lambda event: command())
        self.canvas.tag_bind(self.text, '<Button-1>', lambda event: command())

        return self.rectangle

    def on_enter(self, hover_color):
        # Change color when hovered
        self.canvas.itemconfig(self.button, outline=hover_color)


    def on_leave(self, color):
        # Change color back when not hovered
        self.canvas.itemconfig(self.button, outline=color)


class IncrementalButton:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.integer_value = tk.IntVar(value=1)

        self.canvas = tk.Canvas(parent_frame, width=60, height=20, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, pady=(0, 5), padx=(2, 0), sticky="w")

        self.minus_button = CustomButton(self.canvas, "-", self.decrement_integer, 0, 0, 20, 20)
        self.value_label = self.create_label(self.integer_value.get(), 20, 0)
        self.plus_button = CustomButton(self.canvas, "+", self.increment_integer, 40, 0, 20, 20)

        # Configure column weights
        parent_frame.columnconfigure(0, weight=1)

    def create_label(self, text, x, y):
        label = self.canvas.create_text(x + 10, y + 10, text=str(text), fill="black", font=("Helvetica", 10))
        return label

    def increment_integer(self):
        current_value = self.integer_value.get()
        self.integer_value.set(current_value + 1)
        self.update_button_state()

    def decrement_integer(self):
        current_value = self.integer_value.get()
        if current_value > 1:
            self.integer_value.set(current_value - 1)
            self.update_button_state()

    def update_button_state(self):
        self.canvas.itemconfig(self.value_label, text=str(self.integer_value.get()))

class PeptideMatchingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Peptide Matching")

        # Frame to hold the elements
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.label = tk.Label(frame, text="Spectroscopy Data")
        self.label.grid(row=1, column=0, pady=(0, 2), sticky="w")

        # Initialize the Entry with a placeholder text
        self.path_entry = tk.Entry(frame, width=20)
        self.path_entry.grid(row=2, column=0, pady=(0, 2), padx=5, sticky="ew")
        self.path_entry.insert(0, "Path to file")
        self.path_entry.config(foreground='grey')

        # Create a subframe for the widgets below "Amino Acids:"
        subframe = tk.Frame(frame)
        subframe.grid(row=3, column=0, pady=(0, 2), sticky="w")

        # Title for the Combobox
        self.amino_acids_label = tk.Label(subframe, text="Amino Acids:")
        self.amino_acids_label.grid(row=0, column=0, pady=(0, 2), sticky="w")

        # Dropdown menu options
        amino_acids_options = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

        # Initialize the Combobox with the amino acids options and set width to make it smaller
        self.amino_acids_combobox = ttk.Combobox(subframe, values=amino_acids_options, width=3)
        self.amino_acids_combobox.grid(row=1, column=0, pady=(0, 2), padx=5, sticky="w")

        # Initialize the AdditionalEntryWidget in the subframe at row=2, column=2
        self.additional_entry_widget = IncrementalButton(subframe)
        self.additional_entry_widget.canvas.grid(row=1, column=1, pady=(0, 2), padx=(0, 2), sticky="w")

        self.path_entry.bind("<FocusIn>", self.clear_placeholder)
        self.path_entry.bind("<FocusOut>", self.restore_placeholder)

        self.upload_button = tk.Button(frame, text="Upload File", command=self.upload_file)
        self.upload_button.grid(row=2, column=1, pady=(0, 2), padx=5, sticky="w")

        # Configure column and row weights to make them expand
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=0)
        frame.rowconfigure(3, weight=1)

    def clear_placeholder(self, event):
        if self.path_entry.get() == "Path to file":
            self.path_entry.delete(0, tk.END)
            self.path_entry.config(foreground='black')

    def restore_placeholder(self, event):
        if not self.path_entry.get():
            self.path_entry.insert(0, "Path to file")
            self.path_entry.config(foreground='grey')
        else:
            self.path_entry.config(foreground='black')

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])

        if file_path:
            self.path_entry.config(state='normal')
            self.path_entry.delete(0, tk.END)
            try:
                self.path_entry.insert(0, file_path)
                self.path_entry.config(foreground='black')
            except Exception as e:
                self.label.config(text=f"Error reading file: {e}")
                self.path_entry.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = PeptideMatchingApp(root)
    root.geometry("600x200")
    root.mainloop()
