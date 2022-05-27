import axios from "axios";
import React, { Fragment, useContext, useState } from "react";
import FontAwesome from "react-fontawesome";
import { Navigate } from "react-router-dom";
import Info from "../../components/Guild/Info";
import Missing from "../../components/Guild/Missing";
import Warning from "../../components/Warning/Warning";
import { api_url } from "../../Config";
import { AppContext } from "../../Context";


function Admin() {
    const context = useContext(AppContext);
    if (!context.is_login) {
        return <Navigate to="/login" replace={true} />
    }
    if (!context.user.admin) {
        return <Warning text="ليس لديك صلاحيات للدخول هنا" />
    }
    
    const [element, setElement] = useState();
    const search_handler = () => {
        var guild_id = document.getElementsByClassName("guild-id-input")[0].value;
        axios.get(api_url + `/guilds/${guild_id}/info`).then((res) => {
            setElement(<Info guild={res.data} />);
        }).catch((err) => {
            setElement(<Missing/>);
        })
    }
    return (
        <Fragment>
            <div className="container py-5"></div>
            <section className="py-5 text-center">
                <div className="container">
                    <div className="card">
                        <div className="card-header" style={{borderRadius: "7px 7px 0px 0px", backgroundColor: "var(--color3)", color: "var(--color1)"}}>
                            <h1>إستعلام عن الخادم</h1>
                        </div>
                        <div className="card-body" style={{ backgroundColor: "var(--dark-section-bg-1)", Color: "var(--color1)" }}>
                            <div className="mb-3 row">
                                <label htmlFor="id_input" className="col-sm-2 col-form-label" style={{ color: "var(--color1)" }} >ايدي الخادم</label>
                                <div className="col-sm-10">
                                    <input type="number" placeholder="الايدي من 18 رقم !" id="id_input" className="form-control bot_2 guild-id-input" maxLength="18" defaultValue="" onChange={() => {}} />
                                </div>
                                <br />
                            </div>
                            <div className="text-center">
                                <button onClick={() => search_handler()} className="bot_1 btn btn-danger btn-lg info-search"> <FontAwesome name="fa-solid fa-info" /> إستعلام عن الخادم</button>
                            </div>
                        </div>

                        {element}

                    </div>
                </div>
            </section>

            <div className="container py-5"></div>

        </Fragment>
    )
}

export default Admin;