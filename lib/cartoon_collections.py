def roll_call_dwarves(names):
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls):
    capitalized = [calls.capitalize()+"!" for calls in planeteer_calls]
    return capitalized

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(list):
    cheeses = ["cheddar", "gouda", "camembert"]
    for cheese in list:
        if cheese in cheeses:
            return cheese
    return None