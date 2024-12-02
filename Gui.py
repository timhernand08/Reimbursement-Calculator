import customtkinter

class MyRadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, locations):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.locations = locations
        self.buttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray", text_color="white",corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10,0), sticky="ew")


        for i, value in enumerate(self.locations):
            button = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            button.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky="w")
            self.buttons.append(button)

    def getRadio(self) -> str:
        return self.variable.get()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Reimbursement Calculator")
        self.geometry("400x220")
        customtkinter.set_default_color_theme("custom_theme.json")
        customtkinter.set_appearance_mode("light")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyRadioButtonFrame(self, title="From", locations=["7975", "7900", "6625"])
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")
        self.checkbox_frame2 = MyRadioButtonFrame(self, title="To", locations=["7975", "7900", "6625"])
        self.checkbox_frame2.grid(row=0, column=1, padx=(0,10), pady=(10,0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="Enter", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print(f"You have selected {self.checkbox_frame.getRadio()} and {self.checkbox_frame2.getRadio()}")

app = App()
app.mainloop()