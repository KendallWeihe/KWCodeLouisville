# Kendall's <CodeLouisville> example project

### Steps:
1. What dataset interests me?
2. What questions could I answer?
3. How can I visualize those answers?
4. How should I design my system?

### Dataset:
- I checked out [Kaggle](https://www.kaggle.com/datasets)
- I found [this dataset](https://www.kaggle.com/uciml/mushroom-classification/data)

### Hypothesis/Questions:
- I think: "a majority of mushrooms that grow in the woods have a 'musty' odor"
- What is proof of this?
  - There are 9 different mushroom odors
  - There must be > 1 out of every 9 mushrooms, that grow in the woods, that have a musty odor

### Visualization:
- Pie chart of wooded mushrooms classified by odor

### Design/TODO:
- Download the dataset from Kaggle
- Create a SQL database call `KaggleThings`
- Create an SQL table inside the `KaggleThings` database called `Mushrooms`
  - I'm going to import the entire dataset, in case I want to answer other questions in the future
- Use a Python script to dynamically create the database
- Use another Python script to:
  - Compare the odor of mushrooms to their habitat
  - ...but also compare any other attribute (other than the habitat itself)

---------------------------------------------------

### `buildDB.py`
- shall create the database
- shall create the table
- shall import the data

### `compare.py`
- shall accept a comparison attribute as an argument
- shall query the db table to gather the proportion statistics
- shall visualize the comparison via a pie chart

### `mappings.json`
- shall contain mappings
  - from db column type elements
  - to (easy to understand) english words

### `raw_data/`
- contains raw CSV files

### `full_code/`
- fully functional program









<!-- ... -->
