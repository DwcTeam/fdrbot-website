import React, { Fragment } from "react";
import Guild from "../components/Guild/Guild";
import Nav from "../components/Nav/Nav";
import Footer from "../components/Footer/Footer";

class Dashboard extends React.Component {
    render() {
        var guilds = [
            {
                name: "بوت فاذكروني",
                banner: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                avatar: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                id: "729526735749513267",
            },
            {
                name: "بوت ذكر",
                banner: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                avatar: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                id: "729526735749513267",
            },
        ]
        var Unguilds = [
            {
                name: "بوت فاذكروني",
                banner: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                avatar: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                id: "729526735749513267",
            },
            {
                name: "بوت ذكر",
                banner: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                avatar: "https://cdn.discordapp.com/icons/729526735749513267/222785a5ff8429dbfee4b6a56fd88d8a.png",
                id: "729526735749513267",
            },
        ]
        return (
            <Fragment>
                <Nav />
                <br />
                <br />

                <section class="py-5">
                    <div class="container">
                        <div class="d-flex align-items-center justify-content-center flex-row-reverse" dir="rtl">
                            <h1 class="text-white text-center title">يا هلا والله فيك, H A Z E M</h1>
                        </div>
                        <div class="row text-center row-cols-1 row-cols-md-3 g-3">
                        {guilds.map((item, index) => {
                            return <Guild name={item.name} banner={item.banner} avatar={item.avatar} id={item.id} alive={true} />
                        })}
                        </div>
                    </div>
                </section>

                <section class="py-5">
                    <div class="container">
                        <div class="d-flex align-items-center justify-content-center flex-row-reverse" dir="rtl">
                            <h1 class="text-white text-center title">الخوادم غير المتاحة</h1>
                        </div>
                        <div class="row text-center row-cols-1 row-cols-md-3 g-3">
                        {Unguilds.map((item, index) => {
                            return <Guild name={item.name} banner={item.banner} avatar={item.avatar} id={item.id} alive={false}/>
                        })}   
                        </div>
                    </div>
                </section>

                <Footer />
            </Fragment>
        );
    }
}

export default Dashboard;
