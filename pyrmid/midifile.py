import pyrmid.events as events

class MidiTrack:

    def __init__(self):
        self.events = []


class MidiFile:

    def __init__(self, format, division):
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
