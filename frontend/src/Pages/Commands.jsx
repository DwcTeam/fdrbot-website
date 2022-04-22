import React, { Fragment } from "react";
import { Command, CommandsGroub } from "../components/Command/Commands";
import commands from "../data/commands.json";

class Commands extends React.Component{
    render() {
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