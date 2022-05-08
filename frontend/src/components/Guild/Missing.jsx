import React from "react";


class Missing extends React.Component {
    render() {
        return (
            <div className="not-found">
                <div className="container">
                    <div className="text-center">
                        <i className="fa-solid fa-triangle-exclamation fa-7x error-2" aria-hidden="true"></i><br /><br />
                        <div className="error-1">
                            <div className="card error">
                                <div className="card-body">
                                    <h2 className="card-text text-1"><i className="fa-solid fa-triangle-exclamation"></i> الخادم المطلوب غير موجود</h2>
                                </div>
                            </div>
                        </div>
                        <br /><br /><br />
                    </div>
                </div>
            </div>
        )
    }
}


export default Missing;