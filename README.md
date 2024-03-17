# model-validation-eos30gr-and-eos9tyg
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

## License
All the code in this repository is licensed under a GPLv3 License.
