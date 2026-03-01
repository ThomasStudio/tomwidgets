from tkinter import Widget


class Dragging:
    def __init__(self, *widgets: Widget):
        for w in widgets:
            self._make_draggable(w)

    def bindDraggable(self, *widgets: Widget):
        for w in widgets:
            self._make_draggable(w)

    def bindDraggableAll(self, widget: Widget):
        """bind widget and all its children"""
        self.bindDraggable(widget)
        for child in widget.winfo_children():
            self.bindDraggable(child)

    def _make_draggable(self, widget: Widget):
        widget.bind("<ButtonPress-1>", self._start_dragging)
        widget.bind("<ButtonRelease-1>", self._stop_dragging)

    def _dragging(self, event):
        widget = event.widget
        top = widget.winfo_toplevel()
        new_x = event.x_root - widget._offset_x
        new_y = event.y_root - widget._offset_y
        top.geometry(f"+{new_x}+{new_y}")

    def _start_dragging(self, event):
        widget = event.widget
        top = widget.winfo_toplevel()
        widget._offset_x = event.x_root - top.winfo_x()
        widget._offset_y = event.y_root - top.winfo_y()
        widget.bind("<B1-Motion>", self._dragging)

    def _stop_dragging(self, event):
        widget = event.widget
        widget.unbind("<B1-Motion>")


def test():
    from .Tk import Tk
    from .Frame import Frame
    root = Tk()
    root.geometry("300x200")
    root.title("Dragging Test")

    frame = Frame(root, fg_color="red", border_width=10, bg_color="black",
                  border_color="green", corner_radius=20, width=100, height=100)
    frame.place(x=0, y=0)

    frame2 = Frame(root, fg_color="blue", width=100, height=100)
    frame2.place(x=100, y=100)

    dragging = Dragging(frame, frame2)

    root.mainloop()


if __name__ == "__main__":
    test()
