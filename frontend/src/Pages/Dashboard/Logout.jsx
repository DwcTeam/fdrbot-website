import React from "react";
import { Navigate } from "react-router-dom";


class Logout extends React.Component {
    render() {
        localStorage.removeItem("token");
        setTimeout(() => window.location.reload(), 1000);
        return <Navigate to="/" replace={true} />
    }
}


export default Logout;