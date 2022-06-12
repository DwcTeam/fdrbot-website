import React, { Fragment } from "react";
import "./Loading.css"


class Loading extends React.Component {
    render() {
        return (
            <Fragment>
                <div id="loading" dir="ltr">
                    <div className="load">
                        <div className="loading">
                            <div className="loading-load"></div>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}


export default Loading;