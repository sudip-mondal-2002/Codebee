from Error import *
class Number:
    def __init__(self, value):
        self.value = value
        self.setPos()
        self.setContext()

    def setPos(self, start_pos=None, end_pos=None):
        self.pos_start = start_pos
        self.pos_end = end_pos
        return self

    def setContext(self, context=None):
        self.context = context
        return self

    def addedTo(self, other):
        if isinstance(other, Number):
            return Number(self.value+other.value).setContext(self.context), None

    def subbedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value-other.value).setContext(self.context), None

    def multiTo(self, other):
        if isinstance(other, Number):
            return Number(self.value*other.value).setContext(self.context), None

    def divideBy(self, other):
        if isinstance(other, Number):
            if other.value != 0:
                return Number(self.value/other.value).setContext(self.context), None
            return None, RunTimeError(other.pos_start, other.pos_end, "Division by zero error", self.context)

    def poweredTo(self, other):
        if isinstance(other, Number):
            if self.value == 0 and other.value <= 0:
                return None, RunTimeError(other.pos_start, other.pos_end, "Only positive power of zero is defined", self.context)
            if self.value < 0 and other.value != int(other.value):
                return None, RunTimeError(other.pos_start, other.pos_end, "Fractional power to negatives are defined", self.context)
            return Number(self.value**other.value).setContext(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.setPos(self.pos_start, self.pos_end)
        copy.setContext(self.context)
        return copy

    def __repr__(self):
        return str(self.value)
