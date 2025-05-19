# news-hook-tts

This is a test-server for News-Hook, a platform for sending alerts
The goal of this project is to simulate a client in a production environment


News-Hook is a platform for sending alerts
The user can send "alert-requests" to be informed when and if something of interest happens

Those alerts are essentially webhooks, since we give NH a url and a payload format

# Infrastructure

Since this is a test-server, we just use Swagger-UI to send the alert-requests

We will store those alert-requests in their own database every time we send them, for logging purposes
We will have an "alert-events" table, to store those webhooks, as we get them

## Project setup

```bash
$ npm install

# development
$ npm run start
# watch mode
$ npm run start:dev
# production mode
$ npm run start:prod
```

## Run tests

```bash
# unit tests
$ npm run test
# e2e tests
$ npm run test:e2e
# test coverage
$ npm run test:cov
```
