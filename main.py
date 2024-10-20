SALES_TAX = 1.1
CREATOR = "a rabbit"    #since this repository is public, I am not using my real name
def main():

	username = input("Enter name:\t")
	if username.lower() == CREATOR:
		print(f"My creator {username}, pleasure to serve you!")
	else:
		print(f"Hello {username}, nice to meet you!")

	size = input("\nWhat size do you want? (Small, Medium, Large)\t")

	price = 0.0
	if size.lower() == "small":
		price = 8.99
	elif size.lower() == "medium":
		price = 14.99
	elif size.lower() == "large":
		price = 17.99

	flavor = input("\nWhat flavor do you want?\t")
	crust_type = input("\nWhat type of crust do you want?\t")
	quantity = input("\nHow many do you want? (numeric values only)\t")
	method = input("\nIs this take-out or for delivery?\t")

	delivery_fee = 5 * (method == "delivery")   #decided to convert this if-else block into a 1-liner
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


if __name__ == "__main__":
	main()
