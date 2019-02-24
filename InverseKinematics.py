from Segment import Segment


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
        segment = Segment(60)  # segment length
        if (self.previousSegment == 0):
            segment.startX = self.startX
            segment.startY = self.startY
        else:
            segment.startX = self.previousSegment.endX
            segment.startY = self.previousSegment.endY
            segment.setPreviousSegment(self.previousSegment)
        self.previousSegment = segment
        self.segments.append(segment)

    def addSegments(self):
        for x in range(0, self.amountOfSegments):
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
