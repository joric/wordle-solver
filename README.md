# Wordle Solver

Example telegram bot:

https://t.me/joricswordlesolverbot

## Bot setup

Use @Botfather at Telegram to get telegram token and set up the bot.

* "Sorry, this username is already taken. Please try something different."
	* Start from the beginning, use different display name (e.g. add a number)

### Heroku

Go to a Heroku Settings page, click Reveal Config Vars and then add your vars:

* BOT_TOKEN: '12345:abcde' (@Botfather gives you a token)
* URL: https://appname.domain.com (url of your app)

Since November 28, 2022 free dynos are replaced with eco dynos scaled down to 0,
so Heroku is no longer an option:

* https://help.heroku.com/RSBRUH58/removal-of-heroku-free-product-plans-faq

### Vercel

#### Add env variable to vercel.com

Add your telegram bot token as `BOT_TOKEN` variable

#### Register webhook

``` bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook?url=https://yourapp.vercel.app/api/webhook/"
```

## References

* https://github.com/python-telegram-bot/python-telegram-bot/wiki
* https://github.com/AliAbdelaal/telegram-bot-tutorial (Python + Flask + Heroku)
* https://github.com/Kylmakalle/heroku-telegram-bot (env examples)
* https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2
* https://github.com/potassium-chloride/WordleSolver
* https://habr.com/ru/post/647783/
* https://torrua.github.io/wordle-cracker
* https://wordle.belousov.one
* https://marinintim.com/slovl
* https://anch.info/rus/memories/2335
