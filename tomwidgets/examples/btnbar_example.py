from tomwidgets.widget.BtnBar import BtnBar, BtnConfig
import customtkinter as ctk
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    # Create the main application window
    app = ctk.CTk()
    app.title("Enhanced BtnBar Example")
    app.geometry("700x500")

    # Set a modern theme
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    # Create a main frame for better organization
    main_frame = ctk.CTkFrame(app)
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Title label
    title_label = ctk.CTkLabel(main_frame, text="Enhanced BtnBar Widget Demo",
                               font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=(0, 20))

    # Create a text widget to display actions
    text_widget = ctk.CTkTextbox(main_frame, height=150)
    text_widget.pack(fill="x", pady=(0, 20))
    text_widget.insert("1.0", "Action Log:\n" + "="*50 + "\n")
    text_widget.configure(state="disabled")

    def log_action(action):
        """Helper function to log actions to the text widget"""
        text_widget.configure(state="normal")
        text_widget.insert("end", f"• {action}\n")
        text_widget.see("end")
        text_widget.configure(state="disabled")

    # Define button styles
    primary_style = {"fg_color": "#007acc", "hover_color": "#005a9e"}
    success_style = {"fg_color": "#28a745", "hover_color": "#218838"}
    warning_style = {"fg_color": "#ffc107",
                     "hover_color": "#e0a800", "text_color": "#000"}
    danger_style = {"fg_color": "#dc3545", "hover_color": "#c82333"}

    # Button callback functions
    def save_callback():
        log_action("Save button clicked - Data saved successfully")

    def load_callback():
        log_action("Load button clicked - Data loaded from file")

    def delete_callback():
        log_action("Delete button clicked - Item deleted")

    def edit_callback():
        log_action("Edit button clicked - Entering edit mode")

    def refresh_callback():
        log_action("Refresh button clicked - Data refreshed")

    def export_callback():
        log_action("Export button clicked - Data exported to CSV")

    def import_callback():
        log_action("Import button clicked - Data imported from file")

    def settings_callback():
        log_action("Settings button clicked - Opening settings panel")

    def help_callback():
        log_action("Help button clicked - Opening help documentation")

    # Create the first BtnBar with custom styling
    section1_label = ctk.CTkLabel(main_frame, text="Styled Buttons with Groups:",
                                  font=ctk.CTkFont(weight="bold"))
    section1_label.pack(anchor="w", pady=(10, 5))

    btnInfos = [
        BtnConfig("Save", save_callback,
                  style=primary_style, group="file_ops"),
        BtnConfig("Load", load_callback,
                  style=primary_style, group="file_ops"),
        BtnConfig("Delete", delete_callback,
                  style=danger_style, group="file_ops"),
        BtnConfig("Edit", edit_callback,
                  style=warning_style, group="edit_ops"),
    ]

    btnbar1 = BtnBar(main_frame, button_style={"width": 100, "height": 35},
                     pady=10, padx=8)
    btnbar1.pack(fill="x", pady=(0, 10))
    btnbar1.addBtns(btnInfos)

    # Create the second BtnBar with advanced configuration
    section2_label = ctk.CTkLabel(main_frame, text="Advanced Button Configuration:",
                                  font=ctk.CTkFont(weight="bold"))
    section2_label.pack(anchor="w", pady=(10, 5))

    btnbar2 = BtnBar(main_frame)
    btnbar2.pack(fill="x", pady=(0, 10))

    # Add buttons using advanced configuration
    advanced_buttons = [
        BtnConfig(name='Refresh',
                  callback=refresh_callback,
                  style=success_style,
                  group='data_ops',
                  tooltip='Refresh the current data'
                  ),
        BtnConfig(name='Export',
                  callback=export_callback,
                  style=success_style,
                  group='data_ops',
                  tooltip='Export data to file'
                  ),
        BtnConfig(name='Import',
                  callback=import_callback,
                  style=success_style,
                  group='data_ops',
                  tooltip='Import data from file'
                  )
    ]
    btnbar2.addBtns(advanced_buttons)

    # Create the third BtnBar for utility buttons
    section3_label = ctk.CTkLabel(main_frame, text="Utility Buttons:",
                                  font=ctk.CTkFont(weight="bold"))
    section3_label.pack(anchor="w", pady=(10, 5))

    btnbar3 = BtnBar(main_frame)
    btnbar3.pack(fill="x", pady=(0, 20))

    utility_buttons = [
        BtnConfig("Settings", settings_callback, group="utility"),
        BtnConfig("Help", help_callback, group="utility")
    ]
    btnbar3.addBtns(utility_buttons)

    btnbar4 = BtnBar(main_frame)
    btnbar4.pack(fill="x", pady=(0, 20))

    btnbar4.addBtns([
        BtnConfig("Settings", settings_callback, group="utility"),
        BtnConfig(isSeparator=True),
        BtnConfig("Help", help_callback, group="utility"),
        BtnConfig(isLabel=True, name="Label"),
        BtnConfig("Settings", settings_callback, group="utility"),
        BtnConfig(isSeparator=True),
        BtnConfig("Help", help_callback, group="utility"),
    ])

    # Create a control panel for dynamic operations
    control_frame = ctk.CTkFrame(main_frame)
    control_frame.pack(fill="x", pady=(20, 0))

    control_label = ctk.CTkLabel(control_frame, text="Dynamic Controls:",
                                 font=ctk.CTkFont(weight="bold"))
    control_label.pack(anchor="w", pady=(10, 10))

    # Control functions for dynamic operations
    def toggle_file_ops():
        save_button_info = btnbar1.getBtn("Save")
        if save_button_info and save_button_info['button'].cget("state") == "normal":
            btnbar1.disableGroup("file_ops")
            log_action("File operations group disabled")
        elif save_button_info:
            btnbar1.enableGroup("file_ops")
            log_action("File operations group enabled")
        else:
            log_action("Save button not found - cannot toggle file operations")

    def change_save_button_style():
        new_style = {"fg_color": "#6f42c1", "hover_color": "#5a2d91"}
        if btnbar1.updateBtnStyle("Save", new_style):
            log_action("Save button style updated to purple")

    def add_custom_button():
        def custom_callback():
            log_action("Custom button clicked - Performing custom action")

        if not btnbar3.getBtn("Custom"):
            btnbar3.addBtn(BtnConfig("Custom", custom_callback,
                                     style={"fg_color": "#17a2b8"},
                                     group="utility"))
            log_action("Custom button added to utility group")

    def remove_edit_button():
        if btnbar1.removeBtn("Edit"):
            log_action("Edit button removed from file operations")

    def get_button_info():
        info = btnbar1.getBtn("Save")
        if info:
            log_action(
                f"Save button info: Group={info['data'].group}, Enabled={info['data'].enabled}")

    def show_all_buttons():
        all_buttons = btnbar1.getAllBtns()
        log_action(f"BtnBar1 has {len(all_buttons)} buttons total")

    def clear_all_buttons():
        btnbar1.clearBtns()
        log_action("All buttons cleared from BtnBar1")

    # Create control buttons
    control_btnbar = BtnBar(control_frame)
    control_btnbar.pack(fill="x")

    control_buttons = [
        BtnConfig("Toggle File Ops", toggle_file_ops),
        BtnConfig("Change Save Style", change_save_button_style),
        BtnConfig("Add Custom", add_custom_button),
        BtnConfig("Remove Edit", remove_edit_button),
        BtnConfig("Get Button Info", get_button_info),
        BtnConfig("Show All Buttons", show_all_buttons),
        BtnConfig("Clear All", clear_all_buttons)
    ]
    control_btnbar.addBtns(control_buttons)

    # Status label to show current button information
    status_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(size=12))
    status_label.pack(pady=(10, 0))

    def update_status():
        total_buttons = len(btnbar1.getAllBtns()) + \
            len(btnbar2.getAllBtns()) + len(btnbar3.getAllBtns())
        file_ops_buttons = btnbar1.getGroupBtns("file_ops")
        enabled_file_ops = sum(
            1 for btn in file_ops_buttons if btn['data'].enabled)

        status_text = f"Total buttons: {total_buttons} | "
        status_text += f"File ops: {len(file_ops_buttons)} buttons ({enabled_file_ops} enabled)"

        status_label.configure(text=status_text)
        app.after(100, update_status)  # Update every 100ms

    update_status()

    # Initial log message
    log_action("Enhanced BtnBar application started")
    log_action("All enhanced features are available")

    # Start the application
    app.mainloop()


if __name__ == "__main__":
    main()
