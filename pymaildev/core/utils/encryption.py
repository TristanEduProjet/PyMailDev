import base64


class Encryption:
    """
        Encryption class in Base64 encoding.
    """
    @staticmethod
    def encode(key, clear):
        """
        Encode a string in Base64
        :param key: Secret message
        :param clear: String to encode
        :return: Encoded String
        """
        enc = []
        for i in range(len(clear)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    @staticmethod
    def decode(key, enc):
        """
        Decode a Base64' String
        :param key: Secret message
        :param enc: String to decode
        :return: Decoded String
        """
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)
