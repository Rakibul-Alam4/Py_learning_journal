# Improved Dictionary CRUD Program
data = {}  # খালি dictionary

def convert_value(value):
    """Value integer হলে convert করবে, নাহলে string থাকবে"""
    try:
        return int(value)
    except ValueError:
        return value

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
        key = input("Enter key: ").strip()
        if key == "":
            print("Key cannot be empty!")
            continue
        value = input("Enter value: ").strip()
        data[key] = convert_value(value)
        print(f"{key} added successfully!")
    
    elif choice == "2":
        key = input("Enter key to read: ").strip()
        if key in data:
            print(f"{key} => {data[key]}")
        else:
            print("Key not found!")
    
    elif choice == "3":
        key = input("Enter key to update: ").strip()
        if key in data:
            value = input("Enter new value: ").strip()
            data[key] = convert_value(value)
            print(f"{key} updated successfully!")
        else:
            print("Key not found!")
    
    elif choice == "4":
        key = input("Enter key to delete: ").strip()
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
