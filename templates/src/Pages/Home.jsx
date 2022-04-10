import React, { Fragment } from "react";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";

class Home extends React.Component {
    render() {
        return (
            <Fragment>
                <Nav />
                
                <Footer />
            </Fragment>
        )
    };
}


export default Home;