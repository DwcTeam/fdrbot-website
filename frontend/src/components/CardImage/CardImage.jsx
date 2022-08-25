import React, { Fragment } from "react";
import FontAwesome from "react-fontawesome";

class CardImage extends React.Component {
    render() {
        return (
            <Fragment>
                <div class="features" dir={this.props.dir}>
                    <div class="features-list">
                        <div class="feature">
                                <div class="content">
                                    <FontAwesome name="fas fa-quran" />
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
