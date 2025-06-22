from tqdm import tqdm
import random

def get_valid_integer(prompt, min_val=0, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or (max_val is not None and value > max_val):
                print("❌ Please enter a valid number in range.")
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

def simulate_collection(n_pulls, desired_count, ssr_rate, pickup_rate=0.007, total_offbanners=114):
    off_rate = ssr_rate - pickup_rate
    collection = set()
    for _ in range(n_pulls):
        if random.random() < off_rate:
            pull = random.randint(0, total_offbanners - 1)
            if pull < desired_count:
                collection.add(pull)
            if len(collection) == desired_count:
                return True
    return False

def simulate_expectation(desired_count, ssr_rate, pickup_rate=0.007, total_offbanners=114, trials=10000):
    off_rate = ssr_rate - pickup_rate
    expected_total = 0
    for _ in range(trials):
        collection = set()
        pulls = 0
        while len(collection) < desired_count:
            pulls += 1
            if random.random() < off_rate:
                pull = random.randint(0, total_offbanners - 1)
                if pull < desired_count:
                    collection.add(pull)
        expected_total += pulls
    return expected_total / trials

def run_offbanner_analyzer():
    print("🎯 Off-Banner SSR Collection Analyzer")

    while True:
        mode = input("Choose gacha mode - Normal (3%) or Fes (6%)? (normal/fes): ").strip().lower()
        if mode in ("normal", "fes"):
            break
        print("❌ Please enter 'normal' or 'fes'.")

    ssr_rate = 0.03 if mode == "normal" else 0.06

    pulls = get_valid_integer("🔢 Enter number of total pulls: ", min_val=1)
    desired = get_valid_integer("⭐ How many specific off-banner SSRs do you want to collect? (1-114): ", min_val=1, max_val=114)

    print("\n📊 Simulating 100,000 players... (this may take a few seconds)")
    success = 0
    trials = 100000
    for _ in tqdm(range(trials), desc="🎮 Running Simulations", unit="player"):
        if simulate_collection(pulls, desired, ssr_rate):
            success += 1
    probability = (success / trials) * 100

    print("\n📈 Calculating expected pulls... (please wait)")
    expected = simulate_expectation(desired, ssr_rate)

    print("\n📈 Results:")
    print(f"🎯 Probability of collecting all {desired} off-banners in {pulls} pulls: {probability:.2f}%")
    print(f"📉 Expected number of pulls to collect all {desired} off-banners: {expected:.0f} pulls")

def main():
    print("\n🎲 Welcome to the Off-Banner SSR Analyzer!\n")
    while True:
        run_offbanner_analyzer()
        again = get_yes_no("\n🔁 Would you like to run another analysis? (y/n): ")
        if again != 'y':
            print("\n👋 Exiting Off-Banner SSR Analyzer. Goodbye!")
            break

if __name__ == "__main__":
    main()
