
print("RULE-BASED EXPERT SYSTEM")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()

facts = set()

if fever == "yes":
    facts.add("fever")
if cough == "yes":
    facts.add("cough")
if headache == "yes":
    facts.add("headache")

rules = [
    ({"fever", "cough"}, "possible_flu"),
    ({"fever", "headache"}, "possible_infection"),
    ({"cough"}, "possible_respiratory_problem")
]

print("\nForward Chaining:")

changed = True
while changed:
    changed = False
    for conditions, result in rules:
        if conditions.issubset(facts) and result not in facts:
            facts.add(result)
            print("Rule fired:", result)
            changed = True

goal = input("\nEnter goal to check: ").strip()

print("\nBackward Chaining:")
if goal in facts:
    print(goal, "is supported by the facts.")
else:
    print(goal, "cannot be established.")

print("This is an educational example, not a medical diagnosis.")
