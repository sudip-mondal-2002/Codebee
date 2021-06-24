class RTResult:
    def __init__(self):
        self.value = None
        self.err = None

    def register(self, res):
        if res.err:
            self.err = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.err = error
        return self
