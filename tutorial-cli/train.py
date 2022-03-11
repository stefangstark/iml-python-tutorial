import argparse
from pathlib import Path
import yaml  # pip install pyyaml
import torch


def load_model(**kwargs):
    raise NotImplementedError


def load_loss(**kwargs):
    raise NotImplementedError


def load_opt(params, **kwargs):
    raise NotImplementedError


def load_dataset(**kwargs):
    raise NotImplementedError


def train(model, opt, lossfxn, trainset, n_epochs=1):
    for epoch in range(n_epochs):
        for inputs, targets in trainset:
            opt.zero_grad()
            outputs = model(inputs)

            loss = lossfxn(outputs, targets)
            loss.backward()
            opt.step()

    return


def evaluate(model, testset):
    raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
            "outdir",
            help="directory to write to",
            type=str,
            )

    parser.add_argument(
            "--config",
            help="path to config file",
            type=str,
            )

    args = parser.parse_args()
    outdir = Path(args.outdir)

    config = yaml.load(open(args.config), yaml.SafeLoader)
    print(config)
    raise NotImplementedError("script is still a template")

    outdir.mkdir(exist_ok=True, parents=True)

    # Save the config to the outdir, so you know exactly what had been run
    # You can also save a git hash in case you need to roll back code
    with open(outdir/"config.yaml", 'w') as fout:
        yaml.dump(config, fout)

    model = load_model(**config["model"])
    opt = load_opt(model.parameters(), **config["optim"])
    lossfxn = load_loss(**config["loss"])
    trainset, testset = load_dataset(**config["dataset"])

    train(model, opt, lossfxn, trainset, config["training"]["n_epochs"])
    evals = evaluate(model, testset)

    # save evals & model
    evals.write(outdir/"evals.csv")
    torch.save(model.state_dict(), outdir/"model.pt")
