class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return \Zero\

        # Define mappings
        def one(num):
            \\\ Convert a number less than 20 to words \\\
            switcher = [
                'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
            ]
            return switcher[num]

        def ten(num):
            \\\ Convert a number between 20 and 99 to words \\\
            switcher = [
                'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
            ]
            return switcher[num // 10 - 2]

        def two(num):
            \\\ Convert a number between 0 and 99 to words \\\
            if num == 0:
                return ''
            elif num < 20:
                return one(num)
            else:
                return ten(num) + ('' if num % 10 == 0 else ' ' + one(num % 10))

        def three(num):
            \\\ Convert a number between 0 and 999 to words \\\
            if num == 0:
                return ''
            elif num < 100:
                return two(num)
            else:
                return one(num // 100) + ' Hundred' + ('' if num % 100 == 0 else ' ' + two(num % 100))

        def convert(num):
            \\\ Convert the number to words recursively for different places \\\
            if num == 0:
                return ''
            elif num < 1000:
                return three(num)
            elif num < 1000000:
                return three(num // 1000) + ' Thousand' + ('' if num % 1000 == 0 else ' ' + three(num % 1000))
            elif num < 1000000000:
                return three(num // 1000000) + ' Million' + ('' if num % 1000000 == 0 else ' ' + convert(num % 1000000))
            else:
                return three(num // 1000000000) + ' Billion' + ('' if num % 1000000000 == 0 else ' ' + convert(num % 1000000000))

        return convert(num).strip()

