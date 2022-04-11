import React, { Fragment } from "react";
import { Command, CommandsGroub } from "../components/Command/Commands";
import Footer from "../components/Footer/Footer";
import Nav from "../components/Nav/Nav";
import Warning from "../components/Warning/Warning";

class Commands extends React.Component{
    render() {

        const commands = [
            {
                "title": "الأداره",
                "description": "تحكم في الأداره",
                "childrens": [
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                ]
            },
            {
                "title": "العامه",
                "description": "تحكم في الأداره",
                "childrens": [
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                    {
                        "name": "تحديث البرنامج",
                        "description": "تحديث البرنامج",
                        "icon": "🔄",
                        "link": "/update"
                    },
                ]
            },
        ]

        var commandsO = commands.map((cmds) => {
            return (
                <CommandsGroub title={cmds.title} description={cmds.description}>
                    {cmds.childrens.map((cmd) => {
                        return <Command name={cmd.name} description={cmd.description} />
                    })}
                </CommandsGroub>
            )
        })
        return (
            <Fragment>
                <Nav />
                <section class="py-5 text-center" dir="ltr">
                    <div class="container">
                        <div class="card">
                            {commandsO}
                        </div>
                    </div>
                </section>
                <Footer />
            </Fragment>
        )
    }
}

export default Commands;