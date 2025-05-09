import customtkinter as ctk


class CalculatorApp:
    def __init__(self, master):
        master.title("Calculator")
        master.configure(bg="#1C1C1C")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.result_var = ctk.StringVar()
        self.result_entry = ctk.CTkEntry(
            master,
            textvariable=self.result_var,
            font=("Arial", 48, "bold"),
            fg_color="#1C1C1C",
            text_color="#fff",
            border_width=0,
            justify="right",
            corner_radius=16,
            height=80,
        )
        self.result_entry.grid(
            row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=12
        )

        self.create_buttons(master)

        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

        # Bind das teclas
        master.bind("<Key>", self.key_event)

    def key_event(self, event):
        key = event.char
        if key in "0123456789":
            self.on_button_click(key)
        elif key in "+-*/.":
            self.on_button_click(key)
        elif key == "\r":  # Enter
            self.on_button_click("=")
        elif key == "\x08":  # Backspace
            self.result_var.set(self.result_var.get()[:-1])
        elif key.lower() == "c":
            self.on_button_click("C")
        elif event.keysym == "Escape":
            event.widget.quit()
        elif event.keysym == "Delete":
            self.on_button_click("C")

    def create_buttons(self, master):
        buttons = [
            ("C", 1, 0, "#D4D4D2", "#000"),
            ("+/-", 1, 1, "#D4D4D2", "#000"),
            ("%", 1, 2, "#D4D4D2", "#000"),
            ("/", 1, 3, "#FF9500", "#fff"),
            ("7", 2, 0, "#505050", "#fff"),
            ("8", 2, 1, "#505050", "#fff"),
            ("9", 2, 2, "#505050", "#fff"),
            ("*", 2, 3, "#FF9500", "#fff"),
            ("4", 3, 0, "#505050", "#fff"),
            ("5", 3, 1, "#505050", "#fff"),
            ("6", 3, 2, "#505050", "#fff"),
            ("-", 3, 3, "#FF9500", "#fff"),
            ("1", 4, 0, "#505050", "#fff"),
            ("2", 4, 1, "#505050", "#fff"),
            ("3", 4, 2, "#505050", "#fff"),
            ("+", 4, 3, "#FF9500", "#fff"),
            ("0", 5, 0, "#505050", "#fff"),
            (".", 5, 2, "#505050", "#fff"),
            ("=", 5, 3, "#FF9500", "#fff"),
        ]

        for text, row, col, bg, fg in buttons:
            colspan = 2 if text == "0" else 1
            btn = ctk.CTkButton(
                master,
                text=text,
                font=("Arial", 28, "bold"),
                fg_color=bg,
                text_color=fg,
                corner_radius=40,
                hover_color=(
                    "#888"
                    if bg == "#505050"
                    else "#FFB84D" if bg == "#FF9500" else "#fff"
                ),
                command=lambda val=text: self.on_button_click(val),
                height=70,
            )
            btn.grid(
                row=row, column=col, columnspan=colspan, sticky="nsew", padx=8, pady=8
            )
            if text == "0":
                # Pular a próxima coluna para o botão 0 ocupar duas colunas
                continue

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        elif value == "C":
            self.result_var.set("")
        elif value == "+/-":
            current = self.result_var.get()
            if current and current[0] == "-":
                self.result_var.set(current[1:])
            elif current:
                self.result_var.set("-" + current)
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + value)
