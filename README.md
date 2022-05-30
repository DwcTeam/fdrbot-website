<h1 align="center"> fdrbot.com - لوحة التحكم</h1>
<p align="center">
بوت فاذكروني لإحياء سنة ذكر الله
</p>

<p align="center">
<a href="https://discord.gg/VX5F54YNuy">
    <img alt="Discord" src="https://img.shields.io/discord/729526735749513267" />
</a> 
<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/DwcTeam/fdrbot.com" /> 
<a href="https://fdrbot.com">
    <img alt="Website" src="https://img.shields.io/website?down_color=red&down_message=offline&up_color=green&up_message=online&url=https%3A%2F%2Ffdrbot.com" />
</a>
</p>

<img src="https://i.imgur.com/KqogJwW.png" alt="https://fdrbot.com">

## About
This dashboard is a simple way to manage settings on [fdrbot](https://github.com/DwcTeam/fdrbot), backend is work on python flask and redis cache memory, the front end make with [reactjs](https://reactjs.org).


## Features

- Mange settings your server with out use bot.
- Simple interface fast to use.
- Some analytics for bot.

## How to use

### First you need to deploy the bot on your server. Go to [repository for bot](https://github.com/DwcTeam/fdrbot) and deploy it.
### Then you need to deploy this dashboard on your server. follow this guide:
- You need to install all this tools on your server:
    - [redis](https://redis.io/)
    - [nodejs](https://nodejs.org/en/)
    - [python3](https://www.python.org/)
    - [pip3](https://pip.pypa.io/)

- Then you need to run two web server on your server:
    - flask server (backend) to setup follow this commands:
        ```bash
        pip3 install -r requirements.txt
        python3 app.py  # or gunicorn app:app -b
        ```
    - react server (frontend) to setup follow this commands:
        ```bash
        cd frontend

        npm i  # or yarn
        npm run build  # yarn build
        
        npm i serve -g  # or yarn global add serve

        serve -s build  # or serve -s build -p 80
        ```
- Then all this is done, you can access dashboard on your server.
- i recommend you to use [nginx](https://www.nginx.com/) to make your server public.
