import axios from "axios";
import React, { Fragment, useContext, useEffect, useState } from "react";
import { Navigate, useParams } from "react-router-dom";
import CheckBox from "../../components/UpdateOption/CheckBox";
import ColorMenu from "../../components/UpdateOption/ColorMenu";
import SaveMenu from "../../components/UpdateOption/SaveMenu";
import SelectMenu from "../../components/UpdateOption/SelectMenu";
import Warning from "../../components/Warning/Warning";
import { AppContext } from "../../Context";


const DashboardGuild = () => {
  const context = useContext(AppContext);
  const guild_id = useParams().id;

  const [info, setInfo] = useState({});

  const [channels, setChannels] = useState([]);
  const [roles, setRoles] = useState([]);

  const [state, setState] = useState({});  // is the new data that will be display save menu

  const available_guilds = context.available_guilds;

  const available_times = [
    "دقيقه 30",
    "ساعة",
    "ساعتين",
    "6 ساعات",
    "12 ساعات",
    "24 ساعات",
  ]

  if (!context.is_login) {
    return <Navigate to="/login" replace={true} />
  }
  const guild = available_guilds.find((guild) => guild.id === guild_id);
  if (!guild) {
    return <Warning text="هاذا الخادم غير متاح للتعديل" />
  }

  useEffect(() => {
    axios.get(`/guilds/${guild_id}`).then((res) => {
      setChannels(res.data.guild.channels);
      setRoles(res.data.guild.roles);
      setInfo(res.data.info);
    }).catch((err) => {
      console.log(err);
    });
  }, []);

  if (!info || !channels || !roles) {
    return <div>loading...</div>
  }

  if (
    (state.channel && state.channel !== info.channel) || 
    // eslint-disable-next-line
    (state.role && state.role !== info.role) || 
    // eslint-disable-next-line
    (state.time && state.time !== info.time) && !state.show
  ) {
    useEffect(() => {
      setState({...state, show: true});
    }, []);
    console.log("work")
  } else {
    if (state.show) {
      useEffect(() => {
        setState({...state, show: false});
      }, []);
      console.log("not work")
    }
  }

  return (
    <Fragment>
      <div className="all text first div">
        <section className="py-5 text-white text first div">
          <div className="container">
            <div className="row row-cols-1 row-cols-md-3 g-1">
              <SelectMenu 
                title="تحديد روم للأذكار"  
                items={channels.filter(channel => channel.type === 0)} 
                defaultValue={info.channel ? info.channel : "0"} 
                prefix="#" 
                callback={(value) => {
                  setState({...state, channel: value});
                }}
              />
              <SelectMenu 
                title="تحديد رتبه للقران الكربم"  
                items={roles} 
                defaultValue={info.role_id ? info.role_id : "0"} 
                prefix="@" 
                callback={(value) => {
                  setState({...state, role_id: value});
                }}
                // ignoreValues={roles.find((role) => role.name === "@everyone").} 
              />
              <SelectMenu 
                title="تحديد روم صوتي" 
                items={[]} 
                defaultValue="0" 
                defaultOption="قريباً .." 
                isDisabled={true} 
                callback={(value) => {}}
              />
            </div>
            <div className="row row-cols-1 row-cols-md-3 g-3">
              <SelectMenu 
                title="تغير الوقت" 
                items={available_times}
                defaultValue={info.time} 
                callback={(value) => {
                  setState({...state, time: value});
                }}
                />
              <ColorMenu 
                title="علبة الوان" 
                defaultValue="#262727" 
                isDisabled={true} 
                callback={(value) => {}}
              />
              <SelectMenu 
                title="تحديد روم الخاتمه" 
                items={[]} 
                defaultValue="0" 
                defaultOption="قريباً .." 
                isDisabled={true} 
                callback={(value) => {}}
              />
            </div>
            <br />
            <div className="row row-cols-1 row-cols-md-1 g-4">
              <CheckBox 
                title="تحديد نوع الارسال" 
                checked={info.anti_spam} 
                description={ <Fragment><b className="sfsf-1">(ينصح لسيرفرات الكبيره)</b> يقلل في ارسال الاذكار اذا لم يكون اشات المتفاعل </Fragment>} 
                callback={(value) => {
                  setState({...state, anti_spam: value});
                }}
                />
              <CheckBox 
                title="تحديد نوع الامبد" 
                checked={info.embed} 
                description="يضع الاذكار في سندوق مرتب" 
                callback={(value) => {
                  setState({...state, embed: value});
                }}
              />
            </div>

            {<SaveMenu show={state.show} />}

          </div>
        </section>
      </div>
    </Fragment>
  );
}


export default DashboardGuild;