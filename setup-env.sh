pyenv uninstall 3.10.6

env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.12.3

rm -rf ./venv

python3 -m venv ./venv

source ./venv/bin/activate