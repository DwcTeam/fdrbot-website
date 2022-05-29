import React, { Fragment, useEffect, useState } from "react";


function CheckBox({ title, name, checked, callback, description }) {
    const [isChecked, setIsChecked] = useState();
    useEffect(() => {
        setIsChecked(checked);
    }, [checked]);
    return ( 
        <Fragment>
            <div className="col" dir="ltr">
                <div className="card bg-dark m-1">
                    <div className="card-body">
                        <h1 className="set text-light d-inline-flex float-end">{title}</h1>
                        <div className="form-check form-switch text-start h3 d-inline-flex rt">
                            <input 
                                className="form-check-input rt" 
                                type="checkbox" 
                                role="switch" 
                                checked={isChecked}
                                onChange={(e) => {
                                    setIsChecked(!isChecked);
                                    callback(!isChecked);
                                }} 
                                aria-checked={checked}
                            />
                        </div>
                            <p className="text-end h6 sfsf">{description}</p>
                    </div>
                </div>
            </div>
        </Fragment>   
    )
}

export default CheckBox;