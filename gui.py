import tkinter as tk
from tkinter import ttk
from voice import listen, speak

class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("400x300")  # Set initial window size

        # Add a background color
        self.root.configure(background='#333')

        # Create a style for buttons and labels
        self.style = ttk.Style()
        self.style.configure('TButton', background='#4CAF50', foreground='white', font=('Helvetica', 12))
        self.style.configure('TLabel', background='#333', foreground='white', font=('Helvetica', 14))

        # Create and place widgets
        self.label = ttk.Label(root, text="Welcome to Jarvis", style='TLabel')
        self.label.pack(pady=20)

        self.listen_button = ttk.Button(root, text="Listen", command=self.listen_command, style='TButton')
        self.listen_button.pack(pady=10)

        self.output_label = ttk.Label(root, text="", style='TLabel')
        self.output_label.pack(pady=10)

    def listen_command(self):
        query = listen()
        if query != "None":
            self.output_label.config(text=f"You said: {query}")
            speak(query)

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()
