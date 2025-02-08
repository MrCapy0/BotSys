echo ""
echo "SETUP SYSTEM"
echo ""

# CURL
echo "INSTALL CURL"
echo ""

apt update
apt install curl

# PYENV
echo ""
echo "INSTALL PYENV IF NOT INSTALLED AND INSTALL DEPS"
echo ""

if [ ! -d "/root/.pyenv" ]; then
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
    echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
    echo 'eval "$(pyenv init - bash)"' >> ~/.profile

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init - bash)"' >> ~/.bash_profile

    curl -fsSL https://pyenv.run | bash
fi

apt update; apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

#PYTHON
echo ""
echo "INSTALL PYTHON AND DEPS"
echo ""

apt update
apt install python3-pip
apt install python3-venv
apt install tk-dev

pyenv uninstall 3.10.6

apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git


echo ""
echo "ADDED PERMISSION TO RUN run.sh"
echo ""
chmod +x run.sh
