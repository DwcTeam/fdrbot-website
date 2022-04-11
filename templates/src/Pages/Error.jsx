import React, { Fragment } from "react";
import Footer from "../components/Footer/Footer";
import Nav from "../components/Nav/Nav";
import Warning from "../components/Warning/Warning";

class Error extends React.Component {
  render() {
    return (
        <Fragment>
        <Nav />
        <Warning text="نعتذر منك هاذه الصفحة غير موجوده"/>
        <Footer />
        </Fragment>
    );
  }
}

export default Error;