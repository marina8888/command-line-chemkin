#!/bin/bash

mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install python3
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
sudo easy_install pip
git --version
pip3 install virtualenv


cd Desktop/
git clone https://github.com/marina8888/command-line-chemkin.git


pip3 virtualenv --python=python3.7 .
source bin/activate
pip install -r requirements.txt