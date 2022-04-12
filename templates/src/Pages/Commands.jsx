import React, { Fragment } from "react";
import { Command, CommandsGroub } from "../components/Command/Commands";


class Commands extends React.Component{
    render() {

        const commands = [
            {
                "title": "العامة",
                "childrens": [
                    {
                        "name": "ping",
                        "description": "سرعة اتصال البوت",
                    },
                    {
                        "name": "support",
                        "description": "طلب الدعم الفني",
                    },
                    {
                        "name": "info",
                        "description": "طلب معلومات الخادم",
                    },
                    {
                        "name": "azan",
                        "description": "معرفة وقت الأذان في المدينة الخاصه بك",
                    },
                    {
                        "name": "bot",
                        "description": "جلب معلومات البوت",
                    },
                    {
                        "name": "invite",
                        "description": "أضافة البوت إلى خادمك",
                    },
                    {
                        "name": "help",
                        "description": "أرسال رساله تعرض جميع الأوامر",
                    },
                ]
            },
            {
                "title": "القرآن الكريم",
                "childrens": [
                    {
                        "name": "quran play",
                        "description": "تشغيل القران الكريم",
                    },
                    {
                        "name": "quran radio",
                        "description": "تشغيل اذاعه القران الكريم",
                    },
                    {
                        "name": "quran stop",
                        "description": "إيقاف تشغيل القران الكريم",
                    },
                    {
                        "name": "quran volume",
                        "description": "تغير مستوى الصوت للقرآن الكريم",
                    },
                ]
            },
            {
                "title": "المصحف الشريف",
                "childrens": [
                    {
                        "name": "moshaf pages",
                        "description": "عرض صفحات القرآن الكريم",
                    },
                    {
                        "name": "moshaf page",
                        "description": "عرض صفحه محدده من القرآن الكريم",
                    },
                    {
                        "name": "moshaf surahs",
                        "description": "عرض جميع سور القرآن الكريم",
                    },
                ]
            },
            {
                "title": "الأداره",
                "childrens": [
                    {
                        "name": "set prefix",
                        "description": "تغير البادئة الخاصة بالخادم",
                    },
                    {
                        "name": "set spam",
                        "description": "خاصية تمنع تكرر ارسال الاذكار في حالة عدم تفاعل الشات",
                    },
                    {
                        "name": "set embed",
                        "description": "تغير خاصيه ارسال الاذكار الى امبد",
                    },
                    {
                        "name": "set time",
                        "description": "تغير وقت ارسال الأذكار",
                    },
                    {
                        "name": "set room",
                        "description": "أختيار قناة الأذكار",
                    },
                    {
                        "name": "set role",
                        "description": "تقيد صلاحيات التحكم بالقرآن الكريم",
                    },
                ]
            }
        ]

        return (
            <Fragment>
                <section class="py-5 text-center" dir="ltr">
                    <div class="container">
                        <div class="card">
                            {commands.map((cmds) => {
                                return (
                                    <CommandsGroub 
                                    title={cmds.title} 
                                    description={cmds.description} 
                                    childrens={cmds.childrens.map((cmd) => {
                                        return <Command name={cmd.name} description={cmd.description} />
                                    })} 
                                />)
                            })}
                        </div>
                    </div>
                </section>
            </Fragment>
        )
    }
}

export default Commands;