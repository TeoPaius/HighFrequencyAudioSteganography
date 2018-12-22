import wave, struct

normalizationFactor = 32767.0
# normalizationFactor = 1


def read_whole(filename):
    print("READING FILE ...")
    wav_r = wave.open(filename, 'r')
    print(wav_r.getparams())
    ret = []
    while wav_r.tell() < wav_r.getnframes():
        decoded = struct.unpack("<hh", wav_r.readframes(1))
        ret.append([i/normalizationFactor for i in decoded])
    return ret, wav_r.getparams()

def write_whole(filename,params, frames):
    print("WRITING FILE ...")
    waveFin = wave.open(filename, 'w')
    waveFin.setparams(params)
    print(waveFin.getparams())
    for i in frames:
        data = struct.pack('<hh', int(i[0]*normalizationFactor), int(i[1]*normalizationFactor))
        waveFin.writeframesraw(data)
    waveFin.writeframes(b'')

