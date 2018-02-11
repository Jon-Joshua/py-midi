import events

class MidiTrack:

    def __init__(self):
        self.title = None
        self.copyright = None
        self.bpm = 120
        self.events = []
        self.pan = 0
        self.instrument = 0


class MidiFile:

    def __init__(self, format, division):
        self.title = None
        self.format = format
        self.division = division
        self.tracks = []


class MidiEvent:

    def __init__(self, delta, channel, event, message, type):
        self.type = type
        self.delta = delta
        self.channel = channel
        self.event = event
        self.message = message


    def get_name(self):
        return events.get_event_name(self.event, self.type)