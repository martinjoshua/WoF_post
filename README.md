# WoF_post
Warn-on-Forecast post processing scripts in Python 3

Requirements:

  - Python 3
  - netCDF4/pybrib
  - numpy
  - xarray
  - metplotlib
  - basemap/cartopy
  
Optional packages:

  - scikit image
  - sharppy
  - metpy

## Setup

### Install Prerequisites
Install the future package for upgrading files to Python 3.8
```
pip install future
```

### Install git lfs
Download and install git lfs using the [directions posted here](https://help.github.com/en/github/managing-large-files/installing-git-large-file-storage).
```
git lfs install
```

### Clone 
Clone this repository
```
git clone ...
```

### Create your anaconda environment
```
cd WoF_post
conda create --name wofs --file requirements.txt
conda activate wofs
```

### Upgrade individual modules to Python 3.8
```
futurize --nofix=division_safe -w scripts/post/news_e_post_ensemble.py
```

### Test a module
```
python -m scripts.post.news_e_post_ensemble -d ./data -o ./out/ -t 0
```
A summary file should appear in the /out/ directory
