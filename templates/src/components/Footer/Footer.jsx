import React from "react";
import "../../static/css/App.css";
import "./Footer.moduel.css"

class Footer extends React.Component {
    render() {
        return (
            <footer className="py-5 bg-dark col-sm card-footer ">
                <h1 className="card-title about-fdr text-center h5">جميع الحقوق محفوظة لـ فريق فاذكروني بوت للبرمجة</h1>
            </footer>
        )};
}

export default Footer;