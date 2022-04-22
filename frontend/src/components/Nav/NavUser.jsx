import React, { Fragment } from "react";
import { Link } from "react-router-dom";


class NavUser extends React.Component {
    render(){
        return (
            <Fragment>
                <ul class="navbar-nav ml-auto text-center" dir="ltr">
                    <div class="btn-group d-block me-lg-1 mx-lg-1" role="group">
                        <button id="users" type="button" class="btn primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            <img src={ this.props.user.avatar } width="28" height="28" class="image" alt={ this.props.user.username } /> <b>{ this.props.user.username }</b>
                        </button>
                        <ul class="dropdown-menu saqrs" aria-labelledby="users">
                            <li class="nav-item">
                                <Link class="dropdown-item text-center primary" to="/dashboard">السيرفرات</Link>
                            </li>
                            <li class="nav-item">
                                <Link class="dropdown-item text-center primary" to="/suggestions">ارسال اقتراح</Link>
                            </li>
                            <li>
                                <hr class="dropdown-divider bg-light" />
                            </li>
                            { 
                                this.props.user.is_admin && (
                                    <Fragment>
                                        <li class="nav-item">
                                            <Link class="dropdown-item text-center primary" to="/admin">لوحة الادمن</Link>
                                        </li>
                                        <li class="nav-item">
                                            <Link class="dropdown-item text-center primary" to="/admin/log-sug">السجلات الاقتراحات</Link>
                                        </li>
                                        <li class="nav-item">
                                            <Link class="dropdown-item text-center primary" to="/admin/azkar">السجلات الاذكار</Link>
                                        </li>
                                        <li class="nav-item">
                                            <Link class="dropdown-item text-center primary" to="/admin/logs">السجلات</Link></li>
                                        <li>
                                            <hr class="dropdown-divider bg-light" />
                                        </li>
                                    </Fragment>
                                )
                            }                           
                            <li class="nav-item">
                                <Link class="dropdown-item text-center primary red" to="/logout">تسجيل خروج</Link>
                            </li>
                        </ul>
                    </div>
                </ul>
            </Fragment>
        )
    }
}

export default NavUser;