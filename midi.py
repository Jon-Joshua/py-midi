from decoder import MidiDecoder
import struct

class Midi:

    def decode(self, file):
        return MidiDecoder().decode(file)
