import customtkinter as ctk
from tomwidgets.widget.basic.Tk import Tk
from tomwidgets.widget.OptionBar import OptionBar
from tomwidgets.widget.basic.Label import Label
from tomwidgets.widget.basic.Font import Font


def create_example_window():
    # Create main window
    root = Tk()
    root.title("OptionBar Example")
    root.geometry("600x400")
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create a custom font for demonstration
    custom_title_font = Font(size=16, weight="bold", family="Arial")
    custom_option_font = Font(size=12, family="Arial")

    # Create sample options
    theme_options = ["Light", "Dark", "System"]
    language_options = ["English", "Spanish", "French", "German", "Chinese"]
    size_options = ["12", "16", "20", "24"]

    # Create a label to show selected option
    status_label = Label(
        root, text="Selected Option: None", font=Font(size=14))
    status_label.grid(row=1, column=0, padx=20, pady=20, sticky="n")

    # Custom event handler for OptionBar
    def on_theme_select(selected_option):
        v = theme_option_bar.getSelectedOption()
        status_label.configure(text=f"Selected Theme: {v}")
        # Change theme based on selection
        ctk.set_appearance_mode(v.lower())

    def on_language_select(selected_option):
        status_label.configure(
            text=f"Selected Language: {language_option_bar.getSelectedOption()}")

    def on_size_select(selected_option):
        size = size_option_bar.getSelectedOption()
        size = int(size)
        status_label.configure(
            text=f"Selected Size: {size}")

        # Update the font size of the status label
        size_option_bar.setOptionFont(Font(size=size))
        size_option_bar.setTitleFont(Font(size=size))

    # Create first OptionBar with custom styling
    theme_option_bar = OptionBar(root, title="Theme:", options=theme_options,
                                 defaultOption="System", titleFont=custom_title_font, 
                                 optionFont=custom_option_font, height=50)
    theme_option_bar.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    # Override the onOptionSelect method
    theme_option_bar.bindEvent(on_theme_select)

    # Create additional OptionBars
    language_option_bar = OptionBar(root, title="Language:", options=language_options,
                                    defaultOption="English", height=50)
    language_option_bar.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
    language_option_bar.bindEvent(on_language_select)

    size_option_bar = OptionBar(root, title="Font Size:", options=size_options,
                                defaultOption="16", height=50)
    size_option_bar.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
    size_option_bar.bindEvent(on_size_select)

    # Create a button to dynamically update options
    def update_options():
        new_language_options = [
            "English", "Spanish", "French", "German", "Chinese", "Japanese", "Russian"]
        language_option_bar.setOptions(
            new_language_options, defaultOption="Japanese")

    update_btn = ctk.CTkButton(
        root, text="Update Language Options", command=update_options)
    update_btn.grid(row=4, column=0, padx=20, pady=20)

    # Start the app
    root.mainloop()


def main():
    create_example_window()


if __name__ == "__main__":
    main()
