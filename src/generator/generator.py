import string
import random


class passwordGenerator:
    min_length = 6
    max_length = 16

    special_length = 16
    number_length = 16
    lowercase_length = 16
    uppercase_length = 16

    def __init__(self, length, if_lowercase, if_uppercase, if_special, if_number):
        self.length = length
        self.if_lowercase = if_lowercase
        self.if_uppercase = if_uppercase
        self.if_special = if_special
        self.if_number = if_number

    def _validate(self) -> None:
        if self.length < self.min_length or self.length > self.max_length:
            raise Exception("Character length should not be negative")

    def generate(self) -> string:
        self._validate()

        password = ""
        source = self._get_dict_character()

        i = 0
        while i < self.length:
            val = random.choice(source)
            source.remove(val)
            password += val

            i += 1

        return password

    def _get_dict_character(self) -> list:
        source = ""

        if self.if_lowercase:
            source += self._get_random_character(string.ascii_lowercase, self.lowercase_length)

        if self.if_uppercase:
            source += self._get_random_character(string.ascii_uppercase, self.uppercase_length)

        if self.if_number:
            source += self._get_random_character(string.digits, self.number_length)

        if self.if_special:
            source += self._get_random_character(string.punctuation, self.special_length)

        return [*source]

    def _get_random_character(self, source: str, length: int) -> string:
        return "".join(random.choice(source) for x in range(length))
