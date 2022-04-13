import React, { Fragment } from "react";

class CardImage extends React.Component {
    render() {
        return (
            <Fragment>
                <div className="card py-5 card-1" style={{ maxWidth: "100%" }} dir={this.props.dir}>
                    <div className="row g-0 flex-row-reverse">
                        <div className="col-md-4">
                            <img id="saqr" src={this.props.image} alt="easy_to_use" className="img-fluid rounded-start p-5" />
                        </div>
                        <div className="col-md-8 text-end">
                            <div className="card-body">
                            <h2 className="card-title display-4 pt-5 about-fdr">{this.props.title}</h2>
                            <p className="card-text py-2 mx-auto text-white">{this.props.description}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default CardImage;
