class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        d1, d2 = min(date1, date2), max(date1, date2)
        year1, month1, day1 = (int(i) for i in d1.split('-'))
        year2, month2, day2 = (int(i) for i in d2.split('-'))

        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def days_between_two_years(year1, year2):
            return sum(366 if is_leap(year) else 365 for year in range(year1, year2))

        def days_from_year_start(year, month, day):
            return sum(month_days[:(month - 1)]) + day + (1 if is_leap(year) and month > 2 else 0)

        return days_between_two_years(year1, year2) + days_from_year_start(year2, month2,
                                                                           day2) - days_from_year_start(year1,
                                                                                                        month1,
                                                                                                        day1)


s = Solution()
print(s.daysBetweenDates("2019-08-01", "2020-08-02"))
