import React from "react";
import PropTypes from 'prop-types';
import Loading from "../Loading/Loading";
import FontAwesome from "react-fontawesome";


class Info extends React.Component {
    static propTypes = {
        guild: PropTypes.object.isRequired,
    }
    render() {
        const guild = this.props.guild;
        if (!guild) {
            return <Loading />
        }
        return (
            <div className="card-body guild-info" style={{ backgroundColor: "var(--dark-section-bg-1)", color: "var(--color1)" }}>
                <div className="row text-center row-cols-1 row-cols-md-1 g-3">

                    <div className="col-sm d-flex justify-content-center align-items-center">
                        <div className="card text-light mb-3 card-fdr" style={{ width: "80%" }}>
                            <div className="card-outline-fdr"></div>
                            <div className="d-flex text-start p-3 text-light">
                                <FontAwesome name="fa-solid fa-server" className="h1 verify" />
                            </div>
                            <div className="card-body">
                                <div className="text-center">
                                    <img style={{ width: "200px", height: "200px", borderRadius: "50%", border: "1px solid" }} className="guild-icon" src={guild.icon} alt={guild.name} />
                                </div>
                                <h1 className="card-title text-center"><strong className="strtt guild-name" id="username-1">{guild.name}</strong></h1>
                                
                                <div className="card-body text-start form-floating" id="floatingTextarea2" style={{ height: "auto", backgroundColor: "#10131e", border: "1px solid #437baf" }}>
                                    <label for="floatingTextarea2" style={{ color: "var(--false)" }}>SERVER INFO</label><br />
                                    <p className="text-start">ID: <b className="strtt guild-id">{guild.name}</b></p>
                                    <p className="text-start">Name: <b className="strtt guild-name">{guild.name}</b></p>
                                    <p className="text-start">Owner: <b className="strtt owner-id">{guild.owner_id}</b></p>
                                    <p className="text-start">Channels: <b className="strtt channels">{guild.channels}</b></p>
                                    <p className="text-start">Emojis: <b className="strtt emojis">{guild.emojis}</b></p>
                                    <p className="text-start">Members: <b className="strtt members">{guild.member_count}</b></p>
                                    <p className="text-start">Channel: <b className="strtt channel">{guild.channel}</b></p>
                                    <p className="text-start">Embed: <b className="strtt embed">{guild.embed ? "yes" : "no"}</b></p>
                                    <p className="text-start">AntiSpam: <b className="strtt anti-spam">{guild.anti_spam ? "yes" : "no"}</b></p>
                                    <p className="text-start">QuranRole: <b className="strtt role-id">{guild.role_id}</b></p>
                                    <p className="text-start">Time: <b className="strtt time">{guild.time}</b></p>
                                </div>
                            </div>
                            <div className="card-footer">
                                <a href={"/dashboard/" + guild.id} className="dashboard-link"><button className="btn primary btn-lg me-2 mx-2">تعديل البوت كمساول</button></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


export default Info;