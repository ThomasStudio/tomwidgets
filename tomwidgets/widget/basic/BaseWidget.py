from tkinter import Frame


class BaseWidget:
    def __init__(self):
        pass

    def show(self):
        if self.visible():
            return

        """Show or hide the frame."""
        config = self.geometryConfig()

        if not config:
            return

        config['function'](**config['kwargs'])

    def hide(self):
        # if not self.visible():
        #     return

        config = self.geometryConfig(self._last_geometry_manager_call)
        if not config:
            return

        if config['function'] == self.pack_configure:
            self.pack_forget()
        elif config['function'] == self.grid_configure:
            self.grid_forget()
        elif config['function'] == self.place_configure:
            self.place_forget()

    def toggle(self):
        """Toggle the visibility of the frame."""
        if self.visible():
            self.hide()
        else:
            self.show()

    def geometryConfig(self, config=None):
        if not hasattr(self, '_geometryConfig'):
            self._geometryConfig = None

        if config is not None:
            self._geometryConfig = config

        return self._geometryConfig

    def visible(self) -> bool:
        """Check if the frame is currently visible."""
        return self.winfo_ismapped()

    def autoFit(self):
        """Auto fit the content of the widget."""
        self.configure(height=0)

    def resize(self, master=None):
        if master is None:
            master = self

        f = Frame(master)
        f.pack()
        master.after(100, f.destroy)

    def resizeGrid(self, master=None):
        if master is None:
            master = self

        f = Frame(master)
        f.grid(row=0, column=0)
        master.after(100, f.destroy)
