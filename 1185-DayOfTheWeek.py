# Time Complexity O(1)
# Space Complexity O(1)
class Solution:
	def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

		def isLeapYear(year):
			return 1 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 0

		dayNames = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]
		daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		def daysSinceStart(day, month, year):
			numDays = 0
			for i in range(1971, year):
				numDays += 365 + isLeapYear(i)
			numDays += sum(daysInMonth[:month-1])
			numDays += day
			if month > 2:
				numDays += isLeapYear(year)
			return numDays

		knownStart = daysSinceStart(13,10,2020) #Today
		d = daysSinceStart(day, month, year)
		return dayNames[ (d - knownStart) % 7]
