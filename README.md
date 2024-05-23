# Oil Prices Forecasting


## Overview

This repository contains code and resources for parsing, cleaning, and analyzing news articles related to the oil market. The primary objective is to collect news data, clean it, and mark it based on sentiment (positive or negative) for further analysis. The analysis aims to understand the relationship between news sentiment and oil price fluctuations.

## Repository Structure

### prepare
The `prepare` directory contains all the necessary scripts and data for preparing the dataset. It is organized into the following subdirectories and files:

#### datasets
This folder contains various CSV files used in different stages of data preparation.

#### notebooks
This folder contains Jupyter notebooks used for different stages of data preparation and analysis.

#### parser
This folder contains scripts for parsing news articles from the neftegaz.ru website:

### model
The `model` directory contains the essential components for training and evaluating machine learning models that predict oil price movements based on the sentiment of news articles.


## Data Preparation Workflow

1. **Parsing Data:**
   - The parsing scripts (`parser_neftegaz.ru_links.py` and `parser_neftegaz.ru_neft.py`) are used to scrape news articles from the neftegaz.ru website. The `parser_neftegaz.ru_links.py` script collects the URLs of relevant news articles, which are then used by `parser_neftegaz.ru_neft.py` to extract the actual content of the articles.

2. **Cleaning Data:**
   - The `clearing_dataset.ipynb` notebook is used to clean the scraped data. This involves:
     - Removing duplicate entries.
     - Handling missing or incomplete data.
     - Standardizing data formats to ensure consistency across the dataset.

3. **Marking Data:**
   - The `marking_dataset.ipynb` notebook is used to mark the cleaned news articles with sentiment labels. Each news article is categorized as either positive or negative based on its content.

4. **Combining Data:**
   - The `merge_two_files.py` script is used to merge the sentiment-marked news articles with historical oil price data. This combined dataset allows for comprehensive analysis, correlating news sentiment with oil price movements.

## Analysis Notebook: `analyze_sentiment_and_price.ipynb`

### Process

The `analyze_sentiment_and_price.ipynb` notebook is designed to analyze the relationship between the sentiment of news articles and the fluctuations in oil prices. The process involves the following steps:

1. **Data Loading:**
   - Load the merged dataset containing both sentiment-marked news articles and corresponding oil price data.

2. **Data Exploration:**
   - Conduct exploratory data analysis (EDA) to understand the distribution of sentiments and price data.
   - Visualize trends in oil prices over time and compare them with the frequency and sentiment of news articles.

3. **Sentiment Analysis:**
   - Analyze the distribution of positive and negative sentiments over the dataset.
   - Visualize the sentiment trends over time to observe any patterns or shifts.

4. **Correlation Analysis:**
   - Calculate and visualize the correlation between news sentiment and oil prices.
   - Use statistical methods to identify significant correlations and trends.

5. **Predictive Modeling:**
   - Develop and train predictive models to forecast oil prices based on news sentiment.
   - Evaluate the performance of the models using appropriate metrics.

### Results

The analysis results are summarized as follows:

- **Sentiment Trends:**
  - Identified periods with a high frequency of positive or negative news articles.
  - Observed sentiment shifts corresponding to major events in the oil market.

- **Correlation Insights:**
  - Found significant correlations between the sentiment of news articles and subsequent movements in oil prices.
  - Positive sentiment generally correlates with price increases, while negative sentiment correlates with price decreases.

- **Predictive Model Performance:**
  - Developed predictive models demonstrated a measurable ability to forecast oil price movements based on news sentiment.
  - The models showed promising accuracy, highlighting the potential of sentiment analysis in predicting market trends.

By following the steps outlined in the `analyze_sentiment_and_price.ipynb` notebook, users can replicate the analysis and gain insights into how news sentiment impacts oil price fluctuations. This can be valuable for investors, analysts, and researchers interested in the dynamics of the oil market.

