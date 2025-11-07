# Simple Dictionary CRUD Program
data = {}  # empty dictionary

while True:
    print("\n===== Dictionary CRUD Menu =====")
    print("1. Create / Add item")
    print("2. Read item")
    print("3. Update item")
    print("4. Delete item")
    print("5. Show all items")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
        print(f"{key} added successfully!")
    
    elif choice == "2":
        key = input("Enter key to read: ")
        print(f"{key} => {data.get(key, 'Not Found')}")
    
    elif choice == "3":
        key = input("Enter key to update: ")
        if key in data:
            value = input("Enter new value: ")
            data[key] = value
            print(f"{key} updated successfully!")
        else:
            print("Key not found!")
    
    elif choice == "4":
        key = input("Enter key to delete: ")
        if key in data:
            data.pop(key)
            print(f"{key} deleted successfully!")
        else:
            print("Key not found!")
    
    elif choice == "5":
        if data:
            print("All items in dictionary:")
            for k, v in data.items():
                print(f"{k} => {v}")
        else:
            print("Dictionary is empty.")
    
    elif choice == "6":
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please enter 1-6.")
