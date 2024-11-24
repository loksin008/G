import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        self.root.geometry("800x600")

        self.color = "black"
        self.brush_size = 5

        # Create Canvas
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)

        # Create UI elements for color, brush size, and clear
        self.create_tools()

    def create_tools(self):
        tool_frame = tk.Frame(self.root)
        tool_frame.pack()

        color_btn = tk.Button(tool_frame, text="Color", command=self.change_color)
        color_btn.grid(row=0, column=0)

        clear_btn = tk.Button(tool_frame, text="Clear", command=self.clear_canvas)
        clear_btn.grid(row=0, column=1)

        self.brush_size_slider = tk.Scale(tool_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Brush Size")
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.grid(row=0, column=2)

    def paint(self, event):
        brush_size = self.brush_size_slider.get()
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def change_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
      
