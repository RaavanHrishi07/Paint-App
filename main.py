import tkinter as tk
from tkinter import colorchooser, simpledialog
from tkinter import font as tkfont


CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600
BACKGROUND_COLOR = "white"


class PaintApp:
    """Simple Tkinter paint application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Python Paint")
        self.root.geometry("1000x700")
        self.root.minsize(700, 500)

        self.current_tool = "pencil"
        self.current_color = "black"
        self.line_width = 3

        self.start_x = None
        self.start_y = None
        self.preview_item = None

        self._build_interface()
        self._bind_events()

    def _build_interface(self):
        """Create the application interface."""
        toolbar = tk.Frame(self.root, padx=8, pady=8)
        toolbar.pack(fill=tk.X)

        tools = [
            ("Pencil", "pencil"),
            ("Line", "line"),
            ("Rectangle", "rectangle"),
            ("Oval", "oval"),
            ("Arc", "arc"),
            ("Text", "text"),
        ]

        for label, tool in tools:
            tk.Button(
                toolbar,
                text=label,
                command=lambda selected_tool=tool: self.select_tool(
                    selected_tool
                ),
            ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            toolbar,
            text="Colour",
            command=self.choose_color,
        ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            toolbar,
            text="Clear",
            command=self.clear_canvas,
        ).pack(side=tk.LEFT, padx=3)

        tk.Button(
            toolbar,
            text="Exit",
            command=self.root.destroy,
        ).pack(side=tk.RIGHT, padx=3)

        self.status_label = tk.Label(
            toolbar,
            text="Tool: Pencil",
            anchor="w",
        )
        self.status_label.pack(side=tk.LEFT, padx=15)

        self.canvas = tk.Canvas(
            self.root,
            background=BACKGROUND_COLOR,
            cursor="crosshair",
        )
        self.canvas.pack(
            fill=tk.BOTH,
            expand=True,
            padx=8,
            pady=(0, 8),
        )

    def _bind_events(self):
        """Bind mouse events to the drawing canvas."""
        self.canvas.bind(
            "<ButtonPress-1>",
            self.on_mouse_down,
        )
        self.canvas.bind(
            "<B1-Motion>",
            self.on_mouse_drag,
        )
        self.canvas.bind(
            "<ButtonRelease-1>",
            self.on_mouse_up,
        )

    def select_tool(self, tool):
        """Select the active drawing tool."""
        self.current_tool = tool
        self.status_label.config(
            text=f"Tool: {tool.title()}"
        )

    def choose_color(self):
        """Open the colour picker."""
        selected_color = colorchooser.askcolor(
            title="Choose drawing colour",
            initialcolor=self.current_color,
        )

        if selected_color[1]:
            self.current_color = selected_color[1]

    def clear_canvas(self):
        """Remove every drawing from the canvas."""
        self.canvas.delete("all")

    def on_mouse_down(self, event):
        """Handle the beginning of a mouse action."""
        self.start_x = event.x
        self.start_y = event.y
        self.preview_item = None

        if self.current_tool == "pencil":
            self.last_x = event.x
            self.last_y = event.y

    def on_mouse_drag(self, event):
        """Handle mouse movement while the left button is held."""
        if self.current_tool == "pencil":
            self.canvas.create_line(
                self.last_x,
                self.last_y,
                event.x,
                event.y,
                fill=self.current_color,
                width=self.line_width,
                capstyle=tk.ROUND,
                smooth=True,
            )

            self.last_x = event.x
            self.last_y = event.y

        elif self.current_tool in {
            "line",
            "rectangle",
            "oval",
            "arc",
        }:
            self._draw_preview(event)

    def on_mouse_up(self, event):
        """Handle the end of a mouse action."""
        if self.start_x is None or self.start_y is None:
            return

        if self.current_tool == "text":
            self._add_text(event)

        elif self.current_tool == "line":
            self.canvas.create_line(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                fill=self.current_color,
                width=self.line_width,
            )

        elif self.current_tool == "rectangle":
            self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                outline=self.current_color,
                width=self.line_width,
            )

        elif self.current_tool == "oval":
            self.canvas.create_oval(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                outline=self.current_color,
                width=self.line_width,
            )

        elif self.current_tool == "arc":
            self.canvas.create_arc(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                start=0,
                extent=150,
                style=tk.ARC,
                outline=self.current_color,
                width=self.line_width,
            )

        if self.preview_item is not None:
            self.canvas.delete(self.preview_item)
            self.preview_item = None

        self.start_x = None
        self.start_y = None

    def _draw_preview(self, event):
        """Display a temporary shape while dragging."""
        if self.preview_item is not None:
            self.canvas.delete(self.preview_item)

        if self.current_tool == "line":
            self.preview_item = self.canvas.create_line(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                fill=self.current_color,
                width=self.line_width,
                dash=(4, 2),
            )

        elif self.current_tool == "rectangle":
            self.preview_item = self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                outline=self.current_color,
                width=self.line_width,
                dash=(4, 2),
            )

        elif self.current_tool == "oval":
            self.preview_item = self.canvas.create_oval(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                outline=self.current_color,
                width=self.line_width,
                dash=(4, 2),
            )

        elif self.current_tool == "arc":
            self.preview_item = self.canvas.create_arc(
                self.start_x,
                self.start_y,
                event.x,
                event.y,
                start=0,
                extent=150,
                style=tk.ARC,
                outline=self.current_color,
                width=self.line_width,
                dash=(4, 2),
            )

    def _add_text(self, event):
        """Ask for text and place it on the canvas."""
        text = simpledialog.askstring(
            "Add Text",
            "Enter the text:",
            parent=self.root,
        )

        if text:
            text_font = tkfont.Font(
                family="Arial",
                size=18,
                weight="bold",
            )

            self.canvas.create_text(
                event.x,
                event.y,
                text=text,
                fill=self.current_color,
                font=text_font,
                anchor=tk.NW,
            )


def main():
    root = tk.Tk()
    PaintApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    