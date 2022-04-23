import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import { ContextUser } from "../../Context";

// function NavUser(){
//     const [user, setUser] = useContext(ContextUser);
//     console.log(user);
//     return <Fragment></Fragment>
// }

class NavUser extends React.Component {
    static contextType = ContextUser;
    render(){
        const user = this.context;
        return (
            <Fragment>
            <ul class="navbar-nav ml-auto text-center" dir="ltr">
                    <div class="btn-group d-block me-lg-1 mx-lg-1" role="group">
                        <button id="users" type="button" class="btn primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            <img src={ user.avatar } width="28" height="28" class="image" alt={ user.username } /> <b>{ user.username }</b>
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
                                user.admin && (
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