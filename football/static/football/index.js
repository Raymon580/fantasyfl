$(document).ready(() => {
    $('button').click(() => {
        getScores()
    })

    $("a.nav-link").click((e) => { 
        switchTabs(e);
    });
});

function getScores() {
    const url = "/teams"
    $.get(url,
        (data, textStatus) => {
            console.log(data, textStatus)
        }
    );
}

function authUser() {
    /*const details = {
        'password': '8LQCFwi$VXb%7.k',
        'login': 'adeyusuf580@gmail.com',
        'redirect_uri': "https://fantasy.premierleague.com/a/login",
        'app': 'plfpl-web'
    }
    const url = "https://users.premierleague.com/accounts/login/"
    $.post(url, details, (data, textStatus) => {
            console.log(data, textStatus)
        },
    );
    $.ajax({
        headers: {'accept': 'application/json'},
        method: 'POST',
        url: url,
        data: details,
        dataType: "json",
        error: function() {
            console.log("error!")
        },
        success: function(data, textStatus) {
            console.log(data, textStatus);
        },
        complete: function() {
            console.log("Done!")
        }
    });*/
}

function switchTabs(event) {
    if (event.target.className === "nav-link active") {
        return;
    } else {
        $(".nav-link.active").toggleClass("active");
        event.target.className = "nav-link active";
    }
}