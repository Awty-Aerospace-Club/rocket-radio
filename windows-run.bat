rem You cannot install python 3.8 from command line on windows, have it preinstalled
rem When installing python 3.8 on windows, please check the 'Add python3.8 to PATH' box
rem Or else when running the python script from the cmd it will open up Mircosoft Store
pip3 install pipenv
rem Shell scripts do not work on Windows without a WSL, just run the automation from here
pipenv install
pipenv lock
pipenv shell
rem Run python programs
python python_code\receiver.py
python python_code\chart_csv.py

