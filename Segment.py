import math
import tkinter as tk


class Segment:
    startX = 0
    startY = 0
    endX = 0
    endY = 0
    rotateAngle = 0
    previousSegment = 0
    segmentLength = 50

    # constructor
    def __init__(self, segmentLen):
        self.segmentLength = segmentLen

    def setPreviousSegment(self, previousSegment):
        self.previousSegment = previousSegment

    def rotateTo(self, x, y):
        xDiff = x - self.startX
        yDiff = y - self.startY
        self.rotateAngle = math.atan2(yDiff, xDiff)
        self.endX = self.startX + math.cos(self.rotateAngle) * self.segmentLength
        self.endY = self.startY + math.sin(self.rotateAngle) * self.segmentLength

    def placeSegment(self, x, y):
        self.rotateTo(x, y)
        self.startX = x - math.cos(self.rotateAngle) * self.segmentLength
        self.startY = y - math.cos(self.rotateAngle) * self.segmentLength

        if self.previousSegment != 0:
            self.previousSegment.placeSegment(self.startX, self.startY)


class InverseKinematics:
    amountOfSegments = 0
    previousSegment = 0
    startX = 0
    startY = 0
    segments = []

    # Constructor
    def __init__(self, totalSegments, beginX, beginY):
        self.amountOfSegments = totalSegments
        self.startX = beginX
        self.startY = beginY
        self.addSegments()

    def addNewSegment(self):
        print("add new seg")
        segment = Segment(50)  # segment length
        if (self.previousSegment == 0):
            segment.startX = self.startX
            segment.startY = self.startY
        else:
            segment.startX = self.previousSegment.endX
            segment.startY = self.previousSegment.endY
            segment.setPreviousSegment(self.previousSegment)
        self.segments.append(segment)
        print(segment.startX, segment.startY)
        print(segment.endX, segment.endY)
        self.previousSegment = segment

    def addSegments(self):
        for x in range(0, self.amountOfSegments):
            print(x)
            self.addNewSegment()

    def update(self, x, y):
        self.previousSegment.placeSegment(x, y)
        for segment in self.segments:
            if segment.previousSegment == 0:
                segment.startX = self.startX
                segment.startY = self.startY
            else:
                segment.startX = segment.previousSegment.endX
                segment.startY = segment.previousSegment.endY

IK = InverseKinematics(3, 200, 200)
def drawLine(event):
    # def __init__(self, totalSegments, beginX, beginY, graphics):
    mouseX, mouseY = event.x, event.y

    IK.update(mouseX,mouseY)
    segments = IK.segments
    canvas.delete("all")
    # print("start line")

    if canvas.old_coords:
        x1, y1 = canvas.old_coords

        print(segments.__len__())
        for segment in segments:
            canvas.create_line(segment.startY, 200, mouseX, mouseY)
            # print("drawing segment line", segment.startY)

        canvas.create_line(200, 200, x1, y1)
    canvas.old_coords = mouseX, mouseY


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

root.bind('<Motion>', drawLine)
root.mainloop()
