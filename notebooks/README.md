### Ersilia Model eos30gr Validation
   - eos30gr is a model with the prediction of hERG blockers of small molecules
#### - The following repo contains the model bias evaluation and debugging folder for the model eos30gr
### identified issues and details of steps taken are listed in the [debugging folder](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/tree/main/notebooks/Debugging%20model%20eos30gr) issue includes:
 - model outputs null when running using ersilia HUB log files, and output can be found [here]()
 - the model has issues when imported details can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb)
 - running the model via docker gives null output as well

#### - The `ersilia fetch eos30gr --from__github` gives valid output but have issues. details are included [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb) issues include
 - model outputs values but gives error when redirected to output
#### - Detail steps taken to get issues despite getting errors can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/eos30gr_model_bias.ipynb)
 - I redirected all output into a txt file using a Python function
 - I tried processing the redirected JSON files, but file JSON decoder gives an error
 - I processed the file using regex and successfully got the output files 123

### 1. 00_eos30gr_model_bias.ipynb
- [Data Processing](#section-1)
- [Running Model](#section-2)
- [Evaluate Prediction](#section-3)
   - [histograph](#section-3-1)
   - [basic statistics mean,median...](#section-3-2)
   - [Threshold Prediction using 0.5 as value](#section-3-3)
   - [Frequency](#section-3-4)
   - [Top 10 non-HERG Blocker molecules](#section-3-5)
   - [Top 20 non-HERG Blocker molecules](#section-3-6)
### 2. 01_model_reproducibility.ipynb
- [deephERG(authors model) Output Cleaning and Calcualtion](#section-1)
- [eos30gr Output cleaning and calculation](#section-2)
- [Compare both outputs and visualize analysis](#section-3)
### 3. 02_external_validation.ipynb
In this notebook, I will try to get the performance of the model on an external dataset I have obtained from ChEMBL [here](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL1794573/)
- The dataset contains [Small Molecule Inhibitors of the Human hERG Channel Activity](https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL1794573/)
- I'll Clean the [dataset](https://www.ebi.ac.uk/chembl/g/#browse/compounds/filter/_metadata.related_assays.all_chembl_ids%3ACHEMBL1794573)
- Add class to represent hERG blockers
- Run prediction for the same smile using eos30gr(the model implemented by ersilia)
- I'll Clean the [dataset](https://www.ebi.ac.uk/chembl/g/#browse/compounds/filter/_metadata.related_assays.all_chembl_ids%3ACHEMBL1794573)
- Add class to represent hERG blockers
- Run prediction for the same smile using eos30gr(the model implemented by ersilia)
- Compare results using several ML performance metrics
