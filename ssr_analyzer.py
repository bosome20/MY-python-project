import random
import matplotlib.pyplot as plt

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

def run_simulations(n_pulls, trials=100000, pickup_rate=0.03):
    results = []
    for _ in range(trials):
        results.append(simulate_once(n_pulls, pickup_rate))
    return results

def calculate_percentile(results, actual_ssr):
    better_or_equal = sum(1 for r in results if actual_ssr >= r)
    return (better_or_equal / len(results)) * 100

def show_histogram(results, actual_ssr):
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=range(min(results), max(results)+2), edgecolor='black', color='skyblue')
    plt.axvline(actual_ssr, color='red', linestyle='dashed', linewidth=2, label=f'Your result: {actual_ssr}')
    plt.title("Distribution of SSR Pull Results (100,000 players)")
    plt.xlabel("SSR Count")
    plt.ylabel("Number of Players")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def ssr_analyze():
    print("\n🎯 SSR Pull Analyzer")

    while True:
        mode = input("Choose gacha mode - Normal (3% SSR) or Fes (6% SSR)? (normal/fes): ").strip().lower()
        if mode in ("normal", "fes"):
            break
        print("❌ Please enter 'normal' or 'fes'.")

    pickup_rate = 0.06 if mode == "fes" else 0.03

    while True:
        n = get_valid_integer("🔢 Enter number of pulls you've done: ")
        r = get_valid_integer("⭐ Enter number of SSRs you got: ")

        if r > n:
            print(f"\n❌ Invalid input: You entered {r} SSRs, but only did {n} pulls.")
            print("Please check your input and try again.\n")
            continue

        print("\n📊 Simulating luck... please wait.")
        results = run_simulations(n, pickup_rate=pickup_rate)
        percentile = calculate_percentile(results, r)

        print("\n📈 Results:")
        print(f"🎯 You got {r} SSRs out of {n} pulls.")
        print(f"🏅 You did better than or equal to {percentile:.2f}% of players in {mode} gacha.")

        show = get_yes_no("\n📉 Would you like to see a histogram of the results? (y/n): ")
        if show == 'y':
            show_histogram(results, r)

        break

def main():
    print("🎲 Welcome to the SSR Pull Analyzer!\n")
    while True:
        ssr_analyze()
        again = get_yes_no("\n🔁 Would you like to analyze another SSR pull? (y/n): ")
        if again != 'y':
            print("\n👋 Exiting SSR Pull Analyzer. Goodbye!")
            break

if __name__ == "__main__":
    main()
