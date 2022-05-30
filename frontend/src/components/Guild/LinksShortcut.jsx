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
                                    <img style={{ width: "200px", height: "200px", borderRadius: "50%", border: "1px solid" }} className="guild-icon" src="https://cdn.discordapp.com/icons/843865725886398554/f2c051341380c0c7aa0cda715be6568e.png?size=4096" />
                                </div>
                                <h1 className="card-title text-center"><strong className="strtt guild-name" id="username-1">Ottawa 4 programming</strong></h1>
                                
                                <div className="card-body text-start form-floating" id="floatingTextarea2" style={{ height: "auto", backgroundColor: "#10131e", border: "1px solid #437baf" }}>
                                    <label for="floatingTextarea2" style={{ color: "var(--false)" }}>SERVER INFO</label><br />
                                    <p className="text-start">ID: <b className="strtt guild-id">843865725886398554</b></p>
                                    <p className="text-start">Name: <b className="strtt guild-name">Ottawa 4 programming</b></p>
                                    <p className="text-start">Owner: <b className="strtt owner-id">750376850768789500</b></p>
                                    <p className="text-start">Channels: <b className="strtt channels">84</b></p>
                                    <p className="text-start">Emojis: <b className="strtt emojis">160</b></p>
                                    <p className="text-start">Members: <b className="strtt members">1623</b></p>
                                    <p className="text-start">Channel: <b className="strtt channel">860816245460435000</b></p>
                                    <p className="text-start">Embed: <b className="strtt embed">false</b></p>
                                    <p className="text-start">AntiSpam: <b className="strtt anti-spam">false</b></p>
                                    <p className="text-start">QuranRole: <b className="strtt role-id">843871678768742400</b></p>
                                    <p className="text-start">Time: <b className="strtt time">7200</b></p>
                                </div>
                            </div>
                            <div className="card-footer">
                                <a href="/dashboard/843865725886398554" className="dashboard-link"><button className="btn primary btn-lg me-2 mx-2">تعديل البوت كمساول</button></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}


export default Info;