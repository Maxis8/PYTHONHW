# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('decode.txt', 'w') as data:
    data.write('ffffggghhhllloorrr')

with open('decode.txt', 'r') as data:
    string = data.readline()

def encode_str(decode):
    encode = ''
    count = 1
    res = decode[0]
    for i in range(1, len(decode)):
        if decode[i] == res:
            count += 1
        else:
            encode = encode + str(count) + res
            res = decode[i]
            count = 1
            encode = encode + str(count) + res
    return encode

def decode_srt(encode):
    decoded = ''
    result = ''
    for i in range(len(encode)):
        if encode[i].isdigit():
            result += encode[i]
        else:
            decoded += encode[i] * int(result)
        result = ''
    print(decoded)

    return decoded

with open('decode.txt', 'r') as file:
    decoded = file.read()
with open('encode.txt', 'w') as file:
    encoded = encode_str(decoded)
    file.write(encoded)
print('Decoded: ' + decoded)
print('Encoded: ' + encode_str(decoded))
print(f'Compress ratio: {round(len(decoded) / len(encoded), 1)}')
