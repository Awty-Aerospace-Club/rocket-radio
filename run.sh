echo "Installing pip Dependencies..."
pipenv install
echo "Running python code..."
pipenv run sudo python3 python_code/receiver.py &
pipenv run python3 python_code/chart_csv.py
