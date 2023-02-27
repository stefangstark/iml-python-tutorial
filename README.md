# iml-python-tutorial
Python tutorial for Intro to Machine Learning at ETH

For git beginners, you can clone this repo by running
```
git clone git@github.com:stefangstark/iml-python-tutorial.git
```
on the command line and then enter the repository directory:
```cd iml-python-tutorial```

If you would like to interact with the notebooks, we recommend you create a virtual environment. Enviornments are useful tools to help maintain dependencies between packages across several projects. You can do this using `conda` and `pip`:

First, install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) and/or update `conda`:
```
conda update conda
```

Create an enviornment

```
conda create --name iml-python-tutorial python=3.9
```

Activate it
```
conda activate iml-python-tutorial
```

Install required packages
```
pip install -r requirements.txt
```

Now you should be able to start a notebook server with ```jupyter notebook```
