import socket

class Assignment2:
    def __init__(self, year):
        self.year = year


    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is", age)

    def listAnniversaries(self):
        current_year = 2022
        anniversary_years = []
        for i in range(self.year + 10, current_year + 1, 10):
            anniversary_years.append(i - self.year)
        return anniversary_years

    def modifyYear(self, n):
        year_str = str(self.year)

        first_two_chars = year_str[:2]

        odd_chars = ""
        for i in range(1, len(year_str)):
            if i % 2 == 1:  
                odd_chars += year_str[i]

        combined_str = first_two_chars + odd_chars

        result_str = combined_str * n

        return result_str

    def checkGoodString(self, string):
        if len(string) < 9:
            return False

        if not string[0].islower():
            return False

        digit_count = sum(c.isdigit() for c in string)

        if digit_count != 1:
            return False

        return True

    def connectTcp(self, host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
            return True
        except Exception as e:
            return False

   