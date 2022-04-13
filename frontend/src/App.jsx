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
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
import DashboardGuild from "./Pages/DashboardGuild";
import Outh from "./Pages/Outh";


const App = () => {
  let routes = useRoutes([
    {path: "/", element: <Home />},
    {path: "/about", element: <About />},
    {path: "/commands", element: <Commands />},
    {path: "/dashboard", element: <Dashboard />, children: [
      {path: ":id", element: <DashboardGuild />}
    ]},
    {path: "/outh", element: <Outh />},
    {path: "*", element: <Error />}
  ])
  return routes
}

const AppWrapper = () => {
  return (
    <Router>
      <Nav />
      <App />
      <Footer />
    </Router>
  );
};

export default AppWrapper;