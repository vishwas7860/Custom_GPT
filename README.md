# Custom_GPT
Train your model based on your data (PDF, Docs, Text, etc)
### NOTE: Use GPU System(Google Colab, Local System), If you are facing the issue in the local system during installation then please Update your MS Visual Studio
## Steps to train the model
#### 1. Run this command to install libraries `!pip install -r requirements.txt`
#### 2. Store the data(PDF, Docs, Text, etc) in SOURCE_DOCUMENTS folder
#### 3. Run this command to convert the data `!python ingest.py`
#### 4. Run this command to train and inference the model `!python PrivateGPT.py`

![image](https://github.com/vishwas7860/Custom_GPT/assets/61090712/5c903dd1-a5f7-490f-bbc6-a016bc72d63c)



# Data Scraping
### I scraped the Doctor Profile data from the most popular Hospital's website
#### 1. Go to the `Data Scraping` folder and run the `Data Scraper.ipynb` you will get the Profile URLs text file and `dataset.csv` file with full details
#### NOTE: Update `chromedriver.exe` based on your chrome browser version

# CSV to a Text file conversion
#### Run the `file_conversion.py`, it will make a text file in SOURCE_DOCUMENTS folder
