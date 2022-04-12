import React from "react";
import { Link } from "react-router-dom";
import "./Guild.css"

class Guild extends React.Component {
    render() {
        return (
            <div className="col  text-center">
            <div className="card h-75 card-1">
            <div className="card-body">
                <div className="sc-1vemdld-4 banner" style={{ background: `url('${this.props.banner}') center center / cover no-repeat`, backgroundSize: "100%" }}></div>
                <img src={ this.props.avatar }
                className="avatar-server justify-content-center align-items-center w-50 avalidated"
                alt={ this.props.name } />
            </div>
            </div>
            <div className="pt-2">
            <small className="text-muted float-end">{ this.props.name }</small>
            <Link to={ "/dashboard/"+this.props.id }>
                <button className={"btn primary card-title float-start pe-3 px-3 pt-2 pb-2 "+(this.props.alive ? "saqr-but" : "button-fdr")}>{this.props.alive ? "تحكم" : "أضافة البوت"}</button>
            </Link>
            </div>
        </div>
        )
    }
}

export default Guild;