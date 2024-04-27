""" Ticket booking system
v1: calculate the total of one order
"""


from tkinter import *

ADULT = 15
CHILD = 5
STUDENT = 10
MAX_TICKETS = 100

class Ticket:
    
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def calc_subtype_total(self):
        return self.price * self.quantity


def collect_info():
    order_list = []
    adult = Ticket(ADULT, quantity_adult.get())
    child = Ticket(CHILD, quantity_child.get())
    student = Ticket(STUDENT, quantity_student.get())
    order_list.append(adult)
    order_list.append(child)
    order_list.append(student)
    return order_list

def cal_order_total(order_list):
    total = 0
    for order in order_list:
        total += order.calc_subtype_total()
    return total

def click_total():
    total = cal_order_total(collect_info())
    label_total_amount_var.set("${:.2f}".format(total))
    

# main structure layout
root = Tk()
root.title("Ticket Booking System")
ticket_frame = Frame(root, width="500", height="400")
ticket_frame.grid(row=0, column=0, columnspan=2)

# labels for each ticket type
label_adult = Label(ticket_frame, text = "Adult $15")
label_adult.grid(row=0, column=0, sticky="W")

label_child = Label(ticket_frame, text = "Child $5")
label_child.grid(row=1, column=0, sticky="W")

label_student = Label(ticket_frame, text = "Student / Senior $10")
label_student.grid(row=2, column=0, sticky="W")

# input boxes for number of each ticket type to order
quantity_adult = IntVar()
quantity_adult.set(0)

quantity_child = IntVar()
quantity_child.set(0)

quantity_student = IntVar()
quantity_student.set(0)

entry_adult = Entry(ticket_frame, textvariable = quantity_adult)
entry_adult.grid(row=0, column=1, sticky="W")

entry_child = Entry(ticket_frame, textvariable = quantity_child)
entry_child.grid(row=1, column=1, sticky="W")

entry_student = Entry(ticket_frame, textvariable = quantity_student)
entry_student.grid(row=2, column=1, sticky="W")

# display the total order
button_total = Button(ticket_frame, text = "Total for the order:", command = click_total)
button_total.grid(row=3, column=0, sticky="W", pady=10)

label_total_amount_var = IntVar()
label_total_amount = Label(ticket_frame, textvariable = label_total_amount_var)
label_total_amount.grid(row=3, column=1, sticky="W", pady=10)


root.mainloop()