import React, { Fragment } from "react";
import "./Card.css";


class Card extends React.Component {
    render() {
        return (
            <Fragment>
                <div className="col-sm card-animation">
                    <div className="card text-light mb-3 card-custome">
                        <div className="card-outline-custome"></div>
                        <div className="h1 mt-3">
                            <br />
                            {this.props.icon}
                        </div>
                        <div className="card-body text-center">
                            <h4 className="card-title about-fdr">{this.props.title}</h4>
                            <p className="card-text text-light counter">{this.props.text}</p>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default Card;