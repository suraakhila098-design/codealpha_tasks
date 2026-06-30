function send() {
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: document.getElementById("msg").value
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("reply").innerHTML = data.reply;
    });
}