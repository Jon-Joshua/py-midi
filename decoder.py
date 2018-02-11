import struct
from midifile import MidiFile, MidiTrack
import events
import io

class MidiDecoder:

    def __init__(self):
        pass


    def decode(self, file):
        self.file = file
        byte_s = io.BytesIO(file.read())

        format, tracks, division = self._read_header(byte_s)

        self.midi_file = MidiFile(format, division)

        tracks_l = self._get_tracks(file, tracks)

        if format == 0:
            pass
        else:
            for x in range(2):
                print(x)
                track = self._read_track(tracks_l[x])
                self.midi_file.tracks.append(track)
        
        return self.midi_file


    def _read_header(self, file):
        header, length = self._get_chunkb(file)

        if header != b'MThd':
            raise EOFError

        data = self._read_bytesb(file, length)
        return struct.unpack('>3h', data)


    """ Gets track from 'MTrk' start to 0xFF 0x2F 0x00 end. 
        Ugly as hell...
    """
    def _get_tracks(self, file, tracks):

        tracks_list = []

        for x in range(tracks):
            mtrk_bytes = []

            start = None
            end = None

            file.seek(0)
            cycle = 0

            while True:
                if start == None:
                    byte = file.read(1)

                    if len(mtrk_bytes) == 4:
                        mtrk_bytes.pop(0)
                    mtrk_bytes.append(byte)

                    if b''.join(mtrk_bytes) == b'MTrk':
                        if x == cycle:
                            start = file.tell() - 4
                        else:
                            cycle += 1
                else:
                    byte = self._read_byte_i(file)

                    if byte == 0xFF:
                        if self._read_byte_i(file) == 0x2F:
                            end = file.tell() + 1
                            break

            length = end - start
            file.seek(start)
            tracks_list.append(io.BytesIO(file.read(length)))

        return tracks_list


    def _read_track(self, bytes):
        header, length = self._get_chunkb(bytes)

        if header != b'MTrk':
            return

        track = MidiTrack()

        start = bytes.tell()
        prev_val = None

        while True:
            delta = self._read_vlenb(bytes)
            next_val = int.from_bytes(self._read_bytesb(bytes, 1), byteorder='big')

            if next_val == 0xFF: # Meta Event
                self._decode_meta(bytes, track)
            else:
                self._decode_event(bytes, track, next_val, prev_val)
 
            prev_val = next_val

            # If current pos - start pos equals specified track length, break.
            eot = (bytes.tell() - start) == length
            if eot:
                print('End of track')
                break

        return track


    def _decode_event(self, file, track, val, prev_val):
        event, channel = val >> 4, val & 0xF

        # List of valid events
        event_l = [ 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE ]

        if event in event_l:
            events._process(file, event, track)
        else:
            # If event isn't in list of events process the next event as a continuation of the previous event.
            event, channel = prev_val >> 4, prev_val & 0xF
            events._process(file, event, track)


    def _decode_meta(self, file, track):
        meta_type = self._read_byteb(file)
        meta_length = self._read_vlenb(file)
        meta_data = self._read_bytesb(file, meta_length)

        # print('Type: {}, Length: {}, Data: {}'.format(hex(meta_type), meta_length ,meta_data))

        if meta_type == 0x00:
            pass
        elif meta_type == 0x01:
            pass
        elif meta_type == 0x02:
            track.copyright = meta_data
        elif meta_type == 0x03:
            track.title = meta_data.decode('utf-8')
        elif meta_type == 0x51: # BPM
            track.bpm = 60000000 / int(meta_data.hex(), 16)
        elif meta_type == 0x58:
            key_sig = struct.unpack('>4b', meta_data)
        elif meta_type == 0x59:
            key_sig = struct.unpack('>2B', meta_data)


    def _read_byteb(self, byte_s):
        return byte_s.read(1)


    def _read_byte_i(self, byte_s):
        return int.from_bytes(byte_s.read(1), byteorder='big')


    def _read_bytesb(self, byte_s, length):
        string = b''
        for x in range(length):
            byte = self._read_byteb(byte_s)
            string += byte
        return string


    def _get_chunkb(self, byte_s):
        header = self._read_bytesb(byte_s, 8)
        print(header)
        return struct.unpack('>4sI', header)


    def _read_vlenb(self, byte_s):
        value = 0x00
        while True:
            byte = self._read_byteb(byte_s)
            value += int.from_bytes(byte, byteorder='big')

            if byte != 0x80:
                break
        return value
