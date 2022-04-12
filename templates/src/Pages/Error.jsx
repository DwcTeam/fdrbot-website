import React, { Fragment } from "react";
import Warning from "../components/Warning/Warning";

class Error extends React.Component {
  render() {
    return (
        <Fragment>
        <Warning text="نعتذر منك هاذه الصفحة غير موجوده"/>
        </Fragment>
    );
  }
}

export default Error;