import random

def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("❌ Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'n'):
            return answer
        print("❌ Please enter 'y' or 'n'.")

def simulate_once(n_pulls, pickup_rate):
    count = 0
    for _ in range(n_pulls):
        if random.random() < pickup_rate:
            count += 1
    return count

def run_simulations(n_pulls, trials=100000, pickup_rate=0.007):
    guaranteed = n_pulls // 200
    results = []
    for _ in range(trials):
        natural = simulate_once(n_pulls, pickup_rate)
        results.append(natural + guaranteed)
    return results

def calculate_percentile(results, actual_pickups):
    better_or_equal = sum(1 for result in results if actual_pickups >= result)
    return (better_or_equal / len(results)) * 100

def gacha_analyze():
    n = get_valid_integer("\n🔢 Enter number of pulls you've done: ")
    guaranteed = n // 200

    if guaranteed > 0:
        print(f"\n💡 You automatically get {guaranteed} guaranteed pickup(s) from the point system.")
        print("👉 So your total pickups should include those guaranteed ones.")
        pickup_input = f"⭐ Enter total number of pickups you got (including guaranteed ones): "
    else:
        pickup_input = f"⭐ Enter total number of pickups you got: "

    r = get_valid_integer(pickup_input)

    # Validate logical constraints
    if r > n:
        print(f"\n❌ Invalid input: You entered {r} pickups, but only did {n} pulls.")
        print("That is not possible. Please check your input.")
        return False

    if r < guaranteed:
        print(f"\n❌ Invalid input: You entered {r} pickups, but you're guaranteed at least {guaranteed}.")
        print("Please check your inputs and try again.")
        return False

    print("\n📊 Simulating luck... please wait.")
    results = run_simulations(n)

    natural = r - guaranteed
    natural = max(natural, 0)

    percentile = calculate_percentile(results, r)

    print("\n📈 Results:")
    print(f"🎯 You got {r} pickups total ({natural} from natural pulls, {guaranteed} from guaranteed).")
    print(f"🏅 You did better than or equal to {percentile:.2f}% of players.")

    return True

def main():
    print("\n🎲 Welcome to the Gacha Luck Analyzer!\n")
    first_time = True
    while True:
        if not first_time:
            print()
        success = gacha_analyze()
        if not success:
            retry = get_yes_no("\n🔁 Invalid input detected. Would you like to try again? (y/n): ")
            if retry != 'y':
                print("\n👋 Exiting Gacha Luck Analyzer. Goodbye!")
                break
            else:
                continue
        again = get_yes_no("\n🔁 Would you like to try another simulation? (y/n): ")
        if again != 'y':
            print("\n👋 Exiting Gacha Luck Analyzer. Goodbye!")
            break
        first_time = False

if __name__ == "__main__":
    main()
