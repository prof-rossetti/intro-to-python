
# Jupyer / IPython Notebooks

References:

  + https://docs.jupyter.org/en/latest/
  + https://docs.jupyter.org/en/latest/start/index.html

## Setup

Create a notebooks environment that has the `jupyter` package installed.

```sh
conda create -n notebooks-env python=3.10
conda activate notebooks-env
```

```sh
pip install jupyter
```

If your notebooks require other package dependencies, we need to install them as well in the active environment before running the notebook server.

## Usage

Navigate to a working directory where there are some notebooks

```sh
cd /path/to/directory/with/notebooks

```

Start the server, (then view the notebooks in your browser):

```sh
jupyter notebook
```
