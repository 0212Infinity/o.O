import random

zdjd_char = {'0': 'O.0', '1': 'Ö_o', '2': 'o.0', '3': 'Ow0', '4': 'owO', '5': 'ov0', '6': 'ÖwO', '7': '0.o', '8': 'o_O',
             '9': 'Öwo', 'A': 'o_0', 'B': 'ovO', 'C': 'Öv0', 'D': 'OwÖ', 'E': 'O_O', 'F': '0v0', 'G': 'OvÖ', 'H': 'Ö_O',
             'I': '0wÖ', 'J': 'Owo', 'K': 'owo', 'L': 'Ö_Ö', 'M': 'owÖ', 'N': 'Ö.0', 'O': 'ovÖ', 'P': 'O_o', 'Q': '0.0',
             'R': '0.Ö', 'S': 'Ov0', 'T': '0wO', 'U': '0_Ö', 'V': '0wo', 'W': '0_o', 'X': 'Ö.O', 'Y': '0_0', 'Z': 'ow0',
             'a': 'o.o', 'b': 'Övo', 'c': 'O_0', 'd': 'o_o', 'e': 'Ovo', 'f': 'OwO', 'g': 'o_Ö', 'h': '0vo', 'i': 'ÖvÖ',
             'j': 'O.o', 'k': 'Ö.Ö', 'l': 'Ö.o', 'm': '0.O', 'n': 'o.Ö', 'o': '0vO', 'p': 'ovo', 'q': '0_O', 'r': 'ÖvO',
             's': '0vÖ', 't': 'O.O', 'u': 'ÖwÖ', 'v': 'O.Ö', 'w': 'Öw0', 'x': 'Ö_0', 'y': 'OvO', 'z': '0w0', ' ': 'O_Ö'}

zdjd_char2 = {'O.0': '0', 'Ö_o': '1', 'o.0': '2', 'Ow0': '3', 'owO': '4', 'ov0': '5', 'ÖwO': '6', '0.o': '7',
              'o_O': '8', 'Öwo': '9', 'o_0': 'A', 'ovO': 'B', 'Öv0': 'C', 'OwÖ': 'D', 'O_O': 'E', '0v0': 'F',
              'OvÖ': 'G', 'Ö_O': 'H', '0wÖ': 'I', 'Owo': 'J', 'owo': 'K', 'Ö_Ö': 'L', 'owÖ': 'M', 'Ö.0': 'N',
              'ovÖ': 'O', 'O_o': 'P', '0.0': 'Q', '0.Ö': 'R', 'Ov0': 'S', '0wO': 'T', '0_Ö': 'U', '0wo': 'V',
              '0_o': 'W', 'Ö.O': 'X', '0_0': 'Y', 'ow0': 'Z', 'o.o': 'a', 'Övo': 'b', 'O_0': 'c', 'o_o': 'd',
              'Ovo': 'e', 'OwO': 'f', 'o_Ö': 'g', '0vo': 'h', 'ÖvÖ': 'i', 'O.o': 'j', 'Ö.Ö': 'k', 'Ö.o': 'l',
              '0.O': 'm', 'o.Ö': 'n', '0vO': 'o', 'ovo': 'p', '0_O': 'q', 'ÖvO': 'r', '0vÖ': 's', 'O.O': 't',
              'ÖwÖ': 'u', 'O.Ö': 'v', 'Öw0': 'w', 'Ö_0': 'x', 'OvO': 'y', '0w0': 'z', 'O_Ö': ' '}


def encode(human_language_str):
    utf8_bytes = human_language_str.encode('utf-8')
    result = ''
    for byte in ' '.join(format(byte, '02X') for byte in utf8_bytes):
        if zdjd_char.get(byte) is not None:
            result += zdjd_char[byte]
        else:
            result += byte
        result += ' '
    return result


def decode(zdjd_language_str):
    hex_string = ''
    for word in zdjd_language_str.split():
        hex_string += zdjd_char2[word]
    # 将十六进制字符串分割成字节的十六进制表示列表
    hex_list = hex_string.split()
    # 将十六进制表示转换为整数字节列表
    byte_list = [int(hex_byte, 16) for hex_byte in hex_list]
    # 创建字节序列
    utf8_bytes = bytes(byte_list)
    # 解码字节序列为Unicode字符串
    return utf8_bytes.decode('utf-8')


if __name__ == '__main__':
    encode_str = encode("Hello Word!😀 😃 😄 😁 你好，世界！ 😆 😅 😂 🤣")
    print(encode_str)
    print(decode(encode_str))
