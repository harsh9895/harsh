tickets = [] 
counter = 2000  

while True:
    print("""
    1. Add a Ticket
    2. Resolve a Ticket
    3. Display all Tickets
    4. Reopen a Ticket
    5. Show Ticket Data
    6. Quit
    """)

    print("Please choose a number from 1 to 6")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ticket_id = counter
        ID = input("Enter your staff ID: ")
        Name = input("Enter your name: ")
        Email = input("Enter your email id: ")
        Issue = input("Write your issue here... ")
        
        ticket = {
            "Ticket-id": ticket_id,
            "Name": Name,
            "Staff-id": ID,
            "E-mail": Email,
            "Issue": Issue,
            "Response": "Not Provided",
            "Status": "Open"
        }

        tickets.append(ticket)
        counter += 1
        print("Your ticket is submitted successfully")

    if choice == 2:
        ticket_id = int(input("Ticket ID: "))
        for ticket in tickets:
            if ticket["Ticket-id"] == ticket_id:
                Response = input("Enter Response: ")
                ticket["Response"] = Response
                ticket["Status"] = "Closed"
                break
                
    if choice == 3:
        for ticket in tickets:
            print("===========TICKET===========")
            print("Ticket ID:", ticket["Ticket-id"])
            print("Name:", ticket["Name"])
            print("ID:", ticket["Staff-id"])
            print("E-mail:", ticket["E-mail"])
            print("Issue:", ticket["Issue"])
            print("Response:", ticket["Response"])
            print("Status:", ticket["Status"])
            print("============================")

    if choice == 4:
        ticket_id = int(input("Ticket ID: "))
        for ticket in tickets:
            if ticket["Ticket-id"] == ticket_id:
                ticket["Status"] = "Reopened"
                break
                
    if choice == 5:
        total_tickets = len(tickets)
        open_tickets = sum(ticket["Status"] == "Open" for ticket in tickets)
        print("Total Tickets:", total_tickets)
        print("Open Tickets:", open_tickets)
        
    if choice == 6:
        print("Closing the ticketing system :)")
