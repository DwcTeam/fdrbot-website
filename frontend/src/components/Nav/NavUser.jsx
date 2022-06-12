import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import { AppContext } from "../../Context";


class NavUser extends React.Component {
    static contextType = AppContext;
    render(){
        const user = this.context.user;
        return (
            <Fragment>
            <ul className="navbar-nav ml-auto text-center" dir="ltr">
                    <div className="btn-group d-block me-lg-1 mx-lg-1" role="group">
                        <button id="users" type="button" className="btn primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            <img src={ user.avatar } width="28" height="28" className="image" alt={ user.username } /> <b>{ user.username }</b>
                        </button>
                        <ul className="dropdown-menu saqrs" aria-labelledby="users">
                            <li className="nav-item">
                                <Link className="dropdown-item text-center primary" to="/dashboard">السيرفرات</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="dropdown-item text-center primary" to="/suggestions">ارسال اقتراح</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="dropdown-item text-center primary" to="/tasbih">تسبيح</Link>
                            </li>
                            <li>
                                <hr className="dropdown-divider bg-light" />
                            </li>
                            { 
                                user.admin && (
                                    <Fragment>
                                        <li className="nav-item">
                                            <Link className="dropdown-item text-center primary" to="/admin">لوحة الادمن</Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link className="dropdown-item text-center primary" to="/admin/log-sug">السجلات الاقتراحات</Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link className="dropdown-item text-center primary" to="/admin/azkar">السجلات الاذكار</Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link className="dropdown-item text-center primary" to="/admin/logs">السجلات</Link></li>
                                        <li>
                                            <hr className="dropdown-divider bg-light" />
                                        </li>
                                    </Fragment>
                                )
                            }                           
                            <li className="nav-item">
                                <Link className="dropdown-item text-center primary red" to="/logout">تسجيل خروج</Link>
                            </li>
                        </ul>
                    </div>
                        </ul>
            </Fragment>
        )
    }
}

export default NavUser;