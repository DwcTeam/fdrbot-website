import React, { Fragment } from "react";

function Card({ icon, title, text }) {
    return (
        <Fragment>
            <div class="col-sm" id="card-animation">
                <div class="card text-light mb-3 card-fdr">
                    <div class="card-outline-fdr"></div>
                    <div class="h1 mt-3">
                        <br />
                        {icon}
                    </div>
                    <div class="card-body text-center">
                        <h4 class="card-title about-fdr">{title}</h4>
                        <p class="card-text text-light counter">{text}</p>
                    </div>
                </div>
            </div>
        </Fragment>
    )
}

export default Card;