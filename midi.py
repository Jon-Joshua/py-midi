from header import MidiHeader
from track import MidiTrack
import struct

class Midi:

    def __init__(self, file):
        self.file = file
        self.format, self.tracks, self.division = self._read_header(self.file)
        # print(self.format)

        tracks_l = []

        if self.format == 0:
            pass
        else:
            for x in range(self.tracks):
                tracks_l.append(self._read_track(self.file))
        

    def _read_header(self, file):
        header, length = self._get_chunk(file)

        if header != b'MThd':
            raise EOFError

        data = self._read_bytes(file, length)
        return struct.unpack('>3h', data)


    def _read_track(self, file):
        header, length = self._get_chunk(file)

        if header != b'MTrk':
            return


    def _read_variable_len(self, file, pos):




    def _read_bytes(self, file, length):
        return file.read(length)


    def _get_chunk(self, file):
        header = self._read_bytes(file, 8)
        return struct.unpack('>4sI', header)