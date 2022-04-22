import React from "react";
import Redirect from "../components/Redirect/Redirect";
// import { ContextUser } from "../App.jsx"

class Auth extends React.Component {
    render() {
        const redirect_uri = "https://discord.com/api/oauth2/authorize?client_id=826712661844164609&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fouth&response_type=code&scope=email%20identify%20guilds"
        return <Redirect redirect_uri={redirect_uri} />
    }
}

export default Auth;