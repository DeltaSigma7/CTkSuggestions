
import customtkinter as ctk
from CTkListbox import *


def CTkSuggestions(master, widget, insert_lst):
    toplvl = None
    listbox = None
    #display all entries in list after entry
    def suggestions_output(event):
        # Convert entry into lowercase
        search_term = widget.get().lower()
        
        # Check if 3 signs are typed in or "*"
        if len(search_term) >= 3 or search_term == "*":
            if search_term == "*":
                # Show all entries
                filtered_options = insert_lst
            else:
                # Output filtered options
                filtered_options = [option for option in insert_lst if search_term in option.lower()]
            
            # Check if listbox is initialized
            if listbox is not None:
                # Delete all existing entries
                try:
                    listbox.delete(0, ctk.END)
                except IndexError:
                    pass
                
                # Insert new options to list
                for item in filtered_options:
                    listbox.insert(ctk.END, item)
             
    def destroy_toplevel(event=None):
        nonlocal toplvl, listbox

        # Unbind from widget
        custom_bindings = ["<KeyRelease>", "<Return>", "<Escape>"]
        for binding in custom_bindings:
            widget.unbind(binding)

        master.unbind("<Unmap>")

        if toplvl and toplvl.winfo_exists():
            toplvl.destroy()
            toplvl = None
            listbox = None

    def insert_first(event=None):
        if listbox and listbox.size() > 0:
            widget.delete(0, 'end')
            widget.insert(0, listbox.get(0))
            master.focus_set()
            destroy_toplevel()

    def on_listbox_select(event):
        if listbox:
            selection = listbox.curselection()
            if isinstance(selection, tuple) and selection:
                selected_item = listbox.get(selection[0])
                insert_selected(selected_item)
            elif isinstance(selection, int):
                selected_item = listbox.get(selection)
                insert_selected(selected_item)

    def insert_selected(selection):
        if selection:
            widget.delete(0, 'end')
            widget.insert(0, selection)
            master.focus_set()
            destroy_toplevel()

    def hide_toplevel_on_minimize(event):
        if master.wm_state() == 'iconic' and toplvl:
            toplvl.withdraw()


    
    # bindings
    widget.bind("<KeyRelease>", suggestions_output)
    widget.bind("<Return>", insert_first)
    widget.bind("<Escape>", destroy_toplevel)
    master.bind("<Unmap>", hide_toplevel_on_minimize)

    # create toplvl
    toplvl = ctk.CTkToplevel()
    toplvl.overrideredirect(True)

    # config size
    width = widget.winfo_width()
    height = widget.winfo_height() * 5
    x_pos = widget.winfo_rootx()
    y_pos = widget.winfo_rooty() + widget.winfo_height()

    toplvl.geometry(f'{width}x{height}+{x_pos}+{y_pos}')
    toplvl.grid_columnconfigure(0, weight=1)
    toplvl.grid_rowconfigure(0, weight=1)

    # create listbox
    listbox = CTkListbox(toplvl, font=('Calibri', 23, 'bold'))
    listbox.grid(row=0, column=0, sticky="nsew")
    listbox.bind("<<ListboxSelect>>", on_listbox_select)
