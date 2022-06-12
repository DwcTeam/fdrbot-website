import React, { Fragment } from "react";
import "./Tasbih.css"


class Redirect extends React.Component {
    render() {
        return (
            <Fragment>
                <section className="bg-fdr">
                    <div className="container">
                        <div className="text-center">
                            <div className="card-body">
                                <div className="card-text py-5" disabled>
                                    <button class="btn button-loading card-title text-light login" type="button" disabled>
                                        جار التحميل...
                                        <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </Fragment>
        )
    }
}

export default Redirect;