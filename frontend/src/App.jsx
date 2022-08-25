import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import "./static/css/Root.css"
import "./static/css/normalize.css";
import "./static/css/App.css";
import Home from "./Pages/Home";
import About from "./Pages/About";
import Commands from "./Pages/Commands";
import Error from "./Pages/Error";
import Dashboard from "./Pages/Dashboard/Home";
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
import DashboardGuild from "./Pages/Dashboard/Dashboard";
import Outh from "./Pages/Dashboard/Outh";
import Login from "./Pages/Dashboard/Login";
import axios from "axios";
import "bootstrap"
import Redirect from "./components/Redirect/Redirect";
import { api_url, authorization_uri, invite_uri, support_server_uri, vote_uri } from "./Config";
import { AppContext } from "./Context"
import Loading from "./components/Loading/Loading";
import Logout from "./Pages/Dashboard/Logout";
import Admin from "./Pages/Admin/Admin";
// import Suggestions from "./Pages/Suggestions";


function App() {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
    {path: "/dashboard/", element: <Dashboard />},
    {path: "/dashboard/:id", element: <DashboardGuild />},
    {path: "/outh", element: <Outh />},
    {path: "/login", element: <Login />},
    {path: "/logout", element: <Logout />},
    // {path: "/suggestions", element: <Suggestions />},

    // Admin
    {path: "/admin", element: <Admin />},

    // Redirect
    {path: "/auth", element: <Redirect redirect_uri={ authorization_uri } />},
    {path: "/support", element: <Redirect redirect_uri={ support_server_uri } />},
    {path: "/invite", element: <Redirect redirect_uri={ invite_uri } />},
    {path: "/vote", element: <Redirect redirect_uri={ vote_uri } />},

    {path: "*", element: <Error />}
  ])
  return routes
}


function AppWrapper() {
  var token = localStorage.getItem("token");
  if (token) {
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  }
  const [guilds, setGuilds] = useState();
  const [stats, setStats] = useState();
  const [user, setUser] = useState();
  const [isIssus, setIsIssus] = useState(false);
  if (token) {
    useEffect(() => {
      axios.get(api_url + "/user/@me/guilds").then(response => {
          setGuilds(response.data);
        }).catch((err) => {
          console.log(err);
          setIsIssus(true);
        });
    }, []);

    useEffect(() => {
      axios.get(api_url + "/user/@me").then(response => {
        setUser(response.data);
      }).catch((err) => {
        setIsIssus(true);
      });
    }, []);
  };

  useEffect(() => {
    axios.get(api_url + "/stats").then(response => {
      setStats(response.data);
    }).catch((err) => {
      setStats({});
    })
  }, []);
  if (!stats) {
    return <Loading />
  }
  if (token && !isIssus) {
    if (!user || !guilds) {
      return <Loading />
    }
  }
  return (
    <Router>
      <AppContext.Provider value={{
        available_guilds: guilds ? (!isIssus ? guilds.available_guilds : []) : [],
        unavailable_guilds: guilds ? (!isIssus ? guilds.unavailable_guilds : []) : [],
        is_login: user ? true : false,
        user: user ? user : {},
        stats: stats,
        issus: isIssus
      }}> 
          <Nav />
          <App />
          <Footer />
      </AppContext.Provider>
    </Router>
  );
};

export default AppWrapper;