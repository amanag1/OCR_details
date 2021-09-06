# OCR_details

Prerequisites:
	
- miniconda should be installed for python 3.7


Follow the below steps to execute OCR Code :

1.	Download the zip of the repository OCR_details.
2.	After extracting the zip there will be a folder named as ...
3.	Now, copy the input data i.e. csvs folder also into the above extracted folder i.e. 
4.	After completing the above steps we will create new python environment.
5.	Here, we are creating python environment using conda and assuming that prerequisites are fulfilled.	
6.	Create new conda environment to run the application using the below command.
	
	conda create -n <ENV_NAME> python=3.7
	
	Activate env : conda activate <ENV_NAME>
	Deactivate env  : conda deactivate <ENV_NAME>
	
	We need to make sure that no other environment should be configure in bashrc script as first.
	If that's the case then we need to execute below command:
	export PATH=<path to the /bin of new env>:$PATH
	
7.	After successful creation of the conda environment we need to install few more packages in the environment.
	It can be done using pip.
	Therefore, install the below packages using requirements.txt present in repository using the command given below:

	pip install -r requirements.txt

8.	Now, we can activate our conda environment and will set some environment variables:
	export FLASK_ENV=development
	export FLASK_APP=ocr_code.py
	flask run
	
	At this point our flask server is up.

9.	Now, we will hit POST request to server using curl and it is given below:
	
	curl -H "Content-Type: application/json" -X POST -d '{"body":{"file_name":"<NAME OF FILE>","position":"[x0,y0,x2,y2]"}}' http://localhost:5000/search/text

	Input- curl -H "Content-Type: application/json" -X POST -d '{"body":{"file_name":"a.csv","position":"[50,50,1000,150]"}}' http://localhost:5000/search/text
	Output - {  "text": "State Bank Of India" }

	In case, if file does not exists then we will get the message for the same in text, like {"text": "File does not exists at given path" }
