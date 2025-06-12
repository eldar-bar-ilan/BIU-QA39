// Model function - application logic
function random1To6() {
    let r = Math.random() * 6 + 1;
    r = Math.floor(r);
    return r;
}

// View Function - UI
function ThrowDiceEvent() {
    let sp = document.getElementById("sp");
    sp.innerHTML = random1To6();
}

// register button to click event
const bt = document.getElementById("bt");
bt.addEventListener("click", ThrowDiceEvent);