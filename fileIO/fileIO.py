import wave, struct

normalizationFactor = 32767.0
# normalizationFactor = 1


def read_whole(filename, duration=-1):
    print("READING FILE ...")
    wav_r = wave.open(filename, 'r')
    print(wav_r.getparams())

    if duration != -1:
        nrFrames = duration * wav_r.getframerate()
    else:
        nrFrames = wav_r.getnframes()
    ret = []
    while wav_r.tell() < nrFrames:
        decoded = struct.unpack("<hh", wav_r.readframes(1))
        ret.append([i/normalizationFactor for i in decoded])
    print("DONE READING FILE")
    return ret, wav_r.getparams()

def write_whole(filename,params,frames):
    print("WRITING FILE ...")
    waveFin = wave.open(filename, 'w')
    waveFin.setparams(params)
    print(waveFin.getparams())
    for i in frames:
        data = struct.pack('<hh', int(i[0]*normalizationFactor), int(i[1]*normalizationFactor))
        waveFin.writeframesraw(data)
    waveFin.writeframes(b'')
    print("DONE WRITING FILE...")

