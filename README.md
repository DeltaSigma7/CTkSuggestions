# CTkSuggestions
 CTkSuggestions implements a suggestion dropdown for a customtkinter widget

## Installation
```bash
pip install CTkSuggestions
```


## Example
```python
import customtkinter as ctk
from CTkSuggestions import suggestions
example_lst = [
    "apple","banana","cherry","date","elderberry","fig","grape",
    "honeydew","kiwi","lemon","mango","nectarine","orange",
    "papaya","quince","raspberry","strawberry","tangerine",
    "ugli fruit","vanilla","watermelon","zucchini"
]
#Setup Ctk window
app = ctk.CTk()

app.title("CTkSuggestions_example")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

#configure window size
window_width = screen_width // 2
window_height = screen_height // 2
app.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//4}")

#Create entry fields
entry = ctk.CTkEntry(app, placeholder_text="Entry",justify="center", font=("Arial", 32, "bold"))
entry2 = ctk.CTkEntry(app, placeholder_text="Entry2",justify="center", font=("Arial", 32, "bold"))
entry3 = ctk.CTkEntry(app, placeholder_text="Entry3",justify="center", font=("Arial", 32, "bold"))

entry.pack(pady=10)
entry2.pack(pady=10)
entry3.pack(pady=10)

#Bind Suggestions on FocusIn event 
entry.bind("<FocusIn>", lambda e: suggestions(app,entry,example_lst))
entry2.bind("<FocusIn>", lambda e: suggestions(app,entry2,example_lst))
entry3.bind("<FocusIn>", lambda e: suggestions(app,entry3,example_lst))

app.mainloop()
```


## Options

| Option  | Description                                      |
|---------|--------------------------------------------------|
| Master  | CustomTkinter main window                        |
| Widget  | Entry widget to bind suggestion                    |
| List  | List with potential suggestions           |


## Usage

To use CTkSuggestions in your project, follow these steps:

- **Bind to entry**: Bind the suggestion function to the entry widget, and it should appear automatically when the entry widget is focused.
  
- **Run your code**: Execute your code.

- **Focus entry**: Klick into the entry and a suggestion table will appear.

- **Typing**: After typing at least 3 letters and a suggestion with change.

- **List all**: You can type "*" to show all entrys from the list will appear.
 
- **Confirm entry**: Klick the option you search for or press <kbd>Enter</kbd> to insert it into the widget.


## Credits

Note: Parts of the code in this example are from [CustomTkinter][1] and [CTkListbox][2]

If you find my code helpful and would like to support me, feel free to buy me a Ko-fi. However, if you don't want to, that's okay too!

I'm always open to feedback to improve this project further!

[1]: https://github.com/TomSchimansky/CustomTkinter
[2]: https://github.com/Akascape/CTkListbox

