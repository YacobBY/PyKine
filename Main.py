import tkinter as tk

from InverseKinematics import InverseKinematics

IK = InverseKinematics(3, 400, 400)


def drawLine(event):
    # def __init__(self, totalSegments, beginX, beginY, graphics):
    mouseX, mouseY = event.x, event.y

    IK.update(mouseX, mouseY)
    segments = IK.segments
    canvas.delete("all")
    for segment in segments:
        canvas.create_line(segment.startX, segment.startY, segment.endX, segment.endY)


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
canvas.old_coords = None
root.bind('<Motion>', drawLine)
root.mainloop()
