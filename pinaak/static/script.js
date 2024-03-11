function join_mid() {
    document.getElementById('join-mid').style.visibility = "visible";
    document.getElementById('btn-2').remove();
}

function join_budget() {
    document.getElementById('join-budget').style.visibility = "visible";
    document.getElementById('btn-1').remove();
}

function done2() {
    setTimeout(() => {
        document.getElementById('join-mid').remove();
    }, 100);
    document.getElementById('done2').style.visibility = "visible";
}

function done1() {
    setTimeout(() => {
        document.getElementById('join-budget').remove();
    }, 100);
    document.getElementById('done1').style.visibility = "visible";
}