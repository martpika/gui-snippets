class CaesarCipher:
    def __init__(self, shift):
        """
        :param shift: values on how many alphabet characters be shifted
        """
        encoder = [None] * 26  # contains the encrypted format to follow
        decoder = [None] * 26  # contains the decrypted format to decode

        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def _transform(self, m, trans):
        msg = list(m)
        for i in range(len(msg)):
            temp = ord(msg[i]) - ord('A')
            msg[i] = trans[temp]
        return "".join(msg)

    def encrypt(self, code):
        return self._transform(code, self._forward)

    def decrypt(self, code):
        return self._transform(code, self._backward)

