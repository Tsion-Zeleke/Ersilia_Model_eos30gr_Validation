# The folloeing repo contains the model bia evaluation and debugging folder for the model eos39gr
#idetified issues and details steps taken are lsited in the (debugging folder](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/tree/main/notebooks/Debugging%20model%20eos30gr)r issues includes:
 - model outputs null when running usnig ersilia HUB log files and output are included in the  of each steps and output can be found [here]()
 - model have issues when imported details can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/Debugging%20model%20eos30gr/python-api_eos30gr.ipynb)
 - running model via docker gives null output as well

# the `ersilia fetch eos30gr --from__github gives valied output but have issues. deails are inlcuded [here]() issues include
 - model outputs values but gives error when redirected in output
# Detail steps taken to get isses despite getting error can be found [here](https://github.com/Tsion-Zeleke/Ersilia_Model_eos30gr_Validation/blob/main/notebooks/eos30gr_model_bias.ipynb)
 - I redirected all output in to a txt file using a python function
 - I tried processing the redirected json files but file json decoder gives error
 - I processed the file to using rregex and got the output files
