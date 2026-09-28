import storage
import booking
import inquiry
import validation

def show_menu():
    print("\n--- Railway Reservation System ---")
    print("1. Book a Ticket")
    print("2. Check PNR Status")
    print("3. Cancel a Ticket")
    print("4. Exit")

def main():
    tkts = storage.read_file()
    
    while True:
        show_menu()
        ch = validation.get_int("Enter Choice (1-4): ")
        
        if ch == 1:
            booking.book(tkts)
        elif ch == 2:
            inquiry.check(tkts)
        elif ch == 3:
            inquiry.cancel(tkts)
        elif ch == 4:
            print("Saving data... Closing system.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()