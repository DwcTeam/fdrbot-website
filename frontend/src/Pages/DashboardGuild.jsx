import React, { Fragment } from "react";

class DashboardGuild extends React.Component {
  render() {
    return (
      <Fragment>
        <div className="all text first div">

          <section className="py-5 text-white text first div">
            <div className="container">

              <div className="row row-cols-1 row-cols-md-3 g-1">

                {/* <!-- Setup channel --> */}
                <div className="col update">
                  <div className="card bg-dark m-1">
                    <div className="card-body">
                      <h1 className="set text-light text-center">تحديد روم للاذكار</h1>
                    </div>
                    <div className="card-footer">
                      <select className="form-select form-select-sm channel_id" aria-label=".form-select-sm example">
                        <option selected value="0" >اختر ..</option>
                        <option value="{{ channel.id }}" className="text-start" selected>uiutiytiyiyutiytui
                        </option>
                        <option value="{{ channel.id }}" className="text-start">uiutiytiyiyutiytui</option>
                      </select>
                    </div>
                  </div>
                </div>

                {/* <!-- Setup qurau role channel --> */}
                <div className="col update">
                  <div className="card bg-dark m-1 mb-3">
                    <div className="card-body">
                      <h1 className="set text-light text-center">تحديد رتبه للقران الكربم</h1>
                    </div>
                    <div className="card-body">
                      <select className="form-select form-select-sm role_id" aria-label=".form-select-sm example">
                        <option selected value="0">اختر ..</option>
                        <option value="{{ role.id }}" className="text-start" selected>153445645</option>
  
                        <option value="{{ role.id }}" className="text-start">153445645</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div className="col update">
                  <div className="card bg-dark m-1 maintenance">
                    <div className="card-body">
                      <h1 className="set text-light text-center voice_channel">تحديد روم صوتي</h1>
                    </div>
                    <div className="card-footer">
                      <select className="form-select form-select-sm" aria-label=".form-select-sm example" disabled>
                        <option selected value="0">قريباً ..</option>
                        <option value="{{ channel.id }}" className="text-start" selected>uiutiytiyiyutiytui</option>
                        <option value="{{ channel.id }}" className="text-start">uiutiytiyiyutiytui</option>
                      </select>
                    </div>
                  </div>
                </div>

              </div>

              <div className="row row-cols-1 row-cols-md-3 g-3">

                <div className="col update">
                  <div className="card bg-dark m-1">
                    <div className="card-body">
                      <h1 className="set text-light text-center">تغير الوقت</h1>
                    </div>
                    <div className="card-footer">
                      <select className="form-select form-select-sm time" aria-label=".form-select-sm example">
                        <option value="1800" className="text-end" selected>
                          دقيقه 30</option>
                        <option value="3600" className="text-end" selected>ساعة
                        </option>
                        <option value="7200" className="text-end" selected>
                          ساعتين</option>
                        <option value="21600" className="text-end" selected>6
                          ساعات</option>
                        <option value="43200" className="text-end" selected>
                          ساعات 12</option>
                        <option value="86400" className="text-end" selected>
                          ساعات 24</option>
                      </select>
                    </div>
                  </div>
                </div>

                <div className="col update">
                  <div className="card bg-dark maintenance">
                    <div className="card-body">
                      <h1 className="set text-light text-center">علبة الوان</h1>
                    </div>
                    <div className="card-footer">
                      <input type="color" className="form-control form-control-color w-100" id="exampleColorInput"
                        value="#262727" title="Choose your color" disabled /><br />
                    </div>
                  </div>
                </div>

                <div className="col update">
                  <div className="card bg-dark m-1 maintenance ">
                    <div className="card-body">
                      <h1 className="set text-light text-center">تحديد روم الخاتمه</h1>
                    </div>
                    <div className="card-body">
                      <select className="form-select form-select-sm" aria-label=".form-select-sm example" disabled>
                        <option selected value="0">قريباً ..</option>
                        <option value="{{ channel.id }}" className="text-start" selected>uiutiytiyiyutiytui</option>
                        <option value="{{ channel.id }}" className="text-start">uiutiytiyiyutiytui</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>

              <br />
                <div className="row row-cols-1 row-cols-md-1 g-4">

                  <div className="col update" dir="ltr">
                    <div className="card bg-dark m-1">
                      <div className="card-body">
                        <h1 className="set text-light d-inline-flex float-end">تحديد نوع الارسال</h1>
                        <div className="form-check form-switch text-start h3 d-inline-flex rt">
                          <input className="form-check-input rt anti_spam" type="checkbox" role="switch"
                            id="flexSwitchCheckChecked" aria-checked={true} />
                        </div>
                        <p className="text-end h6 sfsf"><b className="sfsf-1">(ينصح لسيرفرات الكبيره)</b> يقلل في ارسال
                          الاذكار
                          اذا لم يكون
                          اشات المتفاعل</p>
                      </div>
                    </div>
                  </div>

                  <div className="col update" dir="ltr">
                    <div className="card bg-dark m-1">
                      <div className="card-body">
                        <h1 className="set text-light d-inline-flex float-end">تحديد نوع الامبد</h1>
                        <div className="form-check form-switch text-start h3 d-inline-flex rt">
                          <input className="form-check-input rt embed" type="checkbox" role="switch"
                            id="flexSwitchCheckChecked" aria-checked={true} />
                        </div>
                        <p className="text-end h6 sfsf">يضع الاذكار في سندوق مرتب</p>
                      </div>
                    </div>
                  </div>

                </div>
            </div>
          </section>
        </div>


        <div className="container">
          <div className="row row-cols-1 row-cols-md-1 g-3">
            <div className="position-fixed bottom-0 end-0" style={{zIndex: "11"}}>
              <div aria-live="polite" alive={true} className="d-flex justify-content-center align-items-center w-100">
                <div id="liveToast" className="toast" role="alert" aria-live="assertive" alive={true}>
                  <div className="col" dir="ltr">
                    <div className="card bg-dark m-2" style={{border: "1px solid var(--color1);"}}>
                      <div className="card-body">
                        <h1 className="set text-light d-inline-flex float-end ">احذر — لديك تغييرات لم يتم حفظها!</h1>
                        <div className="group-buttons float-start save-menu">
                          <button className="btn me-2 mx-2 save-button" id="liveToastBtn">حفظ التغييرات</button>
                          <button className="btn me-2 mx-2 cancel-button" id="liveToastBtn">إلغاء</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </Fragment>
    );
  }
}

export default DashboardGuild;