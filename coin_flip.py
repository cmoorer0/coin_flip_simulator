import random
import csv

def simulate_coin_flips(num_flips, output_file="coin_results.csv"):
    results = []  # store each flip as 'H' or 'T'
    heads = 0
    tails = 0

    # Perform the flips
    for _ in range(num_flips):
        if random.random() < 0.5:
            results.append("H")
            heads += 1
        else:
            results.append("T")
            tails += 1

    # Convert list of flips to single string
    flip_string = "".join(results)
    print(flip_string)  # ⬅️ Output ALL flips to console

    # Compute percentages
    exp_heads = (heads / num_flips) * 100
    exp_tails = (tails / num_flips) * 100

    # Write CSV summary
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Outcome", "Frequency", "Experimental", "Theoretical"])

        # Heads row
        writer.writerow([
            "1 H, 0 T",
            f"{heads}/{num_flips}",
            f"{exp_heads:.4f}%",
            "50%"
        ])

        # Tails row
        writer.writerow([
            "0 H, 1 T",
            f"{tails}/{num_flips}",
            f"{exp_tails:.4f}%",
            "50%"
        ])

    print("\nSummary written to", output_file)


# ------------ RUN SCRIPT ------------
if __name__ == "__main__":
    flips = int(input("Enter number of coin flips: "))
    simulate_coin_flips(flips)
