import math


class Segment:
    startX = 0
    startY = 0
    endX = 0
    endY = 0
    rotateAngle = 0
    previousSegment = 0
    segmentLength = 0

    # constructor
    def __init__(self, segmentLen):
        self.segmentLength = segmentLen

    def maxRotationX(self, xDiff):
        if (xDiff < -200):
            xDiff = -200
        if (xDiff > 200):
            xDiff = 200
        return xDiff

    def maxRotationY(self, yDiff):
        if (yDiff < -200):
            yDiff = -200
        if (yDiff > 200):
            yDiff = 200
        return yDiff

    def setPreviousSegment(self, previousSegment):
        self.previousSegment = previousSegment

    def rotateTo(self, x, y):
        xDiff = self.maxRotationX(x - self.startX)
        yDiff = self.maxRotationX(y - self.startY)
        self.rotateAngle = math.atan2(yDiff, xDiff)
        self.endX = self.startX + math.cos(self.rotateAngle) * self.segmentLength
        self.endY = self.startY + math.sin(self.rotateAngle) * self.segmentLength

    def placeSegment(self, x, y):
        self.rotateTo(x, y)
        self.startX = x - math.cos(self.rotateAngle) * self.segmentLength
        self.startY = y - math.cos(self.rotateAngle) * self.segmentLength

        if self.previousSegment != 0:
            self.previousSegment.placeSegment(self.startX, self.startY)
