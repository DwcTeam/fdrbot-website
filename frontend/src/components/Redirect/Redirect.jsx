import React, { Fragment } from "react";


class Redirect extends React.Component {
    componentDidMount() {
        window.location.href = this.props.redirect_uri
    }
    render() {
        return (        
        <Fragment>

        </Fragment>
        )

    }
}

export default Redirect;