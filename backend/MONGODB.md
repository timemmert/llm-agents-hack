# Guide to get mongodb running

brew tap mongodb/brew
brew install mongodb-community

In root of project: mkdir -p ./data/db
mongod --dbpath ./data/db
