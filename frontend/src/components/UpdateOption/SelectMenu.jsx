import React, { Fragment } from "react";
import PropTypes from 'prop-types';


class SelectMenu extends React.Component {
    static propTypes = {
        title: PropTypes.string.isRequired,
        items: PropTypes.array.isRequired,
        defaultValue: PropTypes.string.isRequired,
        prefix: PropTypes.string,
        ignoreValues: PropTypes.array,
        defaultOption: PropTypes.string,
        isDisabled: PropTypes.bool
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
                            <select className="form-select form-select-sm" aria-label=".form-select-sm example" defaultValue={ this.props.defaultValue } disabled={this.props.isDisabled}>
                            <option key="0" value="0" >{this.props.defaultOption ? this.props.defaultOption : "اختر .."}</option>
                            {this.props.items.map((item, idx) => {
                                if (this.props.ignoreValues && this.props.ignoreValues.includes(item.id)) {
                                    return <Fragment></Fragment>
                                }
                                return <option key={idx} value={item.id ? item.id : item} className="text-start" >{this.props.prefix ? this.props.prefix : ""}{item.name ? item.name : item}</option>
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
