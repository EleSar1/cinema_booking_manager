# Cinema Booking Manager

Cinema Booking Manager is a cinema booking management system that allows users to make, modify, or cancel bookings for movies, while administrators can manage the movie database.

## How it Works

The program consists of two main roles: **client** and **administrator**. Both interact with the system via a command-line interface (CLI) and can perform different actions.

### Clients
Users (clients) can:
- **Make a booking** for a movie by choosing the number of seats and providing their first and last name.
- **Modify an existing booking**, if they want to change the movie or the number of seats booked.
- **Cancel a booking** if they no longer wish to attend the screening.

### Administrators
Administrators can:
- **Add a new movie** to the system, specifying the title, genre, time, theater, price, and the number of available seats.
- **Modify details of an existing movie**, such as time or availability.
- **Delete a movie** from the database if it is no longer scheduled.

The system relies on two JSON files:
1. **cinemaData.json**: Contains movie details such as title, time, genre, price, and available seats.
2. **userData.json**: Stores user bookings, including their personal details and the movies they have booked.

## How to Run the Program

### Requirements
The program is written in Python and does not have any external dependencies, so you only need to have Python (preferably 3.12) installed on your machine.

### Running the Program

1. **Clone the repository**:
   You can clone the repository using the git command:
   ```bash
   git clone https://github.com/EleSar1/cinema_booking_manager.git

2. **Navigate to the project folder**:
   After cloning the repository, go into the project folder:

   ```bash
   cd cinema_booking_manager
   ```

3. **Run the program**:
   To start the program, execute the `main.py` file:

   ```bash
   python main.py
   ```

4. **Interacting with the Program**:
   Upon startup, you will be asked whether you are a **client** or an **administrator**:

   * Press 'c' to enter as a client.
   * Press 'a' to enter as an administrator.

   Follow the on-screen instructions to perform the desired actions.

### JSON Files

The program will automatically create **cinemaData.json** and **userData.json** files if they do not already exist. You can also create these files manually if needed.

* **cinemaData.json**: Should contain the details of the movies, such as title, genre, time, price, and available seats.
* **userData.json**: Should contain the booking data, including the user's first and last name, the movie they booked, and the number of seats.

### Key points:

- **cinemaData.json** stores the available movies.
- **userData.json** tracks the users' bookings.
- The program offers functionality for both clients and administrators.
```
