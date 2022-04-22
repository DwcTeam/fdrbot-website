import React, {Fragment} from "react";
import "./Commands.css"

class CommandsGroub extends React.Component {
    render() {
        return (
            <Fragment>
                <div className="card-header" style={{ 
                    borderRadius: "7px 7px 0px 0px", 
                    backgroundColor: "var(--color3)", 
                    color: "var(--color1)"}}
                >
                    <h1>{this.props.title}</h1>
                </div>
                <div className="card-body" style={{ 
                    backgroundColor: "var(--dark-section-bg-1)", 
                    color: "var(--color1)" }}
                >          
                    {this.props.childrens}
                </div>
            </Fragment>
        )
    }
}

class Command extends React.Component {
    render() {
        return (
            <Fragment>
                <div className="col p-2" id={ "#" + this.props.name.replace(" ", "_") }>
                    <div className="card command m-1">
                        <div className="card-body pb-4">
                            <h3 className="card-title cmd-1 float-start">
                                <code>/{this.props.name}</code>
                            </h3>
                            <p className="card-text cmd-2 float-end">{this.props.description}</p>
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}


export {Command, CommandsGroub}
