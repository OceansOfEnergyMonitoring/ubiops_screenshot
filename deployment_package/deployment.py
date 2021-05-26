"""
The file containing the deployment code is required to be called 'deployment.py' and should contain the 'Deployment'
class and 'request' method.
"""

from selenium import webdriver
from datetime import datetime as dt 
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class Deployment:

    def __init__(self, base_directory, context):
        """
        Initialisation method for the deployment. It can for example be used for loading modules that have to be kept in
        memory or setting up connections. Load your external model files (such as pickles or .h5 files) here.

        :param str base_directory: absolute path to the directory where the deployment.py file is located
        :param dict context: a dictionary containing details of the deployment that might be useful in your code.
            It contains the following keys:
                - deployment (str): name of the deployment
                - version (str): name of the version
                - input_type (str): deployment input type, either 'structured' or 'plain'
                - output_type (str): deployment output type, either 'structured' or 'plain'
                - language (str): programming language the deployment is running
                - environment_variables (str): the custom environment variables configured for the deployment.
                    You can also access those as normal environment variables via os.environ
        """

        print("Initialising My Deployment")

    def request(self, data):
        """
        Method for deployment requests, called separately for each individual request.

        :param dict/str data: request input data. In case of deployments with structured data, a Python dictionary
            with as keys the input fields as defined upon deployment creation via the platform. In case of a deployment
            with plain input, it is a string.
        :return dict/str: request output. In case of deployments with structured output data, a Python dictionary
            with as keys the output fields as defined upon deployment creation via the platform. In case of a deployment
            with plain output, it is a string. In this example, a dictionary with the key: output.
        """

        print("Processing request for My Deployment")

        # You can run any code to handle the request here.

        # For a structured deployment, we return a Python dict with output. In this example, we are assuming this
        # deployment receives one input field called 'input' and outputs one field called 'output'
        # return {
        #     "output": data['input'] * random.random()
        # }
        
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        driver.get('https://waterberichtgeving.rws.nl/wbviewer/maak_grafiek.php?loc=EPL&set=wigo&nummer=4')

        xpath='/html/body/form/table/tbody/tr/td[1]/div/div[1]' # xpath of graph
        graph=driver.find_elements_by_xpath(xpath)[0] # find element of graph

        action = ActionChains(driver) # create action chain object
        action.double_click(graph).perform() # double click graph
        filename='Hs Europlatform {}.png'.format(dt.now().strftime('%Y-%m-%d %H')) # define filename incl date
        screenshot = driver.save_screenshot(filename) # save screenshot
        driver.quit()
