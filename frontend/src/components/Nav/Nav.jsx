import React, { Component, Fragment } from "react";
import { Link } from "react-router-dom";
import "./Nav.css";
import logo from "../../static/images/logo.png";
import NavUser from "./NavUser";
import { AppContext } from "../../Context";


export default class Nav extends Component {
    static contextType = AppContext;
    render() {
        const isLogin = this.context.is_login;
        return (
            <Fragment>
                <nav className="py-4">
                    <div className="navbar navbar-expand-lg bg-dark navbar-dark fixed-top">
                        <div className="container saqr">
                            <Link to="/" className="navbar-brand d-lg-none d-block" id="male-1">
                                <img src={logo} alt="logo" width="50" height="50"></img>
                            </Link>
                            <hr />
                            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainmenu">
                            <i className="fa-solid fa-bars" id="phone-navbar"></i>
                            </button>
                            <div className="collapse navbar-collapse text-center" id="mainmenu">
                                <ul className="navbar-nav nav-pillsnav navbar-nav ml-auto w-100 justify-content-center nav-pills">
                                    <li className="nav-item me-2 pe-3"><Link to="/" className="nav-link">الرئيسية</Link></li>
                                    <li className="nav-item me-2 pe-3"><Link to="/about" className="nav-link">حول</Link></li>
                                    <li className="nav-item me-2 pe-3"><Link to="/commands" className="nav-link">الأوامر</Link></li>
                                </ul>
                                <Link to="/" className="navbar-brand d-none d-lg-block" id="male-1">
                                    <img src={logo} alt="" width="50" height="50"></img>
                                </Link>
                                <ul className="navbar-nav nav-pillsnav navbar-nav ml-auto w-100 justify-content-center nav-pills">
                                    <li className="nav-item me-2"><Link to="/vote" target="_blank" className="nav-link">تصويت للبوت</Link></li>
                                    <li className="nav-item me-2"><Link to="/invite" target="_blank" className="nav-link">أضف البوت</Link></li>
                                    <li className="nav-item me-2"><Link to="/support" target="_blank" className="nav-link">الدعم الفني</Link></li>
                                    {isLogin ? <NavUser /> : null}
                                </ul>
                            </div>
                        </div>
                    </div>
                </nav>
            </Fragment>
        )
    }
}
