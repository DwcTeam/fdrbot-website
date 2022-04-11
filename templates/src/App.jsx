import React from "react";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import Home from "./Pages/Home";
import About from "./Pages/About";
import Commands from "./Pages/Commands";
import "./static/css/normalize.css";
import "./static/css/App.css";

const App = () => {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
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