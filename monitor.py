from class_web_monitor import WebappMonitor

def main():
    monitor = WebappMonitor()

    while True:
        print("\nWebapp Monitoring Tool")
        print("1. Add Website")
        print("2. Remove Website")
        print("3. Check Connectivity")
        print("4. List Websites")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter the website URL to add: ")
            print(monitor.add_website(website))
        elif choice == "2":
            website = input("Enter the website URL to remove: ")
            print(monitor.remove_website(website))
        elif choice == "3":
            print(monitor.check_connectivity())
        elif choice == "4":
            print(monitor.list_websites())
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()