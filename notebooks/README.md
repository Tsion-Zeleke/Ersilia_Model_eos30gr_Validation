### Ersilia Model eos30gr Validation
#### - The following repo contains the model bias evaluation and debugging folder for the model eos30gr
#idetified issues and details steps taken are listed in the [debugging folder](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/tree/main/notebooks/Debugging%20model%20eos30gr) issue includes:
 - model outputs null when running usnig ersilia HUB log files and outputcan be found [here]()
 - model have issues when imported details can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb)
 - running model via docker gives null output as well

#### - The `ersilia fetch eos30gr --from__github` gives valid output but have issues. deails are inlcuded [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb) issues include
 - model outputs values but gives error when redirected to output
#### - Detail steps taken to get issues despite getting error can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/eos30gr_model_bias.ipynb)
 - I redirected all output in to a txt file using a python function
 - I tried processing the redirected json files but file json decoder gives error
 - I processed the file to using regex and sucesfully got the output files
