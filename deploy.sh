#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

#move to deployment folder.
cd ../TicTacVue-gh-pages/
#update
git pull
# confirm this is the correct branch
git checkout gh-pages
# clean old build repo
git rm css/* img/* js/*
git commit -m "Preparing for Deployment"
# copy files
cp -rf ../TicTacVue/dist/* .
# add resources and push to git
git add css/* img/* js/* index.html favicon.ico
git commit -m "Deployment"
git status
git push

cd -