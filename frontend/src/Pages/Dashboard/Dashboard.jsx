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

  const [isChange, setChange] = useState(false);

  const available_guilds = context.available_guilds;

  const available_times = [
    { id: "1800", name: "دقيقه 30"},
    { id: "3600", name: "ساعه"},
    { id: "7200", name: "ساعتين"},
    { id: "21600", name: "ساعات 6"},
    { id: "43200", name: "ساعه 12"},
    { id: "86400", name: "ساعه 24"},
  ]

  if (!context.is_login) {
    return <Navigate to="/login" replace={true} />
  }
  const guild = available_guilds.find((guild) => guild.id === guild_id);
  if (!guild) {
    return <Warning text="هذا الخادم غير متاح للتعديل" />
  }

  useEffect(() => {
    axios.get(`/guilds/${guild_id}`).then((res) => {
      setChannels(res.data.channels);
      setRoles(res.data.roles);
      var info = {
        id: res.data.id,
        channel_id: res.data.channel_id,
        role_id: res.data.role_id,
        time: res.data.time,
        embed: res.data.embed,
      }
      setInfo(info);
      setState(info);
    }).catch((err) => {
      console.log(err);
    });
  }, []);

  if (!info || !channels || !roles || !state) {
    return <div>loading...</div>
  }

  useEffect(() => {
    if (
      (state.channel_id && state.channel_id !== info.channel_id) || 
      // eslint-disable-next-line
      (state.role_id && state.role_id !== info.role_id) || 
      // eslint-disable-next-line
      (state.time && state.time !== info.time) ||
      // eslint-disable-next-line
      (state.embed !== info.embed)
    ) {
      if (!isChange) {
        setChange(true);
      }
    } else {
      if (isChange) {
        setChange(false);
      }
    }
  }, [state, info, isChange]);
  return (
    <Fragment>
      <div className="all text first div">
        <section className="py-5 text-white text first div">
          <div className="container">
            <div className="row row-cols-1 row-cols-md-3 g-1">
              <SelectMenu 
                title="تحديد روم للأذكار"  
                items={channels.filter(channel => channel.type === 0)} 
                defaultValue={info.channel_id ? info.channel_id : "0"} 
                prefix="#" 
                callback={(e) => {
                  setState({...state, channel_id: e.target.value});
                }}
              />
              <SelectMenu 
                title="تحديد رتبه للقران الكربم"  
                items={roles} 
                defaultValue={info.role_id ? info.role_id : "0"} 
                prefix="@" 
                callback={(e) => {
                  setState({...state, role_id: e.target.value});
                }}
              />
              <SelectMenu 
                title="تحديد روم صوتي" 
                items={[]} 
                defaultValue="0" 
                defaultOption="قريباً .." 
                isDisabled={true} 
                callback={(e) => {}}
              />
            </div>
            <div className="row row-cols-1 row-cols-md-3 g-3">
              <SelectMenu 
                title="تغير الوقت" 
                items={available_times}
                defaultValue={info.time} 
                callback={(e) => {
                  setState({...state, time: e.target.value});
                }}
                isDisabledDefault={true}
                />
              <ColorMenu 
                title="علبة الوان" 
                defaultValue="#262727" 
                isDisabled={true} 
                callback={(e) => {}}
              />
              <SelectMenu 
                title="تحديد روم الختمة" 
                items={[]} 
                defaultValue="0" 
                defaultOption="قريباً .." 
                isDisabled={true} 
                callback={(e) => {}}
              />
            </div>
            <br />
            <div className="row row-cols-1 row-cols-md-1 g-4">
              <CheckBox 
                title="تحديد نوع الامبد" 
                checked={info.embed} 
                description="يضع الاذكار في سندوق مرتب" 
                callback={(checked) => {
                  setState({...state, embed: checked});
                }}
              />
            </div>
          </div>
        </section>
      </div>
      <SaveMenu 
        show={isChange} 
        saveCallback={() => {
          axios.post(`/guilds/${guild_id}/update`, state).then((res) => {
            setInfo(state);
          }).catch((err) => {
            console.log(err);
          })
        }}
        cancelCallback={() => {
          window.location.reload()
        }} 
      />
    </Fragment>
  );
}


export default DashboardGuild;