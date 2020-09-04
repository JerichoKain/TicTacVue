# tic-tac-vue
A tic tac toe game writen with Vue.js with a Selenium / Jupyter Integration Test.

Handy Links and Documentation:
- [Live Demo](https://jerichokain.github.io/TicTacVue/)
- [Selenium docs](https://selenium-python.readthedocs.io/)
- [Jupyter docs](https://jupyter.readthedocs.io/en/latest/)
- [vue cli](https://cli.vuejs.org/guide/installation.html)
- [Vue.js](https://vuejs.org/)
- [jest.js](https://jestjs.io/)

## Project setup
### Prerequisites
This will assume you have the following software versions installed:

0) `$ git --version` => `2.17.1`
   * `$ sudo apt-get install git`
1) `$ node --version` => `v11.6.0`
   * Install `nvm` or "[node version manager]" if you haven't already.
   * `$ nvm install v11.6.0 && nvm use v11.0.6`
2) `$ npm --version` => `6.5.0-next.0`
   * This should be installed with `node`
3) `$ vue --version` => `3.3.0`
   * `$ npm install -g vue-cli` will get you the latest version
4) `$ python --version` => `3.6.7`
   * `$ sudo apt-get update python3 pip3`
5) `$ pip --version` => `19.0.3`
   * `$ pip instal pip`
6) `$ python -m virtualenv --verison` => `16.4.3`
   * `$ pip install virtualenv`
7) `$ jupyter --version` => `4.4.0`
   * `$ sudo apt-get install jupyter`

or just run this code if you trust it:
```bash
#installing nvm
curl https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
#refresh terminal after install
source ~/.profile
test "$(nvm --version)" == "0.36.0" && echo "nvm installed successfully" || (echo "nvm failed, please resolve error on your own." && exit 1)

#installing node v11.6.0
nvm install v11.6.0
nvm use v11.6.0
test "$(node --version)" == "v11.6.0" && echo "node installed successfully" || (echo "node failed, please resolve error on your own." && exit 1)
#assumes correct npm, install vue-cli
npm install -g vue-cli
test "$(vue --version)" == "3.0.0" && echo "vue-cli installed successfully" || (echo "vue-cli failed, please resolve error on your own." && exit 1)

#update from apt-get (git, python3, pip3) ((these come with ubuntu))
sudo apt-get update git python3 pip3
test "$(git --version)" == "2.17.1" && echo "git installed successfully" || (echo "git failed, please resolve error on your own." && exit 1)
test "$(python3 --version)" == "3.6.7" && echo "python3 installed successfully" || (echo "python3 failed, please resolve error on your own." && exit 1)
test "$(pip3 --version)" == "19.0.3" && echo "pip3 installed successfully" || (echo "pip3 failed, please resolve error on your own." && exit 1)

#install virtualenv
pip3 install virtualenv
test "$(python3 -m virtualenv --version)" == "16.4.3" && echo "virtualenv installed successfully" || (echo "virtualenv failed, please resolve error on your own." && exit 1)

#install jupyter
sudo apt-get install jupyter
test "$(jupyter --version)" == "4.4.0" && echo "jupyter installed successfully" || (echo "jupyter failed, please resolve error on your own." && exit 1)

#success
echo "prerequisites met, ready for setup!"
```
---
### Setup TicTacToe Board
0) Checkout this github repo and move into this directory
   * `$ git clone https://github.com/JerichoKain/TicTacVue.git && cd TicTacVue`
1) Install node.js dependecies to build vue app
   * `$ npm install`
2) Setup virtualenv and install python dependencies
   * `$ python3 -m virtualenv .venv`
   * `$ source .venv/bin/activate`
   * `$ pip3 install requirements.txt`
3) Build Vue app
   * `$ npm run build`

or just run this code if you trust it:
```bash
#clone repo and cd to the directory
git clone https://github.com/JerichoKain/TicTacVue.git && cd TicTacVue

#dependencies
npm install
python3 -m virtualenv .venv
source .venv/bin/activate
pip3 install requirements.txt

#build and serve
npm run build
```
---
### Serving and Running Jupyter Notebook for Tests.
* Serve Vue app
  * `$ npm run serve`
* Start Jupyter Notebook
   * `$ jupyter notebook`


[node version manager]: https://github.com/creationix/nvm