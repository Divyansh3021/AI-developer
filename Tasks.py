from crewai import Task
from Agents import *

req_desc = """
Develop a library management system using Python that offers the following functionalities:

Book Management:
Adding Books: Allow adding new books to the system by capturing details like title, author, ISBN (optional), genre, and number of copies available.
Viewing Books: Enable searching for existing books by title, author, or ISBN. Display a list of matching books with details like title, author, genre, and availability status (available/issued).
Member Management:
Adding Members: Allow adding new library members by capturing details like member ID, name, contact information, and maximum borrowing limit.
Viewing Members: Enable searching for existing members by member ID or name. Display member details including name, contact information, and current borrowed books (if any).
Book Loan/Return:
Issuing Books: Allow issuing books to members. The system should check for book availability, member borrowing limit, and any outstanding dues before processing the loan. Update the book's availability status and record the loan details (member ID, book title, issue date, expected return date).
Returning Books: Allow returning borrowed books. Update the book's availability status and remove the loan record from the system.
Reporting:
Missing Books: Allow librarians to report missing books. This could involve marking a book as missing in the system and optionally capturing details like the date it went missing.
Borrowed Books: Generate a report listing all currently borrowed books along with the borrowing member's details and expected return date.
Technical Specifications:

Use Python for development.
Leverage libraries like csv or sqlite3 for data persistence (storing book and member information).
Implement a menu-driven interface for user interaction.
Consider error handling for invalid user inputs and edge cases.
Additional Considerations:

Extend the system to handle renewals for borrowed books.
Implement user authentication for secure access (optional, for more advanced projects).
Design a basic graphical user interface (GUI) using libraries like Tkinter for a more user-friendly experience (optional).
Deliverables:

Provide the complete Python code for the library management system.
Include a README file with instructions on how to run the program.
    """

req = Task(
    description = req_desc,
    expected_output="Requirements of the software mentioned.",
    agent=req_agent
)

verifiy_req = Task(
    description = f"""
    Verify whether requirements obtained is correct according to the task, return False if Any requirement is not followed.

    task: 
    {req_desc}

    requirements:
    {req}
    """,
    expected_output = "True or False",
    agent = verifier
)


