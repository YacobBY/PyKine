import tkinter as tk

from InverseKinematics import InverseKinematics

IK = InverseKinematics(3, 250, 250)


def drawLine(event):
    mouseX, mouseY = event.x, event.y

    IK.update(mouseX, mouseY)
    segments = IK.segments
    canvas.delete("all")
    for segment in segments:
        canvas.create_line(segment.startX, segment.startY, segment.endX, segment.endY)


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
canvas.old_coords = None
root.bind('<Motion>', drawLine)
root.mainloop()
