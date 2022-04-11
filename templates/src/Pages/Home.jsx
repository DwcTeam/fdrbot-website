import React, { Fragment } from "react";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";
import Card from "../components/Card/Card";
import logo from "../static/images/logo.png";
import { Link } from 'react-router-dom';
import FontAwesome from "react-fontawesome";


class Home extends React.Component {
    render() {
        return (
            <Fragment>
                <Nav />
                
                {/* section for login */}
                <section className="bg-fdr">
                    <div className="container">
                        <div className="text-center">
                            <img id="img1" className="img-respnsive img-fluid mx-auto d-block avatar-image lds-circle" src={logo} alt="logo">
                            </img>
                            <br />
                            <h1 className="title">فاذكروني</h1>
                            <hr style={{ border: "1px solid",  height: "1px"}}/>
                            <h5 className="text">بوت فاذكروني اول بوت عربي اسلامي للأذكار | بوت فاذكروني للتذكير بذكر الله في الشات</h5>
                            <br />
                            <div className="group-buttons">
                                {/*<Link to="/dashboard"><button className="btn button-fdr btn-lg me-2 mx-2">لوحة التحكم</button></Link>*/}
                                <Link to="/login"><button className="btn button-fdr btn-lg me-2 mx-2">تسجيل الدخول</button></Link>
                                <Link to="/invite"><button className="btn primary btn-lg me-2 mx-2">أضف البوت</button></Link>
                            </div>
                            <br />
                        </div>
                    </div>
                </section>
                <br></br>
                {/* end section for login */}

                {/* section for services */}
                <section id="Services"></section>
                <section class="py-5">
                <div class="container">
                    <div class="text-center">
                    <h2 id="saqr-6" class="text-center h1 text-white title">ما نقدم ؟</h2>
                    <br />
                    <br />
                    
                    <div class="row text-center row-cols-1 row-cols-md-3 g-3">
                        <Card icon={<FontAwesome name="fas fa-quran" />} title={"القرآن الكريم"}/>
                        <Card icon={<FontAwesome name="fa-solid fa-mosque" />} title={"الأذكار"}/>
                        <Card icon={<FontAwesome name="fa-solid fa-star-and-crescent" />} title={"السنه النبوية"}/>
                    </div>
                    </div>
                </div>
                </section>
                {/* end section for services */}
                
                {/* section for about */}
                <section class="py-5">
                <div class="container">
                    <div class="text-center">
                    <h2 id="saqr-6" class="text-center h1 text-white title">الإحصائيات #</h2>
                    <br />
                    <br />
                    <div class="row text-center row-cols-1 row-cols-md-4 g-3">
                        <Card icon={<FontAwesome name="fa-solid fa-terminal" />} title={"عدد الأوامر"} text="1212"/>
                        <Card icon={<FontAwesome name="fas fa-hashtag" />} title={"عدد الشاتات"} text="212"/>
                        <Card icon={<FontAwesome name="fas fa-server" />} title={"عدد الخوادم"} text="327"/>
                        <Card icon={<FontAwesome name="fas fa-share" />} title={"عدد الشاردات"} text="21"/>
                    </div>
                    </div>
                </div>
                </section>
                {/* end section for about */}

                <Footer />
            </Fragment>
        )
    };
}


export default Home;