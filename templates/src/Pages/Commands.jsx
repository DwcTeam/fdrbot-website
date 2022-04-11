import React, { Fragment } from "react";
import Footer from "../components/Footer/Footer";
import Nav from "../components/Nav/Nav";
import Warning from "../components/Warning/Warning";

class Commands extends React.Component{
    render() {
        return (
            <Fragment>
                <Nav />
                <Warning text="نعتذر منك جاري العمل على هاذه الصفحه"/>
                <Footer />
            </Fragment>
        )
    }
}

export default Commands;