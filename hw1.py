def decimal_to_binary(decimal):
    binary = ''
    for i in range(7, -1, -1):
        if decimal >= 2**i:
            binary += '1'
            decimal -= 2**i
        else:
            binary += '0'
    return binary

def binary_to_hex(binary):
    hex_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    hex_result = ''
    for i in range(0, len(binary), 4):
        hex_digit = binary[i:i+4]
        hex_result += hex_map[hex_digit]
    return hex_result

decimal = int(input("請輸入一個0到255之間的十進位數字: "))
binary_result = decimal_to_binary(decimal)
hex_result = binary_to_hex(binary_result)
print("二進位數字:", binary_result)
print("十六進位數字:", hex_result)
