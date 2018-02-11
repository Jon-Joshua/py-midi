class MidiFile:

    def __init__(self, format, division):
        self.title = None

        self.format = format
        # self.tracks = tracks
        self.division = division

        self.tracks = []