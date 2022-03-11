import argparse  # see also: absl, click, etc
parser = argparse.ArgumentParser()
parser.add_argument(
        "x",
        help="number to exponentiate",
        type=int)

parser.add_argument(
        "--exponent", "-e",
        help="value of exponent",
        type=int,
        default=2)

args = parser.parse_args()

print(args.x ** args.exponent)
