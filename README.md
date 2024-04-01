# model-validation-eos30gr-
This is a model validation repository for the Outreachy contributors 2024. 

## Repository organisation
The repository is organised in folders:
- '/notebooks' contains the jupyter notebooks where most of the work is being developed
- '/data' contains all the .csv files. Model predictions are obtained outside this repository and saved in this folder. Subfolders might be created if needed
- '/src' contains important functions I will re-use throughout the repository, to avoid typing them each time
- '/figures' contains the plots I have produced during the model validation process
- 'requirements.txt' lists all the required packages to run the notebooks in this repository. If possible I also specify the version of the package I am using.

## Getting Started
- Install all prerequists required to run ersilia models from [here](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/installation)
- Clone the Ersilia Repo [here](https://ersilia.gitbook.io/ersilia-book/ersilia-model-hub/installation)
- Activate the env
  ```console
  conda activate <env-name>
  ```
### 1. Use Ersilia Hub to run the model
  - Fetch model
  ```console
     ersilia -v fetch eos9tyg
  ```
  - Serve model
 ```console
     ersilia serve eos3b5e
  ```
   - Serve model
 ```console
     ersilia serve eos3b5e
  ```
    - run prediction on model
        - For single input
         ```console
          ersilia -v api run -i "CCCC"
         ```
        - Running from a csv file
        ```console
        ersilia api run -i input.csv -o output.csv
         ```
### 2. Use Docker
    - Pull the image
    ```console
    docker pull ersiliaos/eos4wt0:latest
    ```
     - Serve and run model
     ```console
     ersilia serve eos4wt0 
    ersilia -v api run -i "CCCC"
    ```

### 3. Use this guide inorder to run model as a python funtion [here](https://github.com/ersilia-os/ersilia/blob/master/notebooks/output-python-api.ipynb)
## Where to get more help:
- Read Outreachy's contribution [tasks](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024)
- Read Ersilia's [documentation](https://ersilia.gitbook.io/ersilia-book)
- Get inspiration from Ersilia's work, for example on this repository for [data processing](https://github.com/ersilia-os/open-data-cleaning)
- Use Slack to ask the mentors and the other interns for help!
### 4. 00_eos30gr_model_bias.ipynb
- [Data Processing](#section-1)
- [Running Model](#section-2)
- [Evaluate Prediction](#section-3)
   - [histograph](#section-3-1)
   - [basic statistics mean,median...](#section-3-2)
   - [Threshold Prediction using 0.5 as value](#section-3-3)
   - [Frequency](#section-3-4)
   - [Top 10 non HERG Blocker molecules](#section-3-5)
   - [Top 20 non HERG Blocker molecules](#section-3-6)
### 5. 01_model_reproducibility.ipynb
- [deephERG(authers model) Output Cleaning and Calcualtion](#section-1)
- [eos30gr Output cleaning and calculation](#section-2)
- [Compare both outputs and visualize analysis](#section-3)
### 6. 02_external_validation.ipynb
In this notebook I will try to get the performance of the model on an external dataset I have obtained from ChEMBL [here](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL1794573/)
- The dataset contains [Small Molecule Inhibitors of the Human hERG Channel Activity](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL1794573/)
- I'll Clean the [dataset](https://www.ebi.ac.uk/chembl/g/#browse/compounds/filter/_metadata.related_assays.all_chembl_ids%3ACHEMBL1794573)
- Add class to represent hERG blokers
- Run prediction for the smae smile suing eos30(the model implemented by ersilia)
- I'll Clean the [dataset](https://www.ebi.ac.uk/chembl/g/#browse/compounds/filter/_metadata.related_assays.all_chembl_ids%3ACHEMBL1794573)
- Add class to represent hERG blokers
- Run prediction for the smae smile suing eos30(the model implemented by ersilia)
- Compare results using several ML performance metrics
## License
All the code in this repository is licensed under a GPLv3 License.
