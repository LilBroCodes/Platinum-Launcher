from _thread import start_new_thread
from lib.dialogue import *
# import lib.server.oauth as gdauth
from PIL import Image
import lib.changelogs as changelogs
import lib.gd as gd


def launch():
    try:
        start_new_thread(gd.client, ())
        info_popup("textOnly", "Info", "Launching platinum GDPS...", 0, True)
    except Exception as e:
        info_popup("textOnly", "Fatal Error", f"Ran into an error while launching Platinum GDPS: \n\n"
                                              f"{e}", getattr(e, "errno"), True)


def creds():
    data = """
        Songs:
            Flourish - Purrple Cat
            
        Images:
            Main icon - Zud
            Custom BG (Ingame) - Zud
            T̶o̶o̶l̶s̶ ̶p̶a̶g̶e̶ ̶i̶c̶o̶n̶ (Unused in current version)
            D̶e̶m̶o̶n̶l̶i̶s̶t̶ ̶i̶c̶o̶n̶ (Unused in current version)
            M̶a̶i̶n̶ ̶p̶l̶a̶s̶t̶e̶r̶ ̶i̶c̶o̶n̶ (Unused in current version)
            
        Misc:
            Modded version of gd that allows you to launch 1.9: Absolute
                (+ Mini-Megahack)
    """
    info_popup("textOnly", "Credits", text=data, do_exit=False, width=450, height=350)


def login():
    title = "Log In"
    queries = ["Username", "Password"]

    results = [None] * len(queries)
    inputs = []

    def on_enter_button_click():
        for i, inpt in enumerate(inputs):
            results[i] = inpt.get()

        popup.destroy()

    popup = ctk.CTk()
    popup.title(title)
    popup.geometry("300x150")

    query_label = ctk.CTkLabel(master=popup, text="Enter info:")
    query_label.pack(pady=5, side="top")

    for query in queries:
        query_input = ctk.CTkEntry(master=popup, placeholder_text=query)
        query_input.pack(pady=5, side="top")
        query_input.bind("<Return>", lambda event: popup.destroy())  # Bind the Enter key.
        inputs.append(query_input)

    query_return = ctk.CTkButton(master=popup, text="Enter", command=on_enter_button_click)
    query_return.pack(pady=5, side="top")

    popup.wait_window()  # This will wait for the window to be closed before continuing

    # Code to run after the popup is closed
    print("Code after popup.wait_window()")

    # Return the result when the window is closed
    return results


def register():
    pass


def main():
    root = ctk.CTk()
    root.title("Platinum GDPS Launcher")
    root.geometry("1000x750")
    root.iconbitmap("data/favicon.ico")

    img = tk.PhotoImage(file="data/icon.png")
    root.tk.call('wm', 'iconphoto', root._w, img)

    bottom_frame = ctk.CTkFrame(root, height=50, bg_color="#333333", border_width=0)
    bottom_frame.pack(side="bottom", fill="x")

    top_frame = ctk.CTkFrame(root, height=50, bg_color="#333333", border_width=0)
    top_frame.pack(side="top", fill="x")

    text_label = ctk.CTkLabel(bottom_frame, text="Made by LilBroCodes & Zud", font=("Arial", 16),
                              text_color="#909090")
    text_label.pack(side="left", padx=10, pady=10)

    version_label = ctk.CTkLabel(bottom_frame, text="Platinum GDPS Launcher pre-01", font=("Arial", 16),
                                 text_color="#909090")
    version_label.pack(side="right", padx=10, pady=10)

    # login_button = ctk.CTkButton(top_frame, text="Log In", font=("Arial", 13), text_color="white", fg_color="#444444",
    #                           hover_color="#555555", width=65, command=login)
    # login_button.pack(side="left", padx=5)

    # register_button = ctk.CTkButton(top_frame, text="Register", font=("Arial", 13), text_color="white",
    #                              fg_color="#444444", hover_color="#555555", width=65, command=register)
    # register_button.pack(side="left", padx=5)

    launch_button = ctk.CTkButton(top_frame, text="Launch", font=("Arial", 20), text_color="white", fg_color="#444444",
                                  hover_color="#555555", width=120, height=50, command=launch)
    launch_button.pack(side="right", padx=5)

    changelogs_frame = ctk.CTkFrame(master=root, width=1920, height=1080, fg_color="#333333")
    changelogs_frame.pack(side="left", padx=10, pady=10)

    changelogs_text = ctk.CTkTextbox(master=changelogs_frame, width=1920, height=1080, text_color="white",
                                     font=("Arial", 15), fg_color="#333333")

    for version in changelogs.get_all():
        title = f"Version {version['version']}:" if version['success'] else version['version'] + ":"
        description = version['description']
        changelogs_text.insert('end', title + "\n")
        changelogs_text.insert('end', "    " + description)

    changelogs_text.configure(state=ctk.DISABLED)
    changelogs_text.pack(padx=10, pady=10)

    image_path = "data/icon.png"
    plaster_image = ctk.CTkImage(Image.open(image_path), size=(50, 50))
    plaster = ctk.CTkButton(master=top_frame, text="", image=plaster_image, bg_color="#333333", fg_color="#333333",
                            border_color="#333333", hover_color="#333333", width=50)
    plaster.pack(padx=10, side="left")

    launch_button = ctk.CTkButton(top_frame, text="Credits", font=("Arial", 20), text_color="white", fg_color="#444444",
                                  hover_color="#555555", width=50, height=50, command=creds)
    launch_button.pack(side="left", padx=5)

    root.mainloop()


if __name__ == '__main__':
    main()
