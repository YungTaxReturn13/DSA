class CeasarCipher:
    """Class for doing encryption and decryption using a Ceasar cipher"""

    def __init__(self, shift) -> None:
        """Construct ceasar cipher using given integer shift for rotation."""
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord("A"))
            decoder[k] = chr((k - shift) % 26 + ord("A"))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        """Return a string representing the encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, message):
        """Return decrypeted message given encrypted secret"""
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string"""
        msg = list(original)
        for k, _ in enumerate(msg):
            if msg[k].isupper():
                j = ord(msg[k]) - ord("A")
                msg[k] = code[j]
        return "".join(msg)


if __name__ == "__main__":
    cipher = CeasarCipher(3)
    message = "WE OUT HERE"
    coded = cipher.encrypt(message)
    print("Secret: ", coded)
    answer = cipher.decrypt(coded)
    print("Message: ", answer)

