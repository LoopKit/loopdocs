// pretty rudimentary but it works (tested for Chrome and Safari)
// each id must be unique (I'm sure there's a way to fix this . . . later)
// example is found on build/step14.md using: <code id="copy-step14-01">

function copyEvent(id)
{
    var str = document.getElementById(id);
    window.getSelection().selectAllChildren(str);
    document.execCommand("Copy")
}
