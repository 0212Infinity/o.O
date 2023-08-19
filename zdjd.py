import random

zdjd_char = {'0': 'o.O', '1': 'ÖwÖ', '2': 'OvO', '3': 'Övo', '4': 'O.Ö', '5': 'o_o', '6': 'Ö.0', '7': '0_O', '8': 'Ö.o',
             '9': 'Ow0', 'A': 'ovÖ', 'B': 'Ö_Ö', 'C': 'ovO', 'D': 'owo', 'E': 'o.Ö', 'F': '0_Ö', 'G': '0.o', 'H': 'o_Ö',
             'I': '0w0', 'J': '0_o', 'K': '0_0', 'L': 'o_O', 'M': '0.0', 'N': 'o.0', 'O': '0wo', 'P': 'Ö_o', 'Q': 'ÖvO',
             'R': 'ÖvÖ', 'S': '0wÖ', 'T': '0v0', 'U': 'O.O', 'V': 'owO', 'W': '0vo', 'X': 'Ö_0', 'Y': 'owÖ', 'Z': 'Öv0',
             'a': '0wO', 'b': 'Öwo', 'c': 'Ö_O', 'd': 'Ov0', 'e': 'O.o', 'f': 'O_0', 'g': 'ov0', 'h': 'Ovo', 'i': 'O_Ö',
             'j': 'ow0', 'k': 'Owo', 'l': 'Öw0', 'm': 'ÖwO', 'n': 'O_o', 'o': '0vÖ', 'p': 'O_O', 'q': 'OwO', 'r': '0.Ö',
             's': 'OwÖ', 't': 'ovo', 'u': 'o_0', 'v': 'Ö.O', 'w': 'o.o', 'x': 'O.0', 'y': '0vO', 'z': 'Ö.Ö'}

zdjd_char2 = {'o.O': '0', 'ÖwÖ': '1', 'OvO': '2', 'Övo': '3', 'O.Ö': '4', 'o_o': '5', 'Ö.0': '6', '0_O': '7',
              'Ö.o': '8', 'Ow0': '9', 'ovÖ': 'A', 'Ö_Ö': 'B', 'ovO': 'C', 'owo': 'D', 'o.Ö': 'E', '0_Ö': 'F',
              '0.o': 'G', 'o_Ö': 'H', '0w0': 'I', '0_o': 'J', '0_0': 'K', 'o_O': 'L', '0.0': 'M', 'o.0': 'N',
              '0wo': 'O', 'Ö_o': 'P', 'ÖvO': 'Q', 'ÖvÖ': 'R', '0wÖ': 'S', '0v0': 'T', 'O.O': 'U', 'owO': 'V',
              '0vo': 'W', 'Ö_0': 'X', 'owÖ': 'Y', 'Öv0': 'Z', '0wO': 'a', 'Öwo': 'b', 'Ö_O': 'c', 'Ov0': 'd',
              'O.o': 'e', 'O_0': 'f', 'ov0': 'g', 'Ovo': 'h', 'O_Ö': 'i', 'ow0': 'j', 'Owo': 'k', 'Öw0': 'l',
              'ÖwO': 'm', 'O_o': 'n', '0vÖ': 'o', 'O_O': 'p', 'OwO': 'q', '0.Ö': 'r', 'OwÖ': 's', 'ovo': 't',
              'o_0': 'u', 'Ö.O': 'v', 'o.o': 'w', 'O.0': 'x', '0vO': 'y', 'Ö.Ö': 'z'}


def generate_zdjd_char():
    """
    用于生成字符映射集
    """
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    first = ['0', 'o', 'O', 'Ö']
    second = ['.', '_', 'v', 'w']
    third = ['0', 'o', 'O', 'Ö']
    result = []
    for f in first:
        for s in second:
            for t in third:
                result.append(f + s + t)
    # 打乱顺序
    random.shuffle(result)

    # 映射字典
    key_mapping = {}
    value_mapping = {}
    for i, ch in enumerate(characters):
        key_mapping[ch] = result[i]
        value_mapping[result[i]] = ch
    print(key_mapping)
    print(value_mapping)


def encode(human_language_str):
    utf8_bytes = human_language_str.encode('utf-8')
    result = ''
    for byte in ' '.join(format(byte, '02X') for byte in utf8_bytes):
        if zdjd_char.get(byte) is not None:
            result += zdjd_char[byte]
        else:
            result += byte
    return result


def decode(zdjd_language_str):
    hex_string = ''
    for word in zdjd_language_str.split():
        for i in range(0, len(word), 3):
            hex_string += zdjd_char2[word[i:i + 3]]
        hex_string += ' '
    # 将十六进制字符串分割成字节的十六进制表示列表
    hex_list = hex_string.split()
    # 将十六进制表示转换为整数字节列表
    byte_list = [int(hex_byte, 16) for hex_byte in hex_list]
    # 创建字节序列
    utf8_bytes = bytes(byte_list)
    # 解码字节序列为Unicode字符串
    return utf8_bytes.decode('utf-8')


if __name__ == '__main__':
    encode_str = encode("HELLO WORD!😀 😃 😄 😁 😆 😅 😂 🤣")
    print(encode_str)
    print(decode(encode_str))
