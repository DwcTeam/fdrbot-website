import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import "./static/css/Root.css"
import "./static/css/normalize.css";
import "./static/css/App.css";
import Home from "./Pages/Home";
import About from "./Pages/About";
import Commands from "./Pages/Commands";
import Error from "./Pages/Error";
import Dashboard from "./Pages/Dashboard";
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
import DashboardGuild from "./Pages/DashboardGuild";
import Outh from "./Pages/Outh";
import Login from "./Pages/Login";
import axios from "axios";
import "bootstrap"
import Redirect from "./components/Redirect/Redirect";
import { authorization_uri, invite_uri, support_server_uri, vote_uri } from "./Config";
import { ContextGuilds, ContextState, ContextUser, IsLogin } from "./Context"
import Loading from "./components/Loading/Loading";

function App() {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
    {path: "/dashboard/", element: <Dashboard />},
    {path: "/dashboard/:id", element: <DashboardGuild />},
    {path: "/outh", element: <Outh />},
    {path: "/login", element: <Login />},

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
  const [guilds, setGuilds] = useState([]);
  const [stats, setStats] = useState({});
  const [user, setUser] = useState(null);
  if (token) {
    useEffect(() => {
      axios.get("/user/@me/guilds").then(response => {
          setGuilds(response.data);
        }).catch(err => {
          console.log(err);
        });
    }, []);

    useEffect(() => {
      axios.get("/user/@me").then(response => {
        setUser(response.data);
      }).catch(err => {
        console.log(err);
      });
    }, []);
  };

  useEffect(() => {
    axios.get("/stats").then(response => {
      setStats(response.data);
    }).catch(err => {
      console.log(err);
    })
  }, []);
  if (!stats) {
    return <Loading />
  }
  if (token) {
    if (!user || !guilds) {
      return <Loading />
    }
  }
  return (
    <Router>
      <ContextUser.Provider value={user}> 
        <ContextGuilds.Provider value={guilds}>
          <ContextState.Provider value={stats}>
            <IsLogin.Provider value={user ? true : false}>
              <Nav />
              <App />
              <Footer />
            </IsLogin.Provider>
          </ContextState.Provider>
        </ContextGuilds.Provider>
      </ContextUser.Provider>
    </Router>
  );
};

export default AppWrapper;