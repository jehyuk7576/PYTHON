import binascii

signature_dic = [
    {'ext': '.hwp', 'hex': 'D0CF11E0A1B11AE1', 'byte': 8},
    {'ext': '.pdf', 'hex': '25504446', 'byte': 4},
    {'ext': '.docx', 'hex': '504B0304', 'byte': 4},
    {'ext': '.pptx', 'hex': '504B0304', 'byte': 4},
    {'ext': '.xlsx', 'hex': '504B0304', 'byte': 4},
    {'ext': '.exe', 'hex': '4D5A', 'byte': 2},
    {'ext': '.img', 'hex': '504943540008', 'byte': 6},
    {'ext': '.gif', 'hex': '474946383961', 'byte': 6},
    {'ext': '.png', 'hex': '89504E470D0A1A0A', 'byte': 8},
    {'ext': '.jpeg', 'hex': 'FFD8FFE0', 'byte': 4},
    {'ext': '.wav', 'hex': '52494646', 'byte': 4},
    {'ext': '.zip', 'hex': '504B0304', 'byte': 4},
    ]

def compare(file_ext):

    for item in signature_dic:
        if item["ext"] == file_ext:
            length = item["byte"]
            hex = item["hex"]
            if length != None:
                return length, hex


filename = input("파일이름을 입력해주세요. : ")

try:
    f = open(filename, "rb")
    ext = "." + filename.split(".")[1]
    length, hex = compare(ext)
    signature = binascii.hexlify(f.read(length)).upper().decode('ascii')

    if signature != hex:
        print("변조된 파일")
    else:
        print("정상파일")
except FileNotFoundError:
    print("없는 파일입니다.")
except TypeError:
    print("지원하지 않는 확장명입니다.")
