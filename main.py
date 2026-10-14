def get_motor_status(temp):
    """Determines the status and message based on the motor temperature."""
    if temp >= 80:
        return "CRITICAL", "STOP", "Stop the simulated motor to prevent potential damage."
    elif temp >= 65:
        return "OVERHEATING", "RESTRICT", "Reduce or stop, according to the motor's limits."
    elif temp >= 50:
        return "WARNING", "MONITOR", "Temperature is elevated. Monitor closely."
    elif temp >= 20:
        return "NORMAL", "OPERATIONAL", "Motor temperature is within the normal range."
    elif temp >= 10:
        return "COOL", "OPERATIONAL", "Motor temperature is within the cool range."
    elif temp >= 0:
        return "COLD", "OPERATIONAL", "Motor is cold. Monitor performance during start-up."
    elif temp >= -20:
        return "LOW TEMPERATURE", "CAUTION", "Cold conditions may affect motor performance."
    else:
        return "EXTREMELY COLD", "CAUTION", "Temperature is extremely low. Verify the motor's operating limits."


def display_monitor(temp, temp_status, op_status, op_message):
    """Prints the formatted robot motor monitor dashboard."""
    print("=" * 35)
    print("\tROBOT MOTOR MONITOR")
    print("=" * 35)
    print(f" Motor Temperature: {temp}°C")
    print(f" Temperature Status: {temp_status}")
    print(f" Operational Status: {op_status}")
    print(f" Message to Display: {op_message}")
    print("=" * 35)


def main():
    try:
        # 1. Take user input
        input_temp = int(input("Enter motor temperature (°C): "))
        
        # 2. Process logic to get status values
        temp_status, op_status, op_message = get_motor_status(input_temp)
        
        # 3. Output the results
        display_monitor(input_temp,temp_status, op_status, op_message)
        
    except ValueError:
        print("Error: Please enter a valid integer for the temperature.")

if __name__ == "__main__":
    main()
