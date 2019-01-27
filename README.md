# account-traffic-api
An API used to host account traffic data and allow for the pull of this data for specific accounts

# Local use

Authorization is handled with a .env file that is not included:

```
echo 'ACCOUNT_API_SECRET=Example' > .env
```

The repo contains a dockerfile and makefile for easy local setup. You can use the following to build the image 
and automatically run it:

```
make run
```

The service will be running locally on port 8080. An example request is below:

```
curl -H "Authorization: {KEY HERE}" http://0.0.0.0:8080/traffic/api/v1/{account}
```

# Testing

The make file includes a seperate command to automatically run tests:

```
make test
```

Once built, the results of the tests will be outputted. 

# Deploy

Create heroku app

Download and install Heroku CLI - https://devcenter.heroku.com/articles/heroku-cli

Setup authorization enviornmental variable:

```
heroku config:set ACCOUNT_API_SECRET=<Key>
```

Initialize repo:

```
git init
```

Setup remote:

```
heroku git:remote -a <app name>
```

Deploy the app:

```
git add .
git commit -am "make it better"
git push heroku master
```

Make a request:

```
curl -H "Authorization: {KEY HERE}" https://<heroku app name>.com/traffic/api/v1/test
```
