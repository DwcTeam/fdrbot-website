import React, { Component, Fragment } from "react";
import "bootstrap/dist/css/bootstrap.css";
import "./Nav.module.css";
import logo from "../../static/images/logo.png";


export default class Nav extends Component {
    render() {
        return (
            <Fragment>
                <nav className="py-4">
                    <div className="navbar navbar-expand-lg bg-dark navbar-dark fixed-top">
                        <div className="container saqr">
                            <a href="/" className="navbar-brand d-lg-none d-block" id="male-1">
                                <img src={logo} alt="" width="50" height="50"></img>
                            </a>
                            <hr />
                            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainmenu">
                            <i className="fa-solid fa-bars" id="phone-navbar"></i>
                            </button>
                            <div className="collapse navbar-collapse text-center" id="mainmenu">
                                <ul className="navbar-nav nav-pillsnav navbar-nav ml-auto w-100 justify-content-center nav-pills">
                                    <li className="nav-item me-2 pe-3"><a href="/" className="nav-link">الرئيسية</a></li>
                                    <li className="nav-item me-2 pe-3"><a href="/about" className="nav-link">حول</a></li>
                                    <li className="nav-item me-2 pe-3"><a href="/commands" className="nav-link">الاوامر</a></li>
                                </ul>
                                <a href="/" className="navbar-brand d-none d-lg-block" id="male-1">
                                    <img src={logo} alt="" width="50" height="50"></img>
                                </a>
                                <ul className="navbar-nav nav-pillsnav navbar-nav ml-auto w-100 justify-content-center nav-pills">
                                    <li className="nav-item me-2"><a href="/vote" target="_blank" className="nav-link">تصويت للبوت</a></li>
                                    <li className="nav-item me-2"><a href="/invite" target="_blank" className="nav-link">أضف البوت</a></li>
                                    <li className="nav-item me-2"><a href="/support" target="_blank" className="nav-link">سيرفر الدعم</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </nav>
            </Fragment>
        )
    }
}
