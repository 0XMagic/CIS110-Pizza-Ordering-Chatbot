PIZZA_PRICE = 14.99
SALES_TAX = 1.1
def main():
	username = input("Enter name:\t")
	print(f"Hello {username}, nice to meet you!")
	size = input("\nWhat size do you want? (Small, Medium, Large)\t")
	flavor = input("\nWhat flavor do you want?\t")
	crust_type = input("\nWhat type of crust do you want?\t")
	quantity = input("\nHow many do you want? (numeric values only)\t")
	method = input("\nIs this take-out or for delivery?\t")
	quantity = int(quantity)
	total = quantity * PIZZA_PRICE * SALES_TAX

	print("-" * 10)
	print(f"Thank you {username} for your {method} order!")
	print(f"Your {quantity} {size} {flavor} pizza(s) with {crust_type} crust will cost ${total:.2f}")
	print("-" * 10)


if __name__ == "__main__":
	main()
