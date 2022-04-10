import React from "react";

function Card() {
    return (
        <div class="col-sm" id="card-animation">
            <div class="card text-light mb-3 card-fdr">
            <div class="card-outline-fdr"></div>
            <div class="h1 mt-3"><br />
                <img class="image w-50" src id="avatar-4"></img>
            </div>
            <div class="card-body text-center">
                <h4 class="card-title about-fdr"><strong id="username-4"></strong></h4>
                <p class="card-text text-light counter"><i class="fa-solid fa-id-card-clip"></i> ID :<strong id="id-4"></strong></p>
            </div>
        </div>
    </div>
    )
}

export default Card;