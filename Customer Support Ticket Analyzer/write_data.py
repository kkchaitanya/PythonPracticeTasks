import csv

from support_ticket_class import Ticket,Category,Priority,Status

# 50 ticket records

tickets = [
    Ticket(1001, "Rahul Sharma", Category.PAYMENT, Priority.HIGH, Status.OPEN, "Amit", 0),
    Ticket(1002, "Priya Reddy", Category.TECHNICAL, Priority.CRITICAL, Status.IN_PROGRESS, "Sneha", 4),
    Ticket(1003, "Arjun Kumar", Category.LOGIN, Priority.MEDIUM, Status.RESOLVED, "Rahul", 12),
    Ticket(1004, "Ananya Singh", Category.COURSE, Priority.LOW, Status.CLOSED, "Neha", 24),
    Ticket(1005, "Vikram Patel", Category.REFUND, Priority.HIGH, Status.OPEN, "Amit", 0),
    Ticket(1006, "Meera Nair", Category.ACCOUNT, Priority.MEDIUM, Status.IN_PROGRESS, "Sneha", 6),
    Ticket(1007, "Rohan Das", Category.PAYMENT, Priority.CRITICAL, Status.RESOLVED, "Rahul", 8),
    Ticket(1008, "Kavya Rao", Category.TECHNICAL, Priority.HIGH, Status.CLOSED, "Neha", 18),
    Ticket(1009, "Aditya Verma", Category.LOGIN, Priority.LOW, Status.OPEN, "Amit", 0),
    Ticket(1010, "Sneha Gupta", Category.COURSE, Priority.MEDIUM, Status.RESOLVED, "Sneha", 10),
    Ticket(1011, "Kiran Joshi", Category.REFUND, Priority.HIGH, Status.IN_PROGRESS, "Rahul", 5),
    Ticket(1012, "Pooja Mehta", Category.ACCOUNT, Priority.LOW, Status.CLOSED, "Neha", 20),
    Ticket(1013, "Suresh Reddy", Category.PAYMENT, Priority.MEDIUM, Status.OPEN, "Amit", 0),
    Ticket(1014, "Divya Kapoor", Category.TECHNICAL, Priority.CRITICAL, Status.IN_PROGRESS, "Sneha", 3),
    Ticket(1015, "Manoj Kumar", Category.LOGIN, Priority.HIGH, Status.RESOLVED, "Rahul", 7),
    Ticket(1016, "Aisha Khan", Category.COURSE, Priority.MEDIUM, Status.CLOSED, "Neha", 16),
    Ticket(1017, "Nikhil Jain", Category.REFUND, Priority.LOW, Status.OPEN, "Amit", 0),
    Ticket(1018, "Swati Agarwal", Category.ACCOUNT, Priority.HIGH, Status.RESOLVED, "Sneha", 9),
    Ticket(1019, "Varun Malhotra", Category.PAYMENT, Priority.CRITICAL, Status.IN_PROGRESS, "Rahul", 2),
    Ticket(1020, "Isha Sharma", Category.TECHNICAL, Priority.MEDIUM, Status.CLOSED, "Neha", 14),
    Ticket(1021, "Akash Rao", Category.LOGIN, Priority.HIGH, Status.OPEN, "Amit", 0),
    Ticket(1022, "Neeraj Singh", Category.COURSE, Priority.LOW, Status.RESOLVED, "Sneha", 11),
    Ticket(1023, "Lakshmi Devi", Category.REFUND, Priority.MEDIUM, Status.IN_PROGRESS, "Rahul", 6),
    Ticket(1024, "Harish Babu", Category.ACCOUNT, Priority.CRITICAL, Status.CLOSED, "Neha", 22),
    Ticket(1025, "Tanvi Shah", Category.PAYMENT, Priority.HIGH, Status.RESOLVED, "Amit", 5),
    Ticket(1026, "Gaurav Yadav", Category.TECHNICAL, Priority.LOW, Status.OPEN, "Sneha", 0),
    Ticket(1027, "Nandini Rao", Category.LOGIN, Priority.MEDIUM, Status.IN_PROGRESS, "Rahul", 4),
    Ticket(1028, "Ravi Teja", Category.COURSE, Priority.HIGH, Status.CLOSED, "Neha", 19),
    Ticket(1029, "Shalini Gupta", Category.REFUND, Priority.CRITICAL, Status.RESOLVED, "Amit", 3),
    Ticket(1030, "Abhishek Roy", Category.ACCOUNT, Priority.MEDIUM, Status.OPEN, "Sneha", 0),
    Ticket(1031, "Deepak Sharma", Category.PAYMENT, Priority.LOW, Status.CLOSED, "Rahul", 25),
    Ticket(1032, "Pallavi Reddy", Category.TECHNICAL, Priority.HIGH, Status.RESOLVED, "Neha", 8),
    Ticket(1033, "Sanjay Kumar", Category.LOGIN, Priority.CRITICAL, Status.IN_PROGRESS, "Amit", 2),
    Ticket(1034, "Ritu Singh", Category.COURSE, Priority.MEDIUM, Status.OPEN, "Sneha", 0),
    Ticket(1035, "Mohit Patel", Category.REFUND, Priority.HIGH, Status.CLOSED, "Rahul", 17),
    Ticket(1036, "Preeti Nair", Category.ACCOUNT, Priority.LOW, Status.RESOLVED, "Neha", 13),
    Ticket(1037, "Karthik Rao", Category.PAYMENT, Priority.CRITICAL, Status.OPEN, "Amit", 0),
    Ticket(1038, "Shreya Das", Category.TECHNICAL, Priority.MEDIUM, Status.IN_PROGRESS, "Sneha", 5),
    Ticket(1039, "Yash Verma", Category.LOGIN, Priority.HIGH, Status.RESOLVED, "Rahul", 6),
    Ticket(1040, "Bhavna Joshi", Category.COURSE, Priority.LOW, Status.CLOSED, "Neha", 21),
    Ticket(1041, "Aman Khan", Category.REFUND, Priority.MEDIUM, Status.OPEN, "Amit", 0),
    Ticket(1042, "Komal Mehta", Category.ACCOUNT, Priority.HIGH, Status.IN_PROGRESS, "Sneha", 7),
    Ticket(1043, "Rakesh Jain", Category.PAYMENT, Priority.CRITICAL, Status.RESOLVED, "Rahul", 4),
    Ticket(1044, "Sakshi Kapoor", Category.TECHNICAL, Priority.LOW, Status.CLOSED, "Neha", 15),
    Ticket(1045, "Tarun Gupta", Category.LOGIN, Priority.MEDIUM, Status.OPEN, "Amit", 0),
    Ticket(1046, "Muskan Sharma", Category.COURSE, Priority.HIGH, Status.IN_PROGRESS, "Sneha", 3),
    Ticket(1047, "Naveen Reddy", Category.REFUND, Priority.CRITICAL, Status.RESOLVED, "Rahul", 2),
    Ticket(1048, "Anjali Verma", Category.ACCOUNT, Priority.MEDIUM, Status.CLOSED, "Neha", 18),
    Ticket(1049, "Rohit Mehta", Category.PAYMENT, Priority.HIGH, Status.OPEN, "Amit", 0),
    Ticket(1050, "Simran Kaur", Category.TECHNICAL, Priority.LOW, Status.RESOLVED, "Sneha", 10),
]


# CSV file name
filename = "tickets.csv"

# Write data to CSV
with open(filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow([
        "ticket_id",
        "customer_name",
        "category",
        "priority",
        "status",
        "assigned_agent",
        "resolution_time"
    ])

    # Data
    for ticket in tickets:
        writer.writerow([
            ticket.ticket_id,
            ticket.customer_name,
            ticket.category.value,
            ticket.priority.value,
            ticket.status.value,
            ticket.assigned_agent,
            ticket.resolution_time
        ])

print(f"{len(tickets)} tickets written to {filename}")