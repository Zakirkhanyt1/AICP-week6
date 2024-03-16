import datetime

# Ticket prices
ticket_prices = {
    "adult": {"one_day": 20.00, "two_day": 30.00},
    "child": {"one_day": 12.00, "two_day": 18.00},
    "senior": {"one_day": 16.00, "two_day": 24.00},
    "family": {"one_day": 60.00, "two_day": 90.00},
    "group": {"one_day": 15.00, "two_day": 22.50}
}

# Extra attraction prices
attraction_prices = {
    "lion feeding": 2.50,
    "penguin feeding": 2.00,
    "evening barbecue (two-day tickets)": 5.00
}


# Function to display ticket options and attractions
def display_options():
    print("Ticket Options:")
    print("1. One-Day Tickets:")
    for ticket, prices in ticket_prices.items():
        print(f"- {ticket.capitalize()}: ${prices['one_day']}")
    print("\n2. Two-Day Tickets:")
    for ticket, prices in ticket_prices.items():
        print(f"- {ticket.capitalize()}: ${prices['two_day']}")
    print("\nExtra Attractions:")
    for attraction, price in attraction_prices.items():
        print(f"- {attraction}: ${price}")


# Function to process a booking
def process_booking():
    print("\nWelcome to the Wildlife Park booking system!")
    display_options()
    today = datetime.date.today()
    days_available = [today + datetime.timedelta(days=i) for i in range(7)]
    print("\nDays Available for Booking:")
    for day in days_available:
        print(day.strftime("%A, %B %d, %Y"))

    total_cost = 0
    tickets = {}
    attractions = []

    # Input tickets required
    while True:
        ticket_type = input("\nEnter ticket type (adult/child/senior/family/group): ").lower()
        if ticket_type not in ticket_prices.keys():
            print("Invalid ticket type. Please try again.")
            continue
        ticket_duration = input("Enter ticket duration (one_day/two_day): ").lower()
        if ticket_duration not in ["one_day", "two_day"]:
            print("Invalid ticket duration. Please try again.")
            continue
        quantity = int(input("Enter quantity: "))
        tickets[(ticket_type, ticket_duration)] = quantity
        total_cost += ticket_prices[ticket_type][ticket_duration] * quantity
        choice = input("Would you like to add more tickets? (yes/no): ").lower()
        if choice != "yes":
            break

    # Input extra attractions
    while True:
        attraction = input("\nEnter extra attraction (or type 'done' to finish): ").lower()
        if attraction == "done":
            break
        if attraction not in attraction_prices.keys():
            print("Invalid attraction. Please try again.")
            continue
        attractions.append(attraction)
        total_cost += attraction_prices[attraction]

    # Generate unique booking number
    booking_number = hash(datetime.datetime.now())

    # Display booking details
    print("\nBooking Details:")
    print(f"Booking Number: {booking_number}")
    print("Tickets:")
    for ticket, quantity in tickets.items():
        print(f"- {quantity} {ticket[0]} {ticket[1]} ticket(s)")
    print("Extra Attractions:")
    for attraction in attractions:
        print(f"- {attraction}")
    print(f"Total Cost: ${total_cost}")


# Main program
def main():
    while True:
        process_booking()
        choice = input("\nWould you like to make another booking? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the Wildlife Park booking system!")
            break


if __name__ == "__main__":
    main()