import React from "react";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import "./static/css/Root.css"
import "./static/css/normalize.css";
import "./static/css/App.css";
import Home from "./Pages/Home";
import About from "./Pages/About";
import Commands from "./Pages/Commands";
import Error from "./Pages/Error";
import Dashboard from "./Pages/Dashboard";


const App = () => {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
    {path: "/dashboard", element: <Dashboard />},
    {path: "/dashboard/{guild_id:int}", element: <Error />},
    {path: "*", element: <Error />}
  ])
  return routes
}

const AppWrapper = () => {
  return (
    <Router>
      <App />
    </Router>
  );
};

export default AppWrapper;