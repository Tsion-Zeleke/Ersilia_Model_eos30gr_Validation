### Ersilia Model eos30gr Validation
   - eos30gr is a model with the prediction of hERG blockers of small molecules
#### - The following repo contains the model bias evaluation and debugging folder for the model eos30gr
# identified issues and details of steps taken are listed in the [debugging folder](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/tree/main/notebooks/Debugging%20model%20eos30gr) issue includes:
 - model outputs null when running using ersilia HUB log files, and output can be found [here]()
 - model has issues when imported details can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb)
 - running the model via docker gives null output as well

#### - The `ersilia fetch eos30gr --from__github` gives valid output but have issues. details are included [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb) issues include
 - model outputs values but gives error when redirected to output
#### - Detail steps taken to get issues despite getting errors can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/eos30gr_model_bias.ipynb)
 - I redirected all output into a txt file using a Python function
 - I tried processing the redirected JSON files, but file JSON decoder gives error
 - I processed the file using regex and successfully got the output files 123