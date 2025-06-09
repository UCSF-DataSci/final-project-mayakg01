# Global Cities: Lifestyle Factors
## Maya Gollamudi - Datasci 223 Final Project Written Description
### What factors best predict a city's happiness?

### Overview of Problem and Dataset
**Dataset:**
- Obtained from Kaggle: https://www.kaggle.com/datasets/prasertk/healthy-lifestyle-cities-report-2021
- Original source: https://www.lenstore.co.uk/research/healthy-lifestyle-report/
- Data compiled from several sources, including World Happiness Report, in the UK in 2021
- Features: Hours of sunshine, average cost of a bottle of water, obesity levels, life expectancy, pollution index, average annual hours worked, outdoor activities, number of take out places, cost of a monthly gym membership
- Target: happiness levels

**Aim & Background**
- We want to use the features in the healthy lifestyle cities dataset, from 2021, to classify the 44 cities into tiers of happiness (low, medium, high).
- This can help us better understand what features are predictive of overall happiness in a population
- It will also help us understand which cities have lifestyles that are predictive of greater or worse overall happiness
- The happiness levels used in this project are obtained from several sources, including the World Happiness Report
- The World Happiness Report (one of the dataset sources) asks participants to rate happiness on a numerical scale, 1-10

### Part 1 - Preprocessing
**Part 1 Focus**:
- Part 1 of this project focused on data cleaning and preprocessing to prepare the data for future analysis. 

**Data Cleaning steps:**
- 2 columns (cost of water bottle, cost of gym membership) contained currency information with the pound symbol in front of each number, these were removed for analysis
- 1 column (obesity levels) had % symbols in front of all values, these were removed
- All numeric columns converted to numeric format
- The dataset had missing values coded as "-", I removed these and marked them as NA values
- Then, all NA values were filled with the median value of that column
    - I chose not to drop any rows with NA values because it would lose valuable information about that city's features
- The dataset had happiness levels as a continuous variable, on a scale of 1-10. Because I wanted this to be a classification problem and not regression, I chose to categorize happiness into 3 discrete tiers: low happiness, medium happiness, and high happiness. 
    - I binned the happiness variable according to the distribution of happiness scores represented in this dataset. On a 1-10 scale (10 is the happiest), 0-5.5 was low happiness, 5.5-6.5 was medium happiness, above 6.5 was high happiness
- I also used a label encoder on the categorized variable version of happiness for future ML analysis (0,1,2 to represent low, medium, and high)
- This resulted in 8 low happiness, 12 medium happiness, 24 high happiness
- Saved the cleaned dataset

### Part 2 - Classification
**Aim**:
In order to go about this classification problem, I decided to test and compare 5 ML classification methods. Since this is a small dataset (44 cities), not all methods would be able to be a suitable choice. I chose to compare random forest, logistic regression, SVM, KNN, and a gradient boosted classifier. I compared the performance metrics of each to select the best classifier for this problem.

**Methodology**:
- Split data into training & testing sets (I used 30% testing, 70% training because of the small dataset size)
- Dropped the rank column (the ranking is based on the source's own weighting of each metric)
- Dropped the city column from the features used to predict the target: happiness level

1. Random Forest:
- Trained a RF classifier
- 100 trees, max depth of 5
- Used 5 fold cross-validation
- Examined cross-validation because of small sample size
Random Forest Results:
Test accuracy: 0.9286
CV accuracy: 0.7667 with SD of 0.2667

2. Logistic Regression:
- Max iterations: 100
- Cross validation
Logistic Regression Results:
Test accuracy: 0.9286
CV accuracy: 0.6000 (+/- 0.2667)

3. SVM classifier:
- Observed perfect test accuracy, likely not reliable and a result of overfitting because of the very small test sample size (this metric was disregarded)
- CV accuracy: 0.5667 (+/- 0.1633)

4. KNN Classifier:
- Selected k=3 for the number of neighbors
Test Accuracy: 0.7143
Cross-validation Accuracy: 0.6333 (+/- 0.2494)

5. Gradient boosted classifier
- Chose a max depth of 3, with the number of trees set at 100
Test Accuracy: 0.9286
Cross-validation Accuracy: 0.6333 (+/- 0.3266)

**Comparison Metrics Table**:
|   accuracy |   precision |   recall |   f1_score |   cv_mean |   cv_std |
|-----------:|------------:|---------:|-----------:|----------:|---------:|
|     0.9286 |      0.9524 |   0.9286 |     0.9306 |    0.7667 |   0.1333 |
|     0.9286 |      0.9429 |   0.9286 |     0.9302 |    0.6333 |   0.1633 |
|     0.7143 |      0.7727 |   0.7143 |     0.6669 |    0.6333 |   0.1247 |
|     0.9286 |      0.9365 |   0.9286 |     0.9256 |    0.6    |   0.1333 |
|     1      |      1      |   1      |     1      |    0.5667 |   0.0816 |

**Winner**: Random Forest
- Highest cv score, highest F1 score

Because the random forest model was the best selected model, I created a variable importance plot to choose the top 5 most important features for predicting happiness from the given features. The top 5 chosen features in order from most to least important were: Cost of a water bottle, Life expectancy, Pollution index, Obesity levels, Number of take out places/city.

### Part 3 - Visualization
- All visualizations saved to the visualizations directory as png or svg files

**Altair visualizations Results & Interpretations**:
- In our analysis, we made a boxplot for each feature that was selected as important by the RF model, separated by happiness tier. The altair interactive interface allows us to hover over each boxplot and view the descriptive statistics. 

1. Life expectancy
- Higher life expectancy seems clearly correlated with higher happiness level. 
- Some overlap in the whiskers of the box plots, especially between medium and low happiness levels.

2. Number of take out places
- Medium happiness tier has the highest median take out spots, high happiness tier has 3 extreme values
- May be confounded by size of city (ie: larger cities have a greater number of businesses)
- Considerable overlap in whiskers of the plots
- Does not seem strongly associated with happiness

3. Cost of a water bottle
- Higher cost of water bottles seems strongly correlated with higher happiness
- Likely confounded by city income levels and overall city wealth

4. Obesity levels
- Major overlap between all boxplots
- Low happiness tier has a much lower median obesity level than high happiness tier
- Also likely confounded by wealth, food access, and food insecurity in communities

5. Pollution levels
- Low pollution strongly correlated with high happiness

**Scatter Plots Results & Interpretations**:
1. Life expectancy vs. Pollution
- Low happiness tier data points are somewhat clustered towards the lower right end (lower life expectancy, higher pollution)
- High happiness tier data points more clustered towards upper left (higher life expectancy, lower pollution)
- Pollution may play a role in reducing life expectancy, both contribute to happiness

2. Life expectancy vs. Obesity
- A bit more random scatter observed
- Some high happiness, high obesity points, some low happiness high obesity
- Effects of obesity on life expectancy and happiness may depend on health care systems & access

**Streamlit Interactive Dashboard**:
- Rank in dataset does not exactly match our classification tiers, they may have prioritized other features
- Interactively visualize the distribution of cities for each feature, color coded by happiness tier

## Reflections, Conclusions, & Next Steps
Combining visual insights and the results from our best random forest model, the features that we observed had strong associations with happiness levels were pollution, cost of a water bottle, and life expectancy. It is important to note that happiness is very subjective and have significant person to person variation. 

The data and our analysis also had several limitations that it is important to be aware of. The way that I categorized happiness levels results in some class imbalance, where we had several more individuals in the high happiness tier than the other two tiers. A follow-up analysis could categorize these differently, perhaps with a higher threshold for "high happiness" to see how this affects the analysis. I also think there could be confounding by income levels, overall city and country wealth, age, and other factors. Future analyses could explore these potential confounders as well as possible interaction effects. 

From my understanding of the data sources, the happiness question was asked to participants in a simple and one-question way, simply asking them to rate their overall quality of life from 1-10. I think that happiness can be affected by so many variables, including mental health, stress, family and social support, a feeling of safety, and overall satisfaction/fulfillment in life. A future study could explore assessing happiness using multiple questions relating to these areas and weighting the participants' answers.

