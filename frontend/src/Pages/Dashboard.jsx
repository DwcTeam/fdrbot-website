import React, { Fragment } from "react";
import { Navigate } from "react-router-dom";
import Guild from "../components/Guild/Guild";
import { default_banner } from "../Config";
import { AppContext } from "../Context";


class Dashboard extends React.Component {
    static contextType = AppContext;
    render() {

        if (!this.context.is_login) {
            return <Navigate to="/login" replace={true} />
        } 

        const available_guilds = this.context.available_guilds;
        const unavailable_guilds = this.context.unavailable_guilds;
        const user = this.context.user
        return (
            <Fragment>
                <br />
                <br />
                <section className="py-5">
                    <div className="container">
                        <div className="d-flex align-items-center justify-content-center flex-row-reverse" dir="rtl">
                            <h1 className="text-white text-center title">يا هلا والله فيك, { user.username }</h1>
                        </div>
                        <div className="row text-center row-cols-1 row-cols-md-3 g-3">
                        {available_guilds.map((guild) => {
                            return <Guild name={guild.name} banner={guild.is_icon ? guild.icon : default_banner } avatar={guild.icon} id={guild.id} alive={true} />
                        })}
                        </div>
                    </div>
                </section>

                <section className="py-5">
                    <div className="container">
                        <div className="d-flex align-items-center justify-content-center flex-row-reverse" dir="rtl">
                            <h1 className="text-white text-center title">الخوادم غير المتاحة</h1>
                        </div>
                        <div className="row text-center row-cols-1 row-cols-md-3 g-3">
                        {unavailable_guilds.map((guild) => {
                            return <Guild name={guild.name} banner={guild.is_icon ? guild.icon : default_banner } avatar={guild.icon} id={guild.id} alive={false}/>
                        })}   
                        </div>
                    </div>
                </section>
            </Fragment>
        );
    }
}

export default Dashboard;
