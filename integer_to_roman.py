"""
Author: Alberto Marci
"""


class DecimalToRoman:
    # convert number from 0 to 9
    def __zero_to_nine(self, number):
        if number == '0':
            return ''
        if number == '1':
            return 'I'
        if number == '2':
            return 'II'
        if number == '3':
            return 'III'
        if number == '4':
            return 'IV'
        if number == '5':
            return 'V'
        if number == '6':
            return 'VI'
        if number == '7':
            return 'VII'
        if number == '8':
            return 'VIII'
        if number == '9':
            return 'IX'

    # convert number from 10 to 90
    def __ten_to_ninety(self, number):
        if number == '0':
            return ''
        if number == '1':
            return 'X'
        if number == '2':
            return 'XX'
        if number == '3':
            return 'XXX'
        if number == '4':
            return 'XL'
        if number == '5':
            return 'L'
        if number == '6':
            return 'LX'
        if number == '7':
            return 'LXX'
        if number == '8':
            return 'LXXX'
        if number == '9':
            return 'XC'

    # convert number from 100 to 900
    def __one_hundred_to_nine_hundred(self, number):
        if number == '0':
            return ''
        if number == '1':
            return 'C'
        if number == '2':
            return 'CC'
        if number == '3':
            return 'CCC'
        if number == '4':
            return 'CD'
        if number == '5':
            return 'D'
        if number == '6':
            return 'DC'
        if number == '7':
            return 'DCC'
        if number == '8':
            return 'DCCC'
        if number == '9':
            return 'CM'

    # convert number from 1000 to 3000
    def __one_thousand_to_three_thousand(self, number):
        if number == '1':
            return 'M'
        if number == '2':
            return 'MM'
        if number == '3':
            return 'MMM'
    # return roman string
    def integer_to_roman(self, number):
        tmp = str(number)
        str_len = len(tmp)
        if str_len == 1:
            return self.__zero_to_nine(tmp[0])
        if str_len == 2:
            roman_str0 = self.__zero_to_nine(tmp[1])
            roman_str1 = self.__ten_to_ninety(tmp[0])
            return roman_str1 + roman_str0
        if str_len == 3:
            roman_str0 = self.__zero_to_nine(tmp[2])
            roman_str1 = self.__ten_to_ninety(tmp[1])
            roman_str2 = self.__one_hundred_to_nine_hundred(tmp[0])
            return roman_str2 + roman_str1 + roman_str0
        if str_len == 4:
            roman_str0 = self.__zero_to_nine(tmp[3])
            roman_str1 = self.__ten_to_ninety(tmp[2])
            roman_str2 = self.__one_hundred_to_nine_hundred(tmp[1])
            roman_str3 = self.__one_thousand_to_three_thousand(tmp[0])
            return roman_str3 + roman_str2 + roman_str1 + roman_str0

    def test(self):
        print(self.integer_to_roman(13))
        print('-------------------------------------------')
        print(self.integer_to_roman(48))
        print('-------------------------------------------')
        print(self.integer_to_roman(444))
        print('-------------------------------------------')
        print(self.integer_to_roman(3444))
        print('-------------------------------------------')
        print(self.integer_to_roman(3999))
        print('-------------------------------------------')
        print(self.integer_to_roman(100))


# ----------------------------------------------------------------------------------------------------------------------

converter = DecimalToRoman()
converter.test()
print('-------------------------------------------')
print('-------------------------------------------')
print(converter.integer_to_roman(1234))
