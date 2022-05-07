import React from "react";
import PropTypes from 'prop-types';

class ColorMenu extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        defaultValue: PropTypes.string.isRequired,
        callback: PropTypes.func.isRequired,
        isDisabled: PropTypes.bool,   
    }
    
    render() {
        return (
            <div className="col">
                <div className={"card bg-dark" + (this.props.isDisabled ? " maintenance" : "")}>
                    <div className="card-body">
                        <h1 className="set text-light text-center">{this.props.title}</h1>
                    </div>
                    <div className="card-footer">
                        <input 
                            type="color" 
                            className="form-control form-control-color w-100"
                            value={this.props.defaultValue} 
                            title="Choose your color" 
                            disabled={this.props.isDisabled}
                            onChange={this.props.callback}
                        />
                        <br />
                  </div>
                </div>
              </div>
        );
    }
}

export default ColorMenu;