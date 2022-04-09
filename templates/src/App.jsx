import React from "react";
import { BrowserRouter as Router, useRoutes } from "react-router-dom";
import Home from "./Pages/Home";
import About from "./Pages/About";
import "./static/css/App.css";

const App = () => {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />}
  ])
  console.log(routes)
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