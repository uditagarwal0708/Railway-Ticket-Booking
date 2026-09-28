import random
import datetime
import storage
import validation

def book(lst):
    print("\n--- Book Train Ticket ---")
    
    nm = validation.get_str("Passenger Name: ")
    ag = validation.get_int("Passenger Age: ")
    st1 = validation.get_str("From Station (e.g. Bhopal): ")
    st2 = validation.get_str("To Station (e.g. Lucknow): ")
    
    p = random.randint(100000, 999999)
    dt = datetime.date.today()
    
    d = {
        "pnr": p,
        "name": nm.title(),
        "age": ag,
        "src": st1.upper(),
        "dest": st2.upper(),
        "dt": dt
    }
    
    lst.append(d)
    storage.write_file(lst)
    
    print("\nTicket Booked Successfully!")
    print("Your PNR: " + str(p))