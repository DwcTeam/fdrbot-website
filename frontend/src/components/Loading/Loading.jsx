import React, { Fragment } from "react";
import "./Loading.css"


class Loading extends React.Component {
    render() {
        return (
            <Fragment>
                <div id="loading" dir="ltr">
                    <div className="load">
                        <div className="load-one"></div>
                        <div className="load-two"></div>
                        <div className="load-three"></div>
                    </div>
                </div>
            </Fragment>
        )
    }
}


export default Loading;