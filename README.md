# UCB_project_4


### Conda Env 
+ Create conda environment to ensure you have all needed packages
`conda create -n rootenv`
+ Activate conda environment
`conda activate rootenv`
+ Install needed packages
`pip install python scikit-learn pandas numpy psycopg2 flask ipython-sql sqlalchemy dash`

## Uncleaned Data
+ Data found within Kaggle: [https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data]
+ Download csv file and place it within `data/` directory

## Clean Data
+ Run `cleaning_analysis.ipynb`
+ `cleaning_analysis.ipynb` creates a new csv file within `data/` named `cleaned_vehicles.csv`

## Data Retrieval from pgAdmin 4
+ Set up DB named `proj_4`
+ run `used_cars.sql` within pgAdmin 4 **OR** DBeaver

## TODO

## References
