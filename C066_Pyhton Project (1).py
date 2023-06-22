import tkinter as tk
import tkinter.messagebox
from tkinter import*
from tkinter import simpledialog
# Define the number of available seats
NUM_SEATS = 50

# Define the ticket price
TICKET_PRICE = 10

# Define an empty list to store the booked seats
booked_seats = []

# Define a function to display the available seats
def display_seats():
    available_seats = NUM_SEATS - len(booked_seats)
    available_seats_label.config(text=f"Available seats: {available_seats}/{NUM_SEATS}")
    booked_seats_label.config(text="Seat numbers already booked: " + ", ".join(str(s) for s in booked_seats))

# Define a function to book a seat
def book_seat():
    if len(booked_seats) >= NUM_SEATS:
        tk.messagebox.showinfo("Error", "Sorry, all seats have been booked.")
        return
    
    num_tickets = num_tickets_entry.get()
    
    try:
        num_tickets = int(num_tickets)
    except ValueError:
        tk.messagebox.showinfo("Error", "Invalid number of tickets. Please enter a number between 1 and 10.")
        return
    
    if num_tickets < 1 or num_tickets > 10:
        tk.messagebox.showinfo("Error", "Invalid number of tickets. Please enter a number between 1 and 10.")
        return
    
    available_seats = set(range(1, NUM_SEATS + 1)) - set(booked_seats)
    
    seat_numbers = set()
    
    for i in range(num_tickets):
        available_seats_str = ", ".join(str(s) for s in sorted(available_seats))
        
        seat_number = tk.simpledialog.askinteger("Select Seat", f"Available seats: {available_seats_str}\nEnter seat number for ticket {i+1} (1-50):", minvalue=1, maxvalue=50)
        
        if seat_number is None:
            return
        
        if seat_number not in available_seats:
            tk.messagebox.showinfo("Error", f"Seat {seat_number} is not available. Please select another seat.")
            return
        
        seat_numbers.add(seat_number)
    
    total_price = num_tickets * TICKET_PRICE
    
    if tk.messagebox.askyesno("Confirm Booking", f"You have selected the following seat numbers:\n{sorted(seat_numbers)}\n\nTotal price: ${total_price}\n\nDo you want to confirm the booking?"):
        tk.messagebox.showinfo("Success", f"{num_tickets} ticket(s) booked successfully!")
        for seat_number in seat_numbers:
            booked_seats.append(seat_number)
        display_seats()

# Create the GUI
window = tk.Tk()
window.title("Railway Booking System")

# Create the widgets
title_label = tk.Label(window, text="Welcome to the Railway Booking System!")
title_label.pack()

available_seats_label = tk.Label(window, text="")
available_seats_label.pack()

booked_seats_label = tk.Label(window, text="")
booked_seats_label.pack()

num_tickets_label = tk.Label(window, text="Enter the number of tickets you want to book (1-10):")
num_tickets_label.pack()

num_tickets_entry = tk.Entry(window)
num_tickets_entry.pack()

book_button = tk.Button(window, text="Book", command=book_seat)
book_button.pack()

quit_button = tk.Button(window, text="Quit", command=window.destroy)
quit_button.pack()

display_seats()

# Start the GUI
window.mainloop()
