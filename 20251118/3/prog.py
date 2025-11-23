import sys
import struct


def parse_wav_header(path: str):
    try:
        with open(path, "rb") as f:
            header = f.read(44)
    except OSError:
        return None

    if len(header) < 44:
        return None

    if header[0:4] != b"RIFF":
        return None
    if header[8:12] != b"WAVE":
        return None
    if header[12:16] != b"fmt ":
        return None
    if header[36:40] != b"data":
        return None

    size, = struct.unpack("<I", header[4:8])    
    audio_type, = struct.unpack("<H", header[20:22])
    channels, = struct.unpack("<H", header[22:24])
    rate, = struct.unpack("<I", header[24:28])   
    bits, = struct.unpack("<H", header[34:36])        
    data_size, = struct.unpack("<I", header[40:44])   

    return size, audio_type, channels, rate, bits, data_size



filename = sys.stdin.readline().strip()

info = parse_wav_header(filename)
if info is None:
    print("NO")
else:
    size, audio_type, channels, rate, bits, data_size = info
    print(
        f"Size={size}, Type={audio_type}, "
        f"Channels={channels}, Rate={rate}, "
        f"Bits={bits}, Data size={data_size}"
    )



