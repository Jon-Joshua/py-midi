class MidiTrack:

    def __init__(self):
        self.title = None
        self.copyright = None
        self.bpm = 120
        self.tracks = []
        self.notes = []

        self.pan = 0
        self.instrument = 0