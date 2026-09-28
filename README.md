# Railway Ticket Booking System  

## Overview of the Project
This is a Command Line Interface (CLI) application built to simulate a basic railway reservation counter. It lets a user book train tickets, check their confirmation status using a generated PNR, and cancel tickets. 

To keep the project lightweight and simple to run, it does not use any heavy external databases like SQL. Instead, it uses basic Python file handling to permanently save all passenger data into a local text file (`tickets.txt`).

## Features
* **Book a Ticket:** Takes passenger details and automatically generates a random 6-digit PNR and booking date.
* **Check PNR Status:** Searches the saved data to show passenger details and confirmation status.
* **Cancel Ticket:** Deletes a specific PNR from the system and updates the save file instantly.
* **Data Persistence:** All bookings are saved to a `.txt` file, so no data is lost when you close the program.

## Technologies & Tools Used
* **Language:** Python 3
* **Storage:** Local text file handling
* **Built-in Modules:** `os`, `random`, `datetime`

## Steps to Install & Run the Project
Because this project is built using only core Python, the setup is extremely simple.

**Environment Setup & Dependencies:**
* You just need Python 3 installed on your computer. 
* There are no external dependencies. You do not need to run any `pip install` commands.

**Configuration:**
* You don't need to configure any databases. The program will automatically create the `tickets.txt` file in the same folder the first time you run it.

**Execution:**
1. Download or clone this repository to your local machine.
2. Open your command line (Terminal on Mac/Linux, or Command Prompt on Windows).
3. Navigate to the folder where the files are saved using the `cd` command. 
   *(Example: `cd Desktop/railway-booking-system`)*
4. Run the main file by typing exactly:
   `python main.py`
5. The menu will appear on your screen. Use the number keys (1, 2, 3, 4) and press Enter to navigate.

## Instructions for Testing
If you are evaluating this project, here is the best way to test that all 5 modules work:
1. Run `python main.py` and select Option **1** to book a ticket. Enter dummy details (e.g., Name: Udit, Age: 19, Source: Bhopal, Destination: Lucknow).
2. Note down the 6-digit PNR number the system prints on the screen.
3. Select Option **4** to exit the program. Open the folder on your computer and open `tickets.txt` to verify the data was saved properly.
4. Run the program again. Select Option **2** and type your PNR to test the search function.
5. Select Option **3** and enter your PNR to cancel the ticket.
6. Check `tickets.txt` one last time to verify the record was successfully deleted.

