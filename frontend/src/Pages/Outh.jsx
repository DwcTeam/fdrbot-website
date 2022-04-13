import React from "react";
import  { Navigate } from 'react-router-dom'
import axios from "axios";


class Outh extends React.Component {
    render(){
        var token = localStorage.getItem("token");
        if (token) {
            return (
                <Navigate to="/dashboard"/>
            )
        }
        else {
            axios.post("http://localhost:5000/auth/login", {})
        }
        return <Navigate to='/' replace={true} />
    }
}

export default Outh;