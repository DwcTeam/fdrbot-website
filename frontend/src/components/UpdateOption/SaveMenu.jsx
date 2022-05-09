import React from "react";
import PropTypes from 'prop-types';

class SaveMenu extends React.Component {
    static propTypes = {
        show: PropTypes.bool.isRequired,
        cancelCallback: PropTypes.func.isRequired,
        saveCallback: PropTypes.func.isRequired,
    }
    render() {
        console.log(this.props.show)
        if (!this.props.show) {
            return null;
        }
        return (
            <div className="container" style={{ zIndex: "11" }}>
                <div className="row row-cols-1 row-cols-md-1 g-3">
                    <div className="position-fixed bottom-0 end-0" >
                        <div aria-live="polite" className="d-flex justify-content-center align-items-center w-100">
                            <div id="liveToast" className="toast show" role="alert" aria-live="assertive">
                                <div className="col" dir="ltr">
                                    <div className="card bg-dark m-2" style={{border: "1px solid var(--color1)"}}>
                                        <div className="card-body">
                                            <h1 className="set text-light d-inline-flex float-end ">احذر — لديك تغييرات لم يتم حفظها!</h1>
                                            <div className="group-buttons float-start save-menu">
                                                <button className="btn me-2 mx-2 save-button" onClick={this.props.saveCallback} >حفظ التغييرات</button>
                                                <button className="btn me-2 mx-2 cancel-button" onClick={this.props.cancelCallback}>إلغاء</button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default SaveMenu;
