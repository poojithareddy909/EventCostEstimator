services = {
    'Venue Rental': 50000,
    'Catering per plate': 800,
    'Photography': 20000,
    'Decoration': 15000,
    'DJ & Music': 10000
}

print("Welcome to the Event Cost Estimation & Negotiation Bot!\n")
print("Available Services:")
for service, price in services.items():
    print(f"- {service}: ₹{price}")


selected_services = []
num_services = int(input("\nHow many services do you want to book? "))

for i in range(num_services):
    service_name = input(f"Enter service name #{i+1}: ")
    if service_name in services:
        quantity = 1
        if service_name == 'Catering per plate':
            quantity = int(input("Enter number of plates: "))
        selected_services.append((service_name, quantity))
    else:
        print("Invalid service name! Skipping.")


total_cost = 0
for service, quantity in selected_services:
    service_cost = services[service] * quantity
    total_cost += service_cost

print(f"\nInitial Event Cost: ₹{total_cost}")


discount = 0
is_repeat_client = input("Is this a repeat client? (yes/no): ").lower() == 'yes'

if total_cost > 100000:
    discount = total_cost * 0.10
    print("Negotiation: 10% discount applied for bill over ₹1,00,000.")
elif len(selected_services) >= 3:
    discount = 5000
    print("Negotiation: ₹5,000 discount applied for booking 3 or more services.")
elif is_repeat_client:
    discount = total_cost * 0.05
    print("Negotiation: 5% loyalty discount for repeat client.")
else:
    print("Negotiation: Complimentary photo album offered as a free add-on!")

final_cost = total_cost - discount
print(f"\nTotal Discount: ₹{discount}")
print(f"Final Event Cost after Negotiation: ₹{final_cost}")

print("\nThank you for using the Event Cost Estimator!")
