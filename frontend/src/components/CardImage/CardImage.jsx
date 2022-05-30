import React, { Fragment } from "react";

class CardImage extends React.Component {
    render() {
        return (
            <Fragment>
                <div class="features">
                    <div class="features-list">
                        <div class="feature">
                                <div class="content">
                                    <i class="fa-solid fa-earth-asia"></i>
                                    <h2 className="about-fdr ">{this.props.title}</h2>
                                    <p className="text-white">{this.props.description}</p>
                                </div>
                            <img src={this.props.image} alt="purple website" />
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default CardImage;
