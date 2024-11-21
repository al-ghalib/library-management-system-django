# Library Management API

The Library Management API facilitates the management of a library system where users (members) can view, borrow, and return books, while administrators can manage the library's collection. The system implements JWT authentication and role-based access control for secure and efficient operations.

---

## **Features**

### **1\. Authentication and Authorization**

- **JWT Authentication**: Ensures secure user authentication.
- **Role-Based Access Control**:
  - **Admin Role**: Full access to manage the library collection (CRUD operations).
  - **Member Role**: Limited access to view available books and perform borrowing/returning operations.

### **2\. Book Management (Admin Only)**

- **CRUD Operations**:
  - **Create**: Add new books to the library.
  - **Read**: View details of existing books.
  - **Update**: Modify information about books (title, author, availability, etc.).
  - **Delete**: Remove books from the library.

### **3\. Book Borrowing and Returning System**

- **Borrowing Books**: Members can borrow books if available.
- **Returning Books**: Members can return borrowed books, updating availability in the system.
- **Borrow Limit**: Members can borrow up to **5 books** at a time.

### **4\. Automatic Book Return Deadline and Fine Calculation**

- **Return Deadline**: A book must be returned within **14 days** of borrowing.
- **Overdue Fines**: Fine calculated as **5 BDT per day** for overdue returns.

---

## Technology Stack

- **Backend Framework**: Django
- **Database**: SQLite
- **API Development**: Django REST Framework (DRF)

---

## Installation

### Prerequisites

- Python 3.10+
- Virtual Environment
- `pip` for managing Python packages

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/al-ghalib/quizapp_restapi.git
   cd quizapp_restapi

   ```

2. Create and activate a virtual environment:

   ```bash
   pip install virtualenv
   virtualenv myenv
   .\myenv\Scripts\activate

   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate

   ```

5. Create a superuser (admin account):

   ```bash
   python manage.py createsuperuser

   ```

6. Run the development server:

   ```bash
   python manage.py runserver

   ```

7. Command to run test cases:

   ```bash
   python manage.py test

   ```

8. Access the API at http://127.0.0.1:8000
