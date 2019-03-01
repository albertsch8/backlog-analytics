# Backlog Analytics

Using python to get the most out of your backlog

# Sample Outputs

<p>
<img src="https://raw.githubusercontent.com/amandabertsch/backlog-analytics/master/images/velocity_output.png" width="260" />
<img src="https://raw.githubusercontent.com/amandabertsch/backlog-analytics/master/images/feature_output.png" width="300" />
<img src="https://raw.githubusercontent.com/amandabertsch/backlog-analytics/master/images/burnup_output.png" width="275" />

</p>

## About this Project

  **Who**: Anyone with basic programming experience that wants to leverage python to get more out of their backlog or excel files

 **What**: Notebooks to help you analyze and visualize excel backlog data with python
 basic_csv_editing.ipynb: edit csv files like you would in excel
- team_features_{OS}.ipynb: calculate sprint velocity, feature progress, burnup for a dev team
- product_features_{OS}.ipynb: calculate feature progress for a product or release

  **Why**: Python is a great, free, and easy to use tool that will let you gather new insight and visualizations of your data

## Running the Notebooks

**Option 1**: Run in Jupyter Notebooks

- Set up a virtual environment (venv) using the specified requirements in the requirements.txt folder

**Option 2**: Run in Google Colab or Azure Notebooks

- You can upload the notebooks to <a href= "https://colab.research.google.com/notebooks/welcome.ipynb#recent=true">Google Colab</a> or Azure Notebooks
[ Note: While Google Colab is free, it may not be a secure option to upload your data to depending on company policy]

## Creating the Azure DevOps Query for the Backlog Feature Analysis

1. Create a query with the following columns for your data at a feature level
<img src="https://raw.githubusercontent.com/albertsch8/backlog-analytics/master/images/feature_analysis_columns.png" width="800" />

2. Export (Windows) or copy query results (Mac) to a csv
3. Save the csv to the folder containing the notebook you're running

Note: Whether you export query data to excel (Windows only) or copy and paste the data will alter the data format. Be sure to use the correct code depending on method. Sample data for each export method is in the "sample_data" folder.