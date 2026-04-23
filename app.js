async function loadSentiment() {
    const res = await fetch("http://127.0.0.1:5000/api/sentiment");
    const data = await res.json();

    const container = document.getElementById("sentiment");

    data.forEach(item => {
        container.innerHTML += `
            <div class="card">
                <p>${item.text}</p>
                <strong>${item.sentiment}</strong>
            </div>
        `;
    });
}

loadSentiment();
