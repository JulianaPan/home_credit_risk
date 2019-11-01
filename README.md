# home_credit_risk

### Feature Engineering

- Continuous variables: mean, min, max, std
- Categorical variables: ratio of each value
- Table of number of generated features.

### Feature Selection

- WOE and IV: select features with IV larger than 0.02
- Feature Importance: using median to filter features 
- Table of number of selected features.

### Data Processing

- fill in missing values: 0xdeadbeef
- split dataset into training set and validation set (8:2)

### Modeling

- Random Forest (Benchmark)
- LightGBM
- Tuning parameters: cross validation (3 fold) RandomizedsearchCV
- Evaluation: AUC, KS (2 x 2 Pictures)
