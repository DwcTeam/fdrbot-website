import React from "react";
import "./Footer.moduel.css"

class Footer extends React.Component {
    render() {
        return (
            <footer className="py-5 bg-dark">
                <div class="col-sm">
                    <div class="card-footer">
                        <h1 class="card-title about-fdr text-center h5">جميع الحقوق محفوظة لـ فريق فاذكروني بوت للبرمجة</h1>
                    </div>
                </div>
            </footer>
        )};
}

export default Footer;