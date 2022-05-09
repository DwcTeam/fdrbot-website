import React, { Fragment } from "react";
import PropTypes from 'prop-types';


class SelectMenu extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        items: PropTypes.array.isRequired,
        defaultValue: PropTypes.any.isRequired,
        callback: PropTypes.func.isRequired,
        prefix: PropTypes.string,
        ignoreValues: PropTypes.array,
        defaultOption: PropTypes.string,
        isDisabled: PropTypes.bool,
        isDisabledDefault: PropTypes.bool,
    }
    render() {

        if (!this.props.items) {
            return (
                <div className="d-flex justify-content-center">
                    <div className="spinner-border text-primary" role="status">
                    <span className="sr-only">Loading...</span>
                    </div>
                </div>
                )
        }
        return (
            <Fragment>
                <div className="col">
                    <div className={"card bg-dark m-1" + (this.props.isDisabled ? " maintenance" : "")}>
                        <div className="card-body">
                            <h1 className="set text-light text-center">{ this.props.title }</h1>
                        </div>
                        <div className="card-footer">
                            <select 
                                className="form-select form-select-sm" 
                                aria-label=".form-select-sm example" 
                                disabled={this.props.isDisabled}
                                onChange={this.props.callback}
                            >   
                                {this.props.isDisabledDefault ? null : <option key="0" value="0" >{this.props.defaultOption ? this.props.defaultOption : "اختر .."}</option>}
                                {this.props.items.map((item, idx) => {
                                    if (this.props.ignoreValues && this.props.ignoreValues.includes(item.id)) {
                                        return <Fragment></Fragment>
                                    }
                                    return <option key={item.id} value={item.id ? item.id : item} className="text-start" selected={item.id === this.props.defaultValue} >{this.props.prefix ? this.props.prefix : ""}{item.name ? item.name : item}</option>
                                })}
                            </select>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}


export default SelectMenu;
