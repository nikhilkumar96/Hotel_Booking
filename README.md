# hotel_booking
Machine Coding for Hotel Booking



Write a program to automate the allocation / deallocation of rooms upon check in / check out at a property. Some hotels prefer allocating rooms from lower floors to higher floors. For example - Jaisalmer as higher floors become very hot. Some hotels prefer allocating rooms from higher floors first - For example Goa or other beach destinations due to better views on higher floors.
 
For example:
Hotel 1 -> this hotel has 5 floor and each floor has 2 rooms each
Hotel 2 -> this hotel has 2 floor and each floor has 10 rooms each
 
For the purpose of this assignment assume that all rooms are of the same type and all room stays are of equal duration of 1 day.
 
I would like to see how you initialize the hotel data structure, a check in function and a check out function.
 
The check-in function should take in the number of rooms as an argument and return the room numbers of the allocated rooms as a List
The check out function should take in the room numbers to check out and vacate the rooms. A room that has been checked in once should not be allocated again until it is checked out.
 
Keep your design scalable such that you can demonstrate the top to bottom and bottom to top allocation mechanisms (one hotel will have a unique allocation mechanism) but can easily support other mechanisms in the future. Do support your code with appropriate unit tests.
 
Input (This is sample input, you can assume/change it):
You need to create hotel based on parameter.
check_in(number_of_requested_rooms = 5) Output - [101, 102, 103, 104, 105]
checkout(room_number = 101) Output - "Room has been successfully checkedout."
 
Expectations:
Code should be demoable. Either by using the main driver program or test cases.
Code should be modular. Code should have basic OO design.
Please do not jam in responsibilities of one class into another. Code should be extensible. Wherever applicable, use interfaces between different methods. It should be easy to add/remove functionality without re-writing the entire codebase. Code should handle edge cases properly and fail gracefully. Code should be legible, readable, and DRY.
