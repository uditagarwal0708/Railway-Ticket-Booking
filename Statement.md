# Project Statement:

# Railway Ticket Booking System

## Problem statement
Keeping track of train reservations manually on paper is slow and leads to mistakes, like double-booking a seat or losing a passenger's details. Setting up a massive database like SQL just to track basic daily tickets is too complex and heavy for a small local booking counter. There is a need for a lightweight, fast, and simple digital system to handle basic ticketing without requiring an internet connection or a heavy server setup.

## Scope of the project
This project is a Python-based Command Line Interface (CLI) application. It is designed to run directly in the terminal and handle the core functions of a reservation system (booking, checking, and canceling tickets). To keep the memory footprint small, the scope of data storage is limited to local text file handling (`tickets.txt`). The project focuses on basic automation, such as generating random PNR numbers and fetching the current date, rather than complex network-based syncing.

## Target users
* **Local Travel Agents:** Small-scale ticket vendors who need a quick, text-based system to book daily routes for customers.
* **Transit Administrators:** Staff at booking counters who want a simple system that won't crash if they accidentally type the wrong input.
* **Computer Science Students:** Users looking for a clear example of how real-world CRUD operations work in a terminal environment.

## High-level features
* **Automated Ticket Generation:** Creates a random 6-digit PNR and timestamps the booking automatically.
* **Instant PNR Inquiry:** Allows users to search for their specific PNR to check their confirmation status and route details.
* **Cancellation System:** Safely searches for and deletes specific ticket records, updating the storage file instantly.
* **Persistent Local Storage:** Saves all bookings to a comma-separated `.txt` file so no data is lost when the program closes.
* **Input Validation:** Prevents the system from crashing by catching basic errors (like typing letters instead of numbers for an age).