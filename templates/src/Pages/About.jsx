import React, { Fragment } from "react";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";
import Warning from "../components/Warning/Warning";

class About extends React.Component {
    render() {
        return (
            <Fragment>
            <Nav />
            <Warning text="نعتذر منك جاري العمل على هاذه الصفحه"/>
            <Footer />
            </Fragment>
        )
    };
}


export default About;