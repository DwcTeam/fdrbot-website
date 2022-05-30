import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { client_id } from "../../Config";
import "./Guild.css"

function Guild ({ name, banner, avatar, id, alive }) {
    const [button, setButton] = useState();
    useEffect(() => {
        if (alive) {
            setButton(        
                <Link to={ "/dashboard/"+id }>
                    <button className="btn primary card-title float-start pe-3 px-3 pt-2 pb-2 saqr-but" >تحكم</button>
                </Link>
            );
        } else {
            setButton(
                <a href={`https://discordapp.com/oauth2/authorize?client_id=${client_id}&scope=bot&permissions=8&guild_id=${id}`}>
                    <button className="btn primary card-title float-start pe-3 px-3 pt-2 pb-2 button-fdr">أضافة البوت</button>
                </a>
            );
        }
    }, [alive]);
    return (
        <div className="col  text-center">
        <div className="card h-75 card-1">
        <div className="card-body">
            <div className="sc-1vemdld-4 banner" style={{ background: `url('${banner}') center center / cover no-repeat`, backgroundSize: "100%" }}></div>
            <img src={ avatar }
            className="avatar-server justify-content-center align-items-center w-50 avalidated"
            alt={ name } />
        </div>
        </div>
        <div className="pt-2">
        <small className="text-muted float-end">{ name }</small>
        {button}
        </div>
    </div>
    )
}

export default Guild;