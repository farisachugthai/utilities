# utilities

## Table of Contents


1. [Requirements](#requirements)
1. [Installation](#installation)
2. [Usage](#usage)
3. [License](#license)
4. [Contributions](#contributions)

This repository houses a number of functional scripts I utilize to
administer multiple workstations.

Quite honestly, it basically started with me saying 'Hey it'd be nice to
have a script do this for me.' every now and then.

That continued until I had enough scripts I was happy with to make a git repo
for them!

<a id="requirements"></a>

## Requirements

Python3 and Git are required in order to install this repository.

There are a plethora of extra dependencies that one can choose to download.

For example, on a functional Linux OS with the Anaconda Distribution setup,
one may create a conda environment using the file at
[./environment.linux.json](./environment.linux.json)

<a id="installation"></a>

## Installation

First clone the repository locally.

```shell
git clone https://github.com/farisachugthai/utilities.git
```

Then run setup.py to establish that the repository contains python modules.

```shell
python3 setup.py install
```

<a id="usage"></a>

##  Usage

Modules can be used to:

- Back up directories
- Automate the process of downloading plain-text files from the Internet.
- Automate downloading videos from YouTube.
- Symlink files recursively
- Inspect varying python modules.
- Introspect environment variables.
- Profiling nvim startup time.
- Strip trailing whitespace from a file.

<a id="license"></a>

## License

MIT

<a id="contributions"></a>

## Contributions

Even though these are mostly scripts I've thrown together;
I'd absolutely love any constructive criticism or
pointers on how to get any module listed to work better!

I hope it goes without saying, but if it doesn't, please don't hesitate
to fork or create an issue.
