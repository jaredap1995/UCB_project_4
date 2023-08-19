# Project Title

![](images/driving.gif)


## Description
An interactive search engine with selectible preferences for used cars on the market. 
We created two machine learning models to perform the following for the search engine:
1. Car price predictions (supervised learning)
2. Car recommendations (unsupervised learning)

## About Us:
* [Jared Perez](https://github.com/jaredap1995)
* [Matthew Fernandez](https://github.com/mattf4171)
* [Bryan Tsan-Tang](https://github.com/bryan-tt)
* [Jen Alfson](https://github.com/jennyalfi)
* [Kolton Kie](https://github.com/kottonxie)
* [Irfan Sencer Senyurt](https://github.com/sncrsenyurt)
* [Kyle Stephens](https://github.com/KAMAS-2058)

## Table of Contents
* Introduction
* About the Data
* Data Exploration & Cleaning
* Machine Learning Models
* Front-end Search Engine
* Challenges
* Conclusion

## Introduction
The purpose of this repository is to store all relevant data and scripting that enable the user to set up an interactive search engine which runs our machine learnling models to search thousands of car listings and give you the most relevant recommendations and pricing. All tools and resources were produced for Project 4 of the 2023 UC Berkeley Data Analytics Bootcamp.

### Conda Environment 
+ Create conda environment to ensure you have all needed packages
`conda create -n rootenv`
+ Activate conda environment
`conda activate rootenv`
+ Install needed packages
`pip install python scikit-learn pandas numpy psycopg2 flask ipython-sql sqlalchemy`

## About the Data
+ Data found within Kaggle: [https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data]
+ Download csv file and place it within `data/` directory

### Clean Data
[File: cleaning_analysis.ipynb](UCB_project_4/cleaning_analysis.ipynb)


+ Run `cleaning_analysis.ipynb`
+ `cleaning_analysis.ipynb` creates a new csv file within `data/` named `cleaned_vehicles.csv`

### Data Retrieval from pgAdmin 4
+ Set up DB named `proj_4`
+ run `used_cars.sql` within pgAdmin 4 **OR** DBeaver

## Data Exploration & Cleaning
[File: cleaning_analysis.ipynb](UCB_project_4/cleaning_analysis.ipynb)
#### Tools
* Jupyter Notebook
* Python Pandas
* Python Matplotlib

#### Observations & Steps Taken:



## Machine Learning Models
### Model 1: Price Prediction
[File: elasticnet_regression.ipynb](UCB_project_4/elasticnet_regression.ipynb)

#### Tools
* Jupyter Notebook
* Python Pandas
* Python Matplotlib
* Scikit-learn
* Psycopg2

#### Model Creation:



### Model 2: Car Recommender
[File: car_recommender.ipynb](UCB_project_4/car_recommender.ipynb)

* Jupyter Notebook
* Python Pandas
* Python Matplotlib
* Scikit-learn
* Psycopg2

#### Model Creation:



## Front-end Search Engine


## Challenges


## Conclusion


### Presentation slides
[Link to Google doc](https://docs.google.com/presentation/d/10NptDFIsyLr6rpVkYUle41i7pjDDeAlkMsKC66Z0VeY/edit#slide=id.g22b11322dec_1_1577)


### References
