import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import asyncio


loop = asyncio.get_event_loop()

if not loop.is_closed():
    loop.run_until_complete(asyncio.sleep(0))  # Let pending tasks complete
    loop.close()


# Dummy credentials
USERNAME = "admin"
PASSWORD = "password"


def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        messagebox.showinfo("Login Success", "Welcome!")
        login_window.destroy()
        open_translator()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials!")


def open_translator():
    translator_window = tk.Tk()
    translator_window.title("Language Translator")
    translator_window.geometry("500x400")

    import asyncio
    from googletrans import Translator

    def translate_text():
        async def async_translate():
            translator = Translator()
            translated = await translator.translate(text_input.get("1.0", tk.END),
                                                    src=source_lang.get(),
                                                    dest=target_lang.get())
            text_output.delete("1.0", tk.END)
            text_output.insert(tk.END, translated.text)

        asyncio.run(async_translate())

    def speak_text():
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text_output.get("1.0", tk.END))
        engine.runAndWait()

    tk.Label(translator_window, text="Enter Text").pack()
    text_input = tk.Text(translator_window, height=5)
    text_input.pack()

    tk.Label(translator_window, text="Select Source Language").pack()
    source_lang = ttk.Combobox(translator_window, values=list(LANGUAGES.values()))
    source_lang.set("english")
    source_lang.pack()

    tk.Label(translator_window, text="Select Target Language").pack()
    target_lang = ttk.Combobox(translator_window, values=list(LANGUAGES.values()))
    target_lang.set("spanish")
    target_lang.pack()

    tk.Button(translator_window, text="Translate", bg="blue", fg="white", command=translate_text).pack()
    tk.Button(translator_window, text="Speak", bg="green", fg="white", command=speak_text).pack()

    tk.Label(translator_window, text="Translated Text").pack()
    text_output = tk.Text(translator_window, height=5)
    text_output.pack()

    translator_window.mainloop()


# Create Login Window
login_window = tk.Tk()
login_window.title("Login Page")
login_window.geometry("300x200")

tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", bg="blue", fg="white", command=login).pack()


login_window.mainloop()


