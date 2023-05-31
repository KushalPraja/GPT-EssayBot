import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from chatbot_logic import get_chatgpt_response


def start_chatbot():
    start_menu.withdraw()  # Hide the start menu window
    window.deiconify()  # Show the main chatbot window


def quit_chatbot():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        window.destroy()
        start_menu.destroy()
        exit()


def send_message():
    user_input = user_entry.get().strip()

    if not user_input:
        return  # Don't send empty messages

    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_area.insert(tk.END, "\n", "space")  # Add a space between user input and chatbot response
    chat_area.insert(tk.END, "Chatbot: " + get_chatgpt_response(
        "Write a detailed 300-word essay that goes in-depth about: " +
        user_input + ". Make sure to use evidence to further back up your claim and include links."
    ) + "\n", "chatbot")
    chat_area.see(tk.END)
    chat_area.configure(state='disabled')
    user_entry.delete(0, tk.END)


def clear_chat():
    chat_area.configure(state='normal')
    chat_area.delete('1.0', tk.END)
    chat_area.configure(state='disabled')


# Start Menu GUI Setup
# Start Menu GUI Setup
# Start Menu GUI Setup
start_menu = tk.Tk()
start_menu.title(" EssayBot Start Menu")
start_menu.geometry("400x300")
start_menu.resizable(False, False)

# Create a gradient background
canvas = tk.Canvas(start_menu, width=400, height=300)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

gradient = Image.open("Images/gradient_image.jpg")
gradient = gradient.resize((400, 300), Image.ANTIALIAS)  # Resize the image
gradient = ImageTk.PhotoImage(gradient)
canvas.create_image(0, 0, anchor="nw", image=gradient)




title_label = tk.Label(start_menu, text="Welcome to EssayBot!", font=("Arial", 24), fg="white", bg="black")
title_label.pack(pady=(50, 20))


# Create a start button with an exciting style
style = ttk.Style()
style.configure(
    "Exciting.TButton",
    foreground="#ffffff",
    background="#ff0055",
    font=("Arial", 16, "bold"),
    relief="raised",
    width=15,
    height=3
)
style.map(
    "Exciting.TButton",
    foreground=[('pressed', "#ffffff"), ('active', "#ffffff")],
    background=[('pressed', "#ff0033"), ('active', "#ff0033")]
)

start_button = ttk.Button(
    start_menu,
    text="Start Chatbot",
    command=start_chatbot,
    style="Exciting.TButton"
)
start_button.pack(pady=(0, 30))

quit_button = ttk.Button(
    start_menu,
    text="Quit",
    command=quit_chatbot,
    style="Modern.TButton"
)
quit_button.pack(pady=(0, 10))


# Create the main chatbot window
window = tk.Toplevel()
window.withdraw()
window.title(" Essaybot v1 ")
window.geometry("500x600")
window.resizable(True, True)

style.configure(
    "Modern.TButton",
    foreground="#ffffff",
    background="#007bff",
    font=("Arial", 12),
    relief="flat",
    width=10,
    height=2
)
style.map(
    "Modern.TButton",
    foreground=[('pressed', "#ffffff"), ('active', "#ffffff")],
    background=[('pressed', "#0056b3"), ('active', "#0056b3")]
)

bg_image = ImageTk.PhotoImage(Image.open("Images/background_image.jpg"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

chat_area = scrolledtext.ScrolledText(window, width=60, height=30, state='disabled', wrap=tk.WORD, font=("Montserrat", 16))
chat_area.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
chat_area.tag_configure("user", foreground="#AEC6CF", font=("Montserrat", 13, "bold"), lmargin1=20, lmargin2=20)
chat_area.tag_configure("chatbot", foreground="#F8C8DC", font=("Montserrat", 13), lmargin1=20, lmargin2=20)

chat_area.tag_configure("space", spacing1=10)  # Add spacing after user input 



window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

user_entry = ttk.Entry(window, width=50, font=("Arial", 12))
user_entry.grid(row=1, column=0, padx=10, pady=5, sticky="W")

send_button = ttk.Button(
    window,
    text="Send",
    command=send_message,
    style="Modern.TButton"
)
send_button.grid(row=1, column=0, padx=10, pady=5, sticky="E")

clear_button = ttk.Button(
    window,
    text="Clear",
    command=clear_chat,
    style="Modern.TButton"
)
clear_button.grid(row=2, column=0, padx=10, pady=5, sticky="E")

start_menu.mainloop()
