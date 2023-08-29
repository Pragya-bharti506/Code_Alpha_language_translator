import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        self.root.configure(bg="#458B74")
    
    # To select the input language
        self.languages = ["Auto Detect", "English", "French", "Hindi", "Japanese", " Russian", "Spanish", "Arabic", "Nepali"]
        self.language_from_label = ttk.Label(root, text="From Language:", background="#F0F0F0")
        self.language_from_label.pack(pady=(100, 0))
        self.language_from_label.pack()

        self.from_language_var = tk.StringVar()
        self.from_language_dropdown = ttk.Combobox(root, textvariable=self.from_language_var, values=self.languages)
        self.from_language_dropdown.pack(pady=(3, 0))
        self.from_language_dropdown.pack()

    # Input text area
        
        self.default_text = "Enter the text"
        self.entry_var = tk.StringVar()
        self.entry_var.set(self.default_text)

        self.entry = tk.Text(root, width=50, height=8, font=("Arial", 12), foreground="gray", wrap="word")
        self.entry.insert("1.0", self.default_text)
        self.entry.bind("<FocusIn>", self.clear_entry)
        self.entry.bind("<FocusOut>", self.restore_entry)
        self.entry.pack(pady=(30, 15))


        
    # Output language selector
        self.language_to_label = ttk.Label(root, text="To Language:", background="#F0F0F0")
        self.language_to_label.pack(pady=(30, 5))
        self.language_to_label.pack()

        self.to_language_var = tk.StringVar()
        self.to_language_dropdown = ttk.Combobox(root, textvariable=self.to_language_var, values=self.languages)
        self.to_language_dropdown.pack()

    # Translate button
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=(30, 15))
        self.translate_button.pack()

    # Output text box
        self.result_label = ttk.Label(root, text="Translated text:", background="#F0F0F0")
        self.result_label.pack(pady=(0, 5))
        self.result_label.pack()

        self.result_text = tk.Text(root, height=5, width=50)
        self.result_text.pack()

        self.translator = Translator()
    
    def clear_entry(self, event):
        if self.entry.get("1.0", "end-1c") == self.default_text:
            self.entry.delete("1.0", "end-1c")
            self.entry.config(foreground="black")

    def restore_entry(self, event):
        if not self.entry.get("1.0", "end-1c"):
            self.entry.insert("1.0", self.default_text)
            self.entry.config(foreground="gray")

    def translate_text(self):
        input_text = self.entry.get("1.0", "end-1c")
        from_language = self.from_language_var.get()
        to_language = self.to_language_var.get()


        if from_language == "Auto Detect":
            from_language = "auto"

        translated_text = self.translator.translate(input_text, src=from_language, dest=to_language)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, translated_text.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()
