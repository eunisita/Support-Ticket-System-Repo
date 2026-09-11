"""
Author: Eunice De Castro (Student ID: 20267230)
Date: September 11, 2026
Course: IT5016 Software Development Fundamentals
Assessment: 3 - Software Research & Practice
"""
import uuid

def generate_ticket_info():
    """
    LESSON 1: Input handling
    Notes: Simple function to collect user input.
    """
    user_name = input("Enter customer name: ")
    issue_severity = int(input("Enter issue severity (1-Low, 2-Medium, 3-High): "))
    base_cost = float(input("Enter base cost of the issue: "))
    ticket_id = f"TC-{str(uuid.uuid4())[:8]}"
    return user_name, issue_severity, base_cost, ticket_id


def calculate_total_cost(base_cost):
    """
    LESSON 2: Simple math logic
    Notes: Keeps calculations in one place. Tax is 15%.
    """
    tax = base_cost * 0.15
    total = base_cost + tax
    return total


def validate_ticket_data(user_name, issue_severity, base_cost):
    """
    LESSON 3: Data validation
    Notes: Checks that the inputs make sense before printing.
    """
    assert len(user_name.strip()) > 0, "Name cannot be empty"
    assert 1 <= issue_severity <= 3, "Severity must be 1, 2, or 3"
    assert base_cost >= 0, "Cost cannot be negative"


def display_ticket_summary(ticket_id, user_name, issue_severity, base_cost, total_cost):
    """
    LESSON 4: Display output
    Notes: Prints the formatted ticket summary.
    """
    print("\n--- SUPPORT TICKET SUMMARY ---")
    print(f"Ticket ID      : {ticket_id}")
    print(f"Customer Name  : {user_name}")
    print(f"Severity Level : {issue_severity}")
    print(f"Base Cost      : ${base_cost:.2f}")
    print(f"Total Cost     : ${total_cost:.2f}")


# Main program execution
user_name, issue_severity, base_cost, ticket_id = generate_ticket_info()
total_cost = calculate_total_cost(base_cost)
validate_ticket_data(user_name, issue_severity, base_cost)
display_ticket_summary(ticket_id, user_name, issue_severity, base_cost, total_cost)