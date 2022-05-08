import React from "react";


class Suggestions extends React.Component {
    render() {
        return (
            <section className="py-5" dir="ltr">
                <div className="container">
                    <div className="text-center">
                        <br /><br />

                        <div className="col-sm">
                            <div className="card text-light mb-3 card-3 bg-fdr-col card-image">
                                <div className="card-header">
                                    <h1 className="h1 text-center title"> ارسال اقتراحك <i className="fa-solid fa-comment-dots"></i></h1>
                                </div>
                                <hr />
                                <div className="card-body" dir="rtl" id="card-animation">
                                    <input type="text" placeholder="اكتب اقتراحك الحد 190 !"
                                        className="form-control bot_2 guild-id-input" id="botId" maxlength="190" value="" required={true} />
                                </div>
                                <div className="text-center">
                                    <button className="btn primary btn-lg" data-bs-toggle="modal" data-bs-target="#staticBackdrop"> 
                                        <svg className="svg-inline--fa fa-info" aria-hidden="true" focusable="false" data-prefix="fas"
                                            data-icon="info" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 512"
                                            data-fa-i2svg="">
                                            <path fill="currentColor"
                                                    d="M160 448h-32V224c0-17.69-14.33-32-32-32L32 192c-17.67 0-32 14.31-32 32s14.33 31.1 32 31.1h32v192H32c-17.67 0-32 14.31-32 32s14.33 32 32 32h128c17.67 0 32-14.31 32-32S177.7 448 160 448zM96 128c26.51 0 48-21.49 48-48S122.5 32.01 96 32.01s-48 21.49-48 48S69.49 128 96 128z">
                                            </path>
                                        </svg> أرسل اقتراحك
                                    </button>
                                </div>
                                <hr />
                                <div className="card-footer">
                                    <p className="card-title img-fluid mb-3 aik-saqr-1 h4 text-start card-avatar"><img
                                            src="https://cdn.discordapp.com/avatars/716783245387235410/4e1581b67a4e10269da668db41716590.png?size=1024"
                                            width="80" height="80" className="image card-avatar-1" /> <b>S A Q R#1200</b>
                                    </p>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        )
    }
}


export default Suggestions;