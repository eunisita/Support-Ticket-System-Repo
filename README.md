# Support Ticket Management System

**Author:** Eunice De Castro  
**Student ID:** 20267230  
**Date:** September 11, 2026  
**Course:** IT5016 Software Development Fundamentals  

---

## What this program does
I built this little Python script using our practice homework to get a better handle on procedural programming and clean code structure. It asks the user for some basic support ticket info, checks to make sure the inputs actually make sense, calculates a 15% tax on the cost, and prints out a clean ticket summary.

## Key things I learned & practiced
* **Single Responsibility Principle:** I broke down my script into small functions so each one does just one job. `generate_ticket_info` collects inputs, `calculate_total_cost` does the math, and `display_ticket_summary` prints it out.
* **Defensive Programming:** I added basic `assert` checks to stop the code if someone types in a blank name, an invalid severity level, or a negative cost.
* **Low Coupling:** My functions pass values directly through arguments instead of relying on global variables.# Support-Ticket-System-Repo
A procedural Python application for gathering, validating, and computing support ticket costs. Practicing Single Responsibility Principle (SRP), low coupling, and basic defensive programming assertions.
