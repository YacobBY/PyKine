import math
import tkinter as tk

segmentArray = []


class Segment:
    previousSegment = 0
    startX = 0
    startY = 0
    endX = 0
    endY = 0
    rotateAngle = 0

    # constructor
    def __init__(self, segmentLength):

        self.segmentLength = segmentLength

    def setPreviousSegment(self, previousSegment):
        self.previousSegment = previousSegment

    def maxRotationX(self, xDiff):
        print("aa")
        if (xDiff < -40):
            xDiff = -40
        if (xDiff > 40):
            xDiff = 40
        return xDiff;

    def rotateTo(self, x, y):
        xDiff = x - self.startX
        yDiff = y - self.startY
        self.rotateAngle = math.atan2(yDiff, xDiff)
        self.endX = self.startX + math.cos(self.rotateAngle) * self.segmentLength

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
    def __init__(self, totalSegments, beginX, beginY, graphics):
        self.amountOfSegments = totalSegments
        self.startX = beginX
        self.startY = beginY
        self.canvas = graphics

    def addNewSegment(self):
        segment = Segment(50)  # segment length
        if (self.previousSegment == 0):
            segment.startX = self.startX
            segment.startY = self.startY
        else:
            segment.startX = self.previousSegment.endX
            segment.startY = self.previousSegment.endY
            segment.setPreviousSegment(self.previousSegment)
        self.segments.append(segment)
        self.previousSegment = segment

    def addSegment(self):
        for segment in segmentArray:
            self.addNewSegment()

    def update(self, x, y):
        self.previousSegment.placeSegment(x.y)
        for segment in segmentArray:
            if segment.previousSegment ==0:
                segment.startX = self.startX
                segment.startY = self.startY
            else:
                segment.startX = segment.previousSegment.endX
                segment.startY = segment.previousSegment.endY


def drawLine(event):


    canvas.delete("all")
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        
        canvas.create_line(200, 200, x1, y1)
    canvas.old_coords = x, y


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.old_coords = None

root.bind('<Motion>', drawLine)
root.mainloop()