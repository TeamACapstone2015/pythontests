[![Build Status](https://travis-ci.org/TeamACapstone2015/pythontests.png?branch=master)](https://travis-ci.org/TeamACapstone2015/pythontests)

# How to download the source

```sh
git clone https://github.com/TeamACapstone2015/pythontests.git
```

# How to run the tests locally

## Install nose

```sh
pip install nose
```

## Run nosetests

```sh
nosetests
```

# How to add your changes

Pretend you modified the file `tests.py`

You would first need to stage you changes with the `git add` command.

```sh
git add tests.py
```

After you have staged the files you want you need to make a commit with
the `git commit` command. This typically will open a editor where you
can type a message describing your changes instead the `-m` options
allows you to put the message in one statement.

```sh
git commit -m "your commit message"
```

# How to upload your changes

```sh
git push
```

# View the tests on Travis CI

https://travis-ci.org/TeamACapstone2015/pythontests
