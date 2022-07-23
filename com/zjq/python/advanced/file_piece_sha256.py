import hashlib

def file_piece_sha256(in_file_path, piece_size):
    sha256 = hashlib.sha256()
    with open(in_file_path, "rb") as in_file:
        # 在此实现 hash 计算
        while True:
            piece = in_file.read(piece_size)
            if piece:
                sha256.update(piece.hex().encode('utf-8'))
            else:
                break
    return sha256.digest().hex()

if __name__ == '__main__':
    ret = file_piece_sha256('file_piece_sha256.py', 128)
    print("file hash is: ", ret)