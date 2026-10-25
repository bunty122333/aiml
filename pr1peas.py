
print("SMART HOME INTELLIGENT AGENT")

temperature = float(input("Enter room temperature: "))
motion = input("Is motion detected? (yes/no): ").lower()
dark = input("Is it dark? (yes/no): ").lower()

print("\nPEAS Representation")
print("Performance: Comfort and energy saving")
print("Environment: Smart home")
print("Actuators: Fan and light")
print("Sensors: Temperature and motion sensors")

if temperature > 30:
    print("Fan: ON")
else:
    print("Fan: OFF")

if dark == "yes" and motion == "yes":
    print("Light: ON")
else:
    print("Light: OFF")
