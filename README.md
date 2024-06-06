*** create virtual environment for project ***
python -m venv env
env\Scripts\activate

*** install below libraries ***
pip install requests beautifulsoup4 selenium pandas openpyxl seaborn numpy matplotlib scipy

## if there is no structured and unstructured data files do below first
    *** 1. run scrapper.py ***
    command: python scrapper.py

    *** 2. run data_cleaning.py ***
    command: python data_cleaning.py

*** If there is already structured and unstructured data files, work on below files ***
analysys_failed_start-ups.ipynb
analysys_successfull_start-ups.ipynb


