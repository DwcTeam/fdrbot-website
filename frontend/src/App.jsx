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
import Auth from "./Pages/Auth";
import axios from "axios";
import "bootstrap"


export const ContextUser = React.createContext();
export const ContextGuilds = React.createContext();
export const ContextState = React.createContext();

function App() {
  

  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
    {path: "/dashboard/", element: <Dashboard />, children: [
      {path: ":id", element: <DashboardGuild />}
    ]},
    {path: "/outh", element: <Outh />},
    {path: "/login", element: <Login />},
    {path: "/auth", element: <Auth />},
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

  return (
    <Router>
    
      <ContextUser.Provider value={user}> 
        <ContextGuilds.Provider value={guilds}>
          <ContextState.Provider value={stats}>
          </ContextState.Provider>
        </ContextGuilds.Provider>
      </ContextUser.Provider>
      
    
      <Nav user={user}/>
      <App />
      <Footer />
    </Router>
  );
};

export default AppWrapper;