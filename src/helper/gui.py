import tkinter as tk
import cv2


def insert_header(container, text):
    heading = tk.Label(
        container,
        bg="white",
        fg="black",
        text=text,
        font='none 24 bold'
    )
    heading.place(relx=0.15, rely=0.1, anchor=tk.W)


def create_frame(container, row):
    frame = tk.Frame(container)
    frame.configure(bg='white')
    frame.place(
        relx=0.15,
        rely=(0.1 * row),
        anchor=tk.W
    )

    return frame


def create_label(master, text, row, col, fix_text=True):
    if (fix_text):
        label_text = tk.Label(
            master=master,
            text=text,
            bg="white",
            fg="black"
        )

    else:
        label_text = tk.Label(
            master=master,
            textvariable=text,
            bg="white",
            fg="black"
        )

    label_text.grid(row=row, column=col, sticky=tk.W)


def create_button(master, text, action, row, col):
    button = tk.Button(
        master=master,
        text=text,
        command=action,
        bg="white",
        fg="black"
    )
    button.grid(row=row, column=col, sticky=tk.W)


def create_check_button(master, text, variable, row, col):
    check_button = tk.Checkbutton(
        master=master,
        text=text,
        variable=variable,
        bg="white",
        fg="black"
    )
    check_button.grid(row=row, column=col, sticky=tk.W)


def create_radio_button(master, text, variable, row, col):
    radio_button = tk.Radiobutton(
        master=master,
        text=text,
        value=text,
        variable=variable,
        bg="white",
        fg="black"
    )
    radio_button.grid(row=row, column=col, sticky=tk.W)


def create_entry(master, default, row, col):

    entry = tk.Entry(master=master)
    entry.configure(bg="white", fg="black")
    entry.grid(row=row, column=col, sticky=tk.W)

    if (default != ""):
        entry.insert(tk.END, default)

    return entry


def show_image_preview(image_dir):
    print(image_dir)
    try:
        image = cv2.imread(image_dir)
        window_name = 'Preview Image'
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except:
        print("Failed to show image preview")