import React, { Fragment } from "react";
import { Link } from "react-router-dom";
import Warning from "../Warning/Warning";

function Issus() {
    return <Warning text={ 
        <Fragment>
            الخدمة حالياً غير متاحة بالوقت الحالي
            <br />
            إذا أستمرة المشكلة يمكنك التواصل مع <Link to="/support">الدعم الفني</Link>
        </Fragment> } 
    />
}

export default Issus;