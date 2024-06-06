## Setting up Virtual Environment

### Create Virtual Environment:
```shell
python -m venv env
```

### Activate Virtual Environment:
```shell
env\Scripts\activate
```

### Install Required Libraries:
```shell
pip install requests beautifulsoup4 selenium pandas openpyxl seaborn numpy matplotlib scipy
```

## Data Collection and Cleaning

### If Data Needs to be Scraped:
1. Run `scrapper.py`:
```shell
python scrapper.py
```

2. Run `data_cleaning.py`:
```shell
python data_cleaning.py
```

### If Data Already Exists:

Work on the following files:
- `analysys_failed_start-ups.ipynb`
- `analysys_successfull_start-ups.ipynb`
