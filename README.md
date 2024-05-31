# Experiment title
Fine-tune a BERT transformer model for the task of binary classification 

The corresponding <a href:=https://www.notion.so/Plan-of-Experiment-PoE-template-efed4153dd7849c5979e9abb00293ec0>Plan of Experiment is provided here</a>.
\
The <a href:=https://www.notion.so/Experiment-Report-Template-450e66b444c74039bd1beda4f6c226a9>Full Report</a> describing the effort is also available.





## Goal of the experiment
The goal of this experiment is to fine-tune a BERT transformer model for the task of binary classification on a pre-prepared dataset, which includes patent claims and their corresponding relevant passages. In this context, each example in the dataset is labeled with either 1 - indicating an X citation (destroying novelty) or 0 - indicating an A citation (providing background).

The primary objective of the experiment is to develop a model capable of effectively distinguishing and classifying patent claims into these two specified categories. This will facilitate the automation of patent document analysis, significantly reducing the time and resources required for expert patent evaluation.


### How to clone the git repository on local machine?
    1. Go to the following link: https://github.com/HumanDevIP/classifier-nikita/tree/classifier
    2. Click the green "Code" button and copy the link to clone the repository.
    3. Open the terminal on your local machine and execute the following command:
        git clone git@github.com:HumanDevIP/classifier-nikita.git

### Project structure.
    Before starting take a look:
        .env file - file for storring credentials.
        .requirements.txt - list of dependecies. (pip install -r requirements.txt)

    Project consists of several main parts:
        1. Dataset.
            * prepared dataset
                + location: /data/origin
            
            * cleaned dataset
                + location: /data/clean
            
            * split data set into train val/test/train in 60/20/20 ratio
                + location: /data/work_data


        2. Python scripts for data prepareing.
            * script for converting files from .paequet to .csv
                + location: /notebooks/convert_files
                + comment: it of course possible to work directly with .parquet format, but going forward, I'm working with .csv format for     clarity. (this can be easily changed if necessary).
            
            * scripts for validating the prepared dataset.
                + location: /notebooks/validate_data
                + comment: these scripts are designed to clean the dataset from duplicates, none values, and items exceeding the allowed (specified by you) token limit. Each function has an explanation.
        

        3. A notebook for fine-tuning the Bert model on a prepared dataset.
            * location: /notebooks
                + file_name: classifier.ipynb
                + final weights will be saved in the same folder with .pt extension.
        
        
        4. A notebook for evaluating final weights using test dataset.
            * location: /tests
                + file_name: evaluate_final_weights.ipynb

### Environment
    - Compute environment local machine (limited data quantity).
        * macOS Sonoma 14.0
        * M1 cheap, 8gb
    
    - Compute environment local machine (limited data quantity).
        * google volab
        * NVIDIA Tesla T4, 16gb vram
    - Python 3.11.2





## Data
The dataset is provided in a .parquet file format and contains the following key columns of interest:

    - test: This column contains patent claims.
    - test_b: This column contains relevant passages.
    - label: This column indicates the type of citation, with the following possible values:
        + 0: Represents an "A" citation.
        + 1: Represents an "X" citation.





## Credentials
All experiments are logged in MLflow. Please fill in the credentials in the configuration file.
