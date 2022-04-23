import React, { Fragment } from "react";
import "./Loading.css"


class Loading extends React.Component {
    render() {
        return (
            <Fragment>
                <div id="loading" dir="ltr">
                    <div class="load">
                        <div class="load-one"></div>
                        <div class="load-two"></div>
                        <div class="load-three"></div>
                    </div>
                </div>
            </Fragment>
        )
    }
}


export default Loading;