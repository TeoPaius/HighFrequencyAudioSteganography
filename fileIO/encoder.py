def messageToBits(message):
    result = []
    for c in message:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bitsToMessage(bitArray):
    chars = []
    for b in range(int(len(bitArray) / 8)):
        byte = bitArray[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

# print(bitsToMessage(messageToBits("aa")))