import React, { Fragment } from "react";
import { Link } from 'react-router-dom';
import "../static/css/App.css";


class Login extends React.Component {
    render() {
        return (
            <Fragment>
                <section className="bg-fdr">
                    <div className="container">
                        <div className="text-center" style={{ width: "100%", height: "366px" }}>
                            <div className="card-body" style={{ margin: "100px" }}>
                                <div className="card-text">
                                    <h1 className="card-title text-light login">يجب أن تسجل دخولك لـ تتمكن من رؤية الصفحة!</h1>
                                </div>
                                <div className="card-text py-5">
                                <Link to="/auth" class="btn login-button btn-lg me-2 mx-2">تسجيل الدخول باستخدام ديسكورد <i className="fab fa-discord btn-discord-logo"></i></Link>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </Fragment>
        )
    }
}

export default Login;