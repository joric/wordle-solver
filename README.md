# Wordle Solver

Example telegram bot (hosted on heroku):

https://t.me/joricswordlesolverbot

## Bot setup

Use @Botfather at Telegram to get telegram token and set up the bot.

* "Sorry, this username is already taken. Please try something different."
	* Start again from the bot name but (e.g. add a number)

If you add bot to channel it needs administrator rights to be able to reply.

## Heroku setup

Go to a Settings page, click Reveal Config Vars and then add your vars:

* TELEGRAM_TOKEN: '12345:abcde'
* HEROKU_URL: https://appname.herokuapp.com

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
