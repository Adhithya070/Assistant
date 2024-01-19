import tkinter as tk
from tkinter import scrolledtext
import pyttsx3

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot GUI")

        # Set UI to completely black
        self.window.configure(bg="black")

        # Increase the window size
        self.window.geometry("800x600")

        # Enable auto-scroll in the conversation
        self.text_widget = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=100, height=20, bg="black", fg="white")
        self.text_widget.grid(column=0, row=0, columnspan=4)

        self.user_entry = tk.Entry(self.window, width=60, bg="black", fg="white")
        self.user_entry.grid(column=0, row=1, padx=10, pady=10, columnspan=4)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message, bg="#4CAF50", fg="white")
        self.send_button.grid(column=0, row=2, padx=10, pady=10, columnspan=3)

        self.speak_button = tk.Button(self.window, text="Speak", command=self.speak_text, bg="#008CBA", fg="white")
        self.speak_button.grid(column=1, row=2, padx=10 , pady=10, columnspan=3)

        # Set auto-scroll to always scroll to the bottom
        self.text_widget.config(yscrollcommand=self.text_widget.yview)
        self.text_widget.see(tk.END)

        # Bind the Enter key to the send_message function
        self.window.bind('<Return>', lambda event=None: self.send_message())

        # Text-to-speech engine
        self.engine = pyttsx3.init('sapi5')

    def send_message(self):
        user_input = self.user_entry.get()
        self.text_widget.insert(tk.END, 'You: ' + user_input + '\n')

        # Add your chatbot response logic here

        self.user_entry.delete(0, tk.END)

        # Scroll to the bottom after sending a message
        self.text_widget.see(tk.END)

    def speak_text(self):
        text_to_speak = self.text_widget.get("1.0", tk.END)
        self.engine.say(text_to_speak)
        self.engine.runAndWait()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    chatbot_gui = ChatbotGUI()
    chatbot_gui.run()
