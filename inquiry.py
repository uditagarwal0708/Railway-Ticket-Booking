import validation
import storage

def check(lst):
    print("\n--- PNR Status ---")
    chk = validation.get_int("Enter PNR Number: ")
    
    flag = 0
    for i in lst:
        if i["pnr"] == chk:
            print("\nPassenger Name: " + i["name"])
            print("Route: " + i["src"] + " to " + i["dest"])
            print("Date of Booking: " + str(i["dt"]))
            print("Status: CONFIRMED")
            flag = 1
            break
            
    if flag == 0:
        print("Sorry, no ticket found with that PNR.")

def cancel(lst):
    print("\n--- Cancel Ticket ---")
    c = validation.get_int("Enter PNR to cancel: ")
    
    flag = 0
    for i in range(len(lst)):
        if lst[i]["pnr"] == c:
            lst.pop(i) # Delete from list
            storage.write_file(lst)
            print("Ticket Cancelled Successfully.")
            flag = 1
            break
            
    if flag == 0:
        print("PNR not found. Cannot cancel.")