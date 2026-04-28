import asyncio
from datetime import datetime

# Type annotations for data structures
BookStore = dict[int, str]
library_inventory: BookStore = {
    101: "C++ for Beginner",
    102: "Data Structures 101"
}

async def borrow_book(user_id: int, book_id: int) -> str:
    #Simulates the asynchronous process of borrowing a book
    print(f"User {user_id} is requesting book {book_id}...")



    
    # Simulate a network/database delay
    await asyncio.sleep(4) 
    
    if book_id in library_inventory:
        book_title = library_inventory.pop(book_id)
        return f"SUCCESS: User {user_id} borrowed '{book_title}' at {datetime.now()}"
    return f"ERROR: Book {book_id} is not available."

async def main():
    # Simulating multiple users accessing the system at the same time
    print("--- Library API Simulation Starting ---\n")
    
    # Create tasks to run concurrently and corotuine object
    task1 = borrow_book(1, 101)
    task2 = borrow_book(2, 102)
    task3 = borrow_book(3, 101) # This should fail as 101 is taken
    
    results = await asyncio.gather(task1, task2, task3)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())