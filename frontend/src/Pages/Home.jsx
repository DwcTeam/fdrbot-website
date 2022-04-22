import React, { Fragment } from "react";
import Card from "../components/Card/Card";
import logo from "../static/images/logo.png";
import easy_to_use from "../static/images/easy_to_use.png";
import easy_to_use_2 from "../static/images/easy_to_use_2.png";
import { Link } from 'react-router-dom';
import FontAwesome from "react-fontawesome";
import CardImage from "../components/CardImage/CardImage";


class Home extends React.Component {
    render() {
        return (
            <Fragment>
                                
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
                                <Link to="/dashboard"><button className="btn button-login btn-lg me-2 mx-2">لوحة التحكم</button></Link>
                                {/*<Link to="/login"><button className="btn button-login btn-lg me-2 mx-2">تسجيل الدخول</button></Link>*/}
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
                <section className="py-5">
                <div className="container">
                    <div className="text-center">
                    <h2 id="saqr-6" className="text-center h1 text-white title">ما نقدم ؟</h2>
                    <br />
                    <br />
                    
                    <div className="row text-center row-cols-1 row-cols-md-3 g-3">
                        <Card icon={<FontAwesome name="fas fa-quran" />} title={"القرآن الكريم"}/>
                        <Card icon={<FontAwesome name="fa-solid fa-mosque" />} title={"الأذكار"}/>
                        <Card icon={<FontAwesome name="fa-solid fa-star-and-crescent" />} title={"السنه النبوية"}/>
                    </div>
                    </div>
                </div>
                </section>
                {/* end section for services */}
                
                {/* section for introduction */}
                
                <section className="py-5">
                    <CardImage image={easy_to_use} title="لوحة تحكم سهلة الاستخدام" description="تمتع بتجربة فريدة, ومميزة وتحكم كامل بسيرفرك" dir="rtl" />
                    <CardImage image={easy_to_use_2} title="مناسب لجميع الفئات" description="مناسب لسيرفرات المتاجر, البوتات, الالعاب, وسيرفرات المسابقات وسيرفرات الاجتماعية" dir="ltr" />
                </section>
                
                {/* end section for introduction */}

                {/* section for about */}
                <section className="py-5">
                <div className="container">
                    <div className="text-center">
                    <h2 id="saqr-6" className="text-center h1 text-white title">الإحصائيات #</h2>
                    <br />
                    <br />
                    <div className="row text-center row-cols-1 row-cols-md-4 g-3">
                        <Card icon={<FontAwesome name="fa-solid fa-terminal" />} title={"عدد الأوامر"} text="32"/>
                        <Card icon={<FontAwesome name="fas fa-hashtag" />} title={"عدد الشاتات"} text={ "" + this.props.channels } />
                        <Card icon={<FontAwesome name="fas fa-server" />} title={"عدد الخوادم"} text={ "" + this.props.guilds }/>
                        <Card icon={<FontAwesome name="fas fa-share" />} title={"عدد الشاردات"} text={ "" + this.props.shards }/>
                    </div>
                    </div>
                </div>
                </section>
                {/* end section for about */}

            </Fragment>
        )
    };
}


export default Home;