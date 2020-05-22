# car_game
# text-based simulator car game
comment = ""
started = False
while True:
    comment = input("> ").lower()
    if comment == "start":
        if started:
            print("car has already started!")
        else:
            started = True
            print("the car has started.")
    elif comment == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car has stopped.")
    elif comment == "quit":
        print("thanks for playing. goodbye.")
        break
    elif comment == "help":
        print("""
                > start - start the car
                > stop - stop the car
                > quit - end the game
                > help - show menu
            """)
    else:
        print("we dont understand that!")

