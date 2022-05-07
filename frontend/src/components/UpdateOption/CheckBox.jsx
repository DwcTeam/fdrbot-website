import React, { Fragment } from "react";
import PropTypes from 'prop-types';


class CheckBox extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        checked: PropTypes.bool.isRequired,
        callback: PropTypes.func.isRequired,
        description: PropTypes.string
    }
    render() {
        return (
            <Fragment>
                <div className="col" dir="ltr">
                    <div className="card bg-dark m-1">
                        <div className="card-body">
                            <h1 className="set text-light d-inline-flex float-end">{this.props.title}</h1>
                            <div className="form-check form-switch text-start h3 d-inline-flex rt">
                                <input 
                                    className="form-check-input rt" 
                                    type="checkbox" 
                                    role="switch" 
                                    aria-checked={true} 
                                    checked={this.props.checked} 
                                    onChange={this.props.callback} 
                                />
                            </div>
                                <p className="text-end h6 sfsf">{this.props.description}</p>
                        </div>
                    </div>
                </div>
            </Fragment>   
        )
    }
}

export default CheckBox;