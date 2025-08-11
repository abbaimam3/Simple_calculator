def task1_sum_of_integers():
    print("\n=== Task 1: Sum of Integer List ===")
    numbers = input("Enter integers separated by spaces: ").split()
    int_list = [int(num) for num in numbers]
    print("Sum:", sum(int_list))

def task2_favorite_books():
    print("\n=== Task 2: Favorite Books ===")
    favorite_books = (
        "Atomic Habits",
        "Deep Work",
        "The Psychology of Money",
        "The Alchemist",
        "Thinking, Fast and Slow"
    )
    print("My favorite books:")
    for book in favorite_books:
        print(f"- {book}")

def task3_person_dictionary():
    print("\n=== Task 3: Person Information ===")
    person = {
        "name": input("Enter your name: "),
        "age": int(input("Enter your age: ")),
        "favorite_color": input("Enter your favorite color: ")
    }
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")

def task4_common_set_elements():
    print("\n=== Task 4: Common Set Elements ===")
    set1 = set(map(int, input("Enter first set of numbers (space-separated): ").split()))
    set2 = set(map(int, input("Enter second set of numbers (space-separated): ").split()))
    common_elements = set1 & set2
    print("Common elements:", common_elements)

def task5_odd_length_words():
    print("\n=== Task 5: Odd-Length Words ===")
    words = input("Enter words separated by spaces: ").split()
    odd_length_words = [word for word in words if len(word) % 2 != 0]
    print("Words with odd character count:", odd_length_words)

def main():
    while True:
        print("\n===== Python Data Structures Practice =====")
        print("1. Sum of Integer List")
        print("2. Favorite Books Tuple")
        print("3. Person Information Dictionary")
        print("4. Common Set Elements")
        print("5. Odd-Length Words")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == '1':
            task1_sum_of_integers()
        elif choice == '2':
            task2_favorite_books()
        elif choice == '3':
            task3_person_dictionary()
        elif choice == '4':
            task4_common_set_elements()
        elif choice == '5':
            task5_odd_length_words()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()