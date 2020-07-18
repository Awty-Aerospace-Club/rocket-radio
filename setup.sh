### Dependencies ###
echo "Verifying System Dependencies..."

dpkg-query --status 'python3.8' > /dev/null ||
  (echo "Please install Python 3.8" && exit)

pip3 --version ||
  (echo "Please install pip3" && exit)

pip3 show --quiet pipenv ||
  (echo "Installing pipenv..." && pip3 install pipenv)

### PiPEnv Setup ###
echo "Setting up PIP Environment..."
pipenv install
