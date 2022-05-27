import { createContext } from "react";

export const AppContext = createContext({
    available_guilds: [],
    unavailable_guilds: [],
    is_login: false,
    user: {},
    stats: {},
    issus: false
})

