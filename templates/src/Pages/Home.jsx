import React, { Fragment } from "react";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";

class Home extends React.Component {
    render() {
        return (
            <Fragment>
                <Nav />
                <h1>Home</h1>
                <Footer />
            </Fragment>
        )
    };
}


export default Home;