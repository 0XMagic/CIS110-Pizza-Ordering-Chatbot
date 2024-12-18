import time
SALES_TAX = 1.1
CREATOR = "a rabbit"  #since this repository is public, I am not using my real name


def main():
	username = input("Enter name:\t")
	while not username:
		username = input("Name cannot be blank, please enter name:\t")

	if username.lower() == CREATOR:
		print(f"My creator {username}, pleasure to serve you!")
	else:
		print(f"Hello {username}, nice to meet you!")
	keep_going = "y"
	while keep_going.lower() == "y":
		size = input("\nWhat size do you want? (Small, Medium, Large)\t")
		while size.lower() not in ("small", "medium", "large"):
			size = input("\nInvalid size! Enter size: (Small, Medium, Large)")

		price = 0.0
		if size.lower() == "small":
			price = 8.99
		elif size.lower() == "medium":
			price = 14.99
		elif size.lower() == "large":
			price = 17.99

		flavor = input("\nWhat flavor do you want?\t")

		while not flavor:
			flavor = input("\nFlavor cannot be blank! Enter flavor:\t")

		crust_type = input("\nWhat type of crust do you want?\t")
		while not crust_type:
			crust_type = input("Crust type cannot be blank! Enter crust type:\t")

		quantity = input("\nHow many do you want? (numeric values only)\t")

		while not quantity.isdigit():
			quantity = input("\nInvalid value! How many do you want:\t")

		method = input("\nIs this carry out or for delivery?\t").lower()
		while method not in ("carry out", "delivery"):
			method = input("\nInput must be carry out or delivery!\t").lower()

		delivery_fee = 5 * (method == "delivery")  #decided to convert this if-else block into a 1-liner
		quantity = int(quantity)
		total = quantity * price * SALES_TAX + delivery_fee

		print("-" * 10)
		print(f"Thank you {username} for your {method} order!")
		print(f"Your {quantity} {size} {flavor} pizza(s) with {crust_type} crust will cost ${total:.2f}")

		if total >= 50:
			print("\nCongratulations, you earned a $10-off coupon on your next order")
		else:
			print("\nDid you know? Orders over $50 get a $10 coupon.")

		print("-" * 10)

		minutes_remaining = 3
		print(f"Order received: ETA {minutes_remaining} minutes")
		for minute in range(minutes_remaining, 0, -1):
			print(f"{minute} minutes remaining.")
			for second in range(60, 0, -1):
				print(second, end = " \r")
				time.sleep(1)
		print("Your order is ready!")
		keep_going = input("\nOrder another pizza? (y/n)")







if __name__ == "__main__":
	main()
