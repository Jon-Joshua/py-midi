class MidiTrack:

    def __init__(self):
        self.title = None
        self.copyright = None
        self.bpm = 120
        self.notes = []

        self.pan = 0
        self.instrument = 0


class MidiFile:

    def __init__(self, format, division):
        self.title = None

        self.format = format
        # self.tracks = tracks
        self.division = division

        self.tracks = []


class MidiNote:

    def __init__(self, note, velocity):
        self.note = note
        self.velocity = velocity