# flask echo - LINE Messaging API

Sample echo-bot using [Flask](http://flask.pocoo.org/)

## Getting started local env

```
$ export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

$ pip install -r requirements.txt
```

Run WebhookParser sample

```
$ python app.py
```

Run WebhookHandler sample

```
$ python app_with_handler.py
```

## Getting started with Heroku

### heroku button

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hiroyamaa/line-bot-sdk-python)

then set Webhook URL: `https://{YOUR_APP}.herokuapp.com/callback`

### deploy by yourself

```sh
heroku create
heroku info # then set Webhook URL: https://{YOUR_APP}.herokuapp.com/callback
heroku config:set LINE_CHANNEL_SECRET="..."
heroku config:set LINE_CHANNEL_ACCESS_TOKEN="..."
git push heroku master
heroku logs
```
