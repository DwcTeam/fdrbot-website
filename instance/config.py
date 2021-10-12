TOKEN=""
CLIENT_ID=123
CLIENT_SECRET=""
REDIRECR_URI="http://127.0.0.1:5000/outh"
INVITE=f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&permissions=8&redirect_uri={REDIRECR_URI}&response_type=code&scope=bot%20applications.commands%20identify%20guilds"
AUTH_URL=f"https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECR_URI}&response_type=code&scope=identify%20guilds"
