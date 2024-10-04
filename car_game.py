command = ""
is_started = False
while True:
    command = input("'help' to list all possible commands. Type a command here > ").lower()
    if command == "help":
        print(
"""start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "start":
        if is_started:
            print("Car is already running...", is_started)
        else:
            is_started = True
            print("Car is running...", is_started)
    elif command == "stop":
        if not is_started:
            print("Car is already stopped", is_started)
        else:
            is_started = False
            print("Car is stopped", is_started)
    elif command == "quit":
        print("Program is shutting down...", is_started)
        break
    else:
        print("Invalid command")
