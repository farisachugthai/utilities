#!/data/data/com.termux/files/usr/bin/bash
# Objectives:
# Establish a functional python development on Termux
# Maintainer: Faris Chugthai

# Pkg up automatically runs apt update && apt upgrade

set -eu
set -vx

pkg up -y

pip install -U pip
pip install -U virtualenv
pip install -U cheat
pip install -U youtube-dl

mkdir -pv "$HOME/virtualenvs/"
vhome="$HOME/virtualenvs"

virtualenv --python=python3.6 "$vhome/ipython"
source "$vhome/ipython/bin/activate" && pip install -U ipython flake8 && deactivate

virtualenv --python=python3.6 "$vhome/neovim"
source "$vhome/neovim/bin/activate" && pip install -U neovim python-language-server[all] && deactivate


#Now lets add some color to cheat
cd $PREFIX/etc/bash_completion.d/
curl -so cheat.bash https://raw.githubusercontent.com/chrisallenlane/cheat/master/cheat/autocompletion/cheat.bash


# Add a community repo so you can download Jupyter Notebooks on your phone!
# https://raw.githubusercontent.com/its-pointless/gcc_termux/master/setup-pointless-repo.sh

# Make the sources.list.d directory
if ! [[ -d "$PREFIX/etc/apt/sources.list.d" ]]; then
    mkdir -pv "$PREFIX/etc/apt/sources.list.d"
fi

# sources.list.d isn't a default folder
echo "deb [trusted=yes] https://its-pointless.github.io/files/ termux extras" >> $PREFIX/etc/apt/sources.list.d/pointless.list

# Download signing key from https://its-pointless.github.io/pointless.gpg
# TODO: Could this be a pipe and save the disk write?
wget -O "pointless.gpg" https://its-pointless.github.io/pointless.gpg
apt-key add pointless.gpg

# Now lets install all the necessary dependecies
pkg install -y clang fftw libzmq libzmq-dev freetype freetype-dev libpng libpng-dev pkg-conf

# Setup the compiler
# shellcheck
LDFLAGS=" -lm -lcompiler_rt"

# Install pip packages
install_pip_packages() {
local pi
pi="pip install -U"
"$pi" numpy
"$pi" matplotlib
"$pi" pandas
"$pi" jupyter
unset pi
}

install_pip_packages

exit 0
