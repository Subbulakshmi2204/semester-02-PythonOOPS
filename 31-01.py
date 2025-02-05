def book_movie_ticket():
    name = input("Enter the name: ")
    phone_number = input("Enter your phone number: ")
    dob = input("Enter your date of birth: ")
    total_seats = int(input("Select total number of seats: "))
    
    print("\nAvailable Seat Categories:")
    print("First Class: A to G - ₹200 + GST")
    print("Second Class: H to X - ₹150 + GST")
    print("Economic Class: Y and Z - ₹50 + GST")
    
    available_seats = "A1, A2, A3, A4, A5, A6, B1, B2, B3, ... Y1, Z1"
    print("\nAvailable Seats:", available_seats)
    
    seats = input(f"Select your seats (e.g., A2, A6, etc.) for {total_seats} seats: ").split(',')
    print(f"\nYou have selected seats: {', '.join(seats)}")
   
    snacks_choice = input("Do you want Snacks (Yes/No): ").strip().lower()
    
    snacks_price = {
        "popcorn": 100,
        "ice cream": 80,
        "puffs": 60,
        "tea": 40,
        "soft drinks": 50
    }
    
    snack_total = 0
    if snacks_choice == "yes":
        print("\nAvailable Snacks:")
        for snack, price in snacks_price.items():
            print(f"{snack.capitalize()} - ₹{price}")
        
        snack_order = input("Select your snacks (e.g., Popcorn, Ice Cream, etc.): ").strip().lower()
        snack_quantity = int(input(f"How many {snack_order}s do you want? "))
        
        
        if snack_order in snacks_price:
            snack_total = snacks_price[snack_order] * snack_quantity
            print(f"\nYou have selected {snack_quantity} {snack_order}(s). Total Snack Price: ₹{snack_total}")
        else:
            print("Invalid snack selection.")
    
    ticket_price = 0
    for seat in seats:
        row = seat[0] 
        if 'A' <= row <= 'G':
            ticket_price += 200
        elif 'H' <= row <= 'X':
            ticket_price += 150
        elif row in ['Y', 'Z']:
            ticket_price += 50
    
    gst = 0.18
    total_price = ticket_price * (1 + gst) + snack_total
    
    print(f"\nHi {name} ..! You have successfully booked {total_seats} tickets. Seats: {', '.join(seats)}")
    print(f"Your total ticket price: ₹{ticket_price * (1 + gst)}")
    print(f"Your snacks price: ₹{snack_total}")
    print(f"Your final total: ₹{total_price:.2f}")

book_movie_ticket()
