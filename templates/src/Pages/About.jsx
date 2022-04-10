import React, { Fragment } from "react";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";

class About extends React.Component {
    render() {
        return (
            <Fragment>
            <Nav />
            <h1>About</h1>
            <Footer />
            </Fragment>
        )
    };
}


export default About;