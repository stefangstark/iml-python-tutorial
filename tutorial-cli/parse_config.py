import argparse
import yaml  # pip install pyyaml

parser = argparse.ArgumentParser()
parser.add_argument(
        "--config",
        help="path to config file",
        type=str,
        default="./configs/config.yaml"
        )

args = parser.parse_args()

config = yaml.load(open(args.config), yaml.SafeLoader)
print(config)
