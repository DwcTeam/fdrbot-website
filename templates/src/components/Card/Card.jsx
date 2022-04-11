import React, { Fragment } from "react";
import "./Card.css";

function Card({ icon, title, text }) {
    return (
        <Fragment>
            <div className="col-sm" id="card-animation">
                <div className="card text-light mb-3 card-fdr">
                    <div className="card-outline-fdr"></div>
                    <div className="h1 mt-3">
                        <br />
                        {icon}
                    </div>
                    <div className="card-body text-center">
                        <h4 className="card-title about-fdr">{title}</h4>
                        <p className="card-text text-light counter">{text}</p>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default Card;