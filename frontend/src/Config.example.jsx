export const client_id = "";
export const redirect_uri = "";  // like: http://localhost:5000/auth
export const scopes = ["identify", "guilds", "email"];  // keep this

// Dont touch this
export const authorization_uri = `https://discordapp.com/oauth2/authorize?client_id=${client_id}&redirect_uri=${encodeURI(redirect_uri)}&scope=${scopes.join("%20")}&response_type=code`;
export const support_server_uri = "https://discord.com/invite/VX5F54YNuy";
export const invite_uri = `https://discord.com/api/oauth2/authorize?client_id=${client_id}&permissions=8&scope=bot%20applications.commands`

// You can change these
export const vote_uri = "https://discordbots.org/bot/728782652454469662/vote";
export const default_banner = "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png";

export const api_url = "http://164.92.202.125:4000";

