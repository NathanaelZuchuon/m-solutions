def getInput(msg, amount=None):

	while type(amount) is not float:

		try:
			amount = float(input(msg))
			assert(amount > 0)
			return amount

		except(ValueError, AssertionError):
			amount = str(amount)

def number_of_months(num):
	print(f"Number of months: {num}")

def main():

	PORTION_DOWN_PAYMENT = 0.25 # Down payment
	CURRENT_SAVINGS = 0
	r = 0.4 # Annual interest rate

	annual_salary = getInput("Enter your annual salary: ")
	portion_saved = getInput("Enter the percent of your salary to save, as a decimal: ")
	total_cost = getInput("Enter the cost of your dream home: ")

	months = 0
	while CURRENT_SAVINGS < total_cost:

		additional_funds = CURRENT_SAVINGS*r/12
		CURRENT_SAVINGS += annual_salary*portion_saved
		CURRENT_SAVINGS += additional_funds
		monthly_salary = annual_salary/12
		CURRENT_SAVINGS += monthly_salary*portion_saved
		months += 1

	number_of_months(months)

main() # BY ZUCH
