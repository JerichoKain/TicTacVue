#!/usr/bin/env sh

# abort on errors
set -e


# switch to master branch
git checkout master
git pull

# build
npm run build

# confirm this is the correct branch
git checkout gh-pages
# clean old build repo
git rm css/* img/* js/*
git commit -m "Preparing for Deployment"
# copy files
cp -rf dist/* .
# add resources and push to git
git add css/* img/* js/* index.html favicon.ico
git commit -m "Deployment"
git status
git push

#switch back to master.
git checkout master