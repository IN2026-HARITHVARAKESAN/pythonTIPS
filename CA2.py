"""This file contains the boiler control logic. It manages the boiler's operational states, interlock switch, and event logging."""
import time
import os

def start_boiler():
    """start_boiler() initiates the boiler start sequence"""
    global interlock_switch, boiler_status
    if interlock_switch != "Closed":
        print("Cannot start boiler. Close the interlock switch first.")
        return
    if boiler_status != "Ready":
        print("Cannot start boiler. Reset the lockout first.")
        return
    boiler_status = "Pre-Purge"
    print("Boiler start sequence initiated.")
    log_event("Boiler start sequence initiated.")

    for time_undergone in range(11):
        print(f"Pre-Purge: {10-time_undergone} seconds remaining")
        time.sleep(1)

    print("Pre-Purge completed.")
    log_event("Pre-Purge completed.")

    for time_undergone in range(11):
        print(f"Ignition: {10-time_undergone} seconds remaining")
        time.sleep(1)

    print("Ignition completed.")
    log_event("Ignition completed.")

    boiler_status = "Operational"
    print("Boiler is now operational.")
    log_event("Boiler is now operational.")

def stop_boiler():
    """stop_boiler() stops the boiler and sets it to lockout state"""
    global boiler_status
    if boiler_status=="Operational":
        boiler_status = "Lockout"
        print("Boiler stopped. System in Lockout.")
        log_event("Boiler stopped. System in Lockout.")
    else:
        print("Boiler is not running.")

def simulate_error():
    """simulate_error() simulates an error condition in the boiler"""
    global boiler_status
    if boiler_status=="Operational":
        boiler_status = "Lockout"
        print("Simulated error occurred. Boiler in Lockout.")
        log_event("error occurred. Boiler in Lockout.")
    else:
        print("Boiler is not running. Cannot simulate error.")

def toggle_interlock():
    """toggle_interlock() toggles the state of the interlock switch"""
    global interlock_switch
    if interlock_switch == "Open":
        interlock_switch = "Closed"
    else:
        interlock_switch = "Open"

    message = f"Interlock Switch toggled to {interlock_switch}."
    print(message)
    log_event(message)

def reset_lockout():
    """reset_lockout() resets the boiler to a ready state"""
    global interlock_switch, boiler_status
    if interlock_switch == "Closed":
        boiler_status = "Ready"

        print("Boiler Status changed to Ready.")
        log_event("Boiler Status changed to Ready")

    else:
        print("Please close the Run Interlock switch before resetting.")

def view_event_log():
    """view_event_log() displays the contents of the event log"""
    try:
        with open("Boiler_Log.txt", "r") as log_file:
            print("\nEvent Log:")
            print(log_file.read())
    except FileNotFoundError:
        print("No event log found.")

def log_event(message):
    """log_event() logs an event with a timestamp to the event log file"""
    if not os.path.exists("Boiler_Log.txt"):
        with open("Boiler_Log.txt", "w") as log_file:
            log_file.write("Timestamp , Event\n")
    with open("Boiler_Log.txt", "a") as log_file:
        log_file.write(f"{time.ctime()}, {message}\n")

if __name__ == "__main__":
    interlock_switch = "Open"
    boiler_status = "Lockout"
    while True:
        
        print("\n========== BOILER CONTROLLER ==========")
        print("Boiler Status:", boiler_status)
        print("Interlock Switch:", interlock_switch)

        print("\n1. Start Boiler Sequence")
        print("2. Stop Boiler Sequence")
        print("3. Simulate Boiler Error")
        print("4. Toggle Run Interlock Switch")
        print("5. Reset Lockout")
        print("6. View Event Log")
        print("7. Exit Application")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            start_boiler()
        elif choice == "2":
            stop_boiler()
        elif choice == "3":
            simulate_error()
        elif choice == "4":
            toggle_interlock()
        elif choice == "5":
            reset_lockout()
        elif choice == "6":
            view_event_log()
        elif choice == "7":
            print("Exiting Boiler Controller. Goodbye!")
            log_event("Application exited.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")