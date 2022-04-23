import React, {Fragment} from "react";
import FontAwesome from "react-fontawesome";
import { Link } from "react-router-dom";
import "./Warning.module.css"

class Warning extends React.Component {
    render() {
        return (
            <Fragment>
                <section className="bg-fdr">
                    <div className="container">
                        <div className="text-center">
                            <i className="fa-solid fa-triangle-exclamation fa-7x error-2" aria-hidden="true"></i>
                            <br />
                            <br />
                            <div className="error-1">
                                <div className="card error">
                                    <div className="card-body">
                                        <h2 className="card-text text-">
                                            <FontAwesome name="fa-solid fa-triangle-exclamation" /> { this.props.text }
                                        </h2>
                                        <Link to="/" className="nav-link">
                                            <button className="btn btn-outline-warning text-white c" type="submit">
                                            الصفحة الرئيسية
                                            </button>
                                        </Link>
                                    </div>
                                </div>
                            </div>
                            <br />
                            <br />
                            <br />
                        </div>
                    </div>
                </section>
            </Fragment>
        )
    }
}

export default Warning;
