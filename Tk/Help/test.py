from tkinter import simpledialog, filedialog, Tk, Label, Entry, Button, Frame

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.title("Custom Dialog")

        # Create and pack the Entry widget
        Label(master, text="Enter a string:").grid(row=0, column=0, sticky="e")
        self.entry_var = Entry(master)
        self.entry_var.grid(row=0, column=1, padx=10, pady=10)

        # Create and pack the "Browse" button
        browse_button = Button(master, text="Browse", command=self.browse_file)
        browse_button.grid(row=1, column=0, columnspan=2, pady=10)

    def apply(self):
        # Implement the apply method to handle the data after the OK button is clicked
        self.result = self.entry_var.get()

    def browse_file(self):
        # Function to handle the "Browse" button click
        file_path = filedialog.askopenfilename(title="Select File")
        if file_path:
            # Update the Entry widget with the selected file path
            self.entry_var.delete(0, 'end')
            self.entry_var.insert(0, file_path)

# Create a root Tkinter window
root = Tk()
root.withdraw()  # Hide the main window

# Instantiate and display the custom dialog
dialog = CustomDialog(root)
result = dialog.result

# Check if a value was entered or selected
if result:
    print(f"Entered or selected value: {result}")
else:
    print("Dialog canceled.")

# Close the Tkinter window
root.destroy()
