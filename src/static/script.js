let timeout;
document.getElementById("city").addEventListener("input", function () {
    clearTimeout(timeout);
    const query = this.value;
    timeout = setTimeout(() => {
        (async () => {
            if (query.length < 2) return;
            try {
                const res = await fetch(`/api/suggest?q=${encodeURIComponent(query)}`);
                const suggestions = await res.json();
                const datalist = document.getElementById("suggestions");
                datalist.innerHTML = "";
                suggestions.forEach(city => {
                    const option = document.createElement("option");
                    option.value = city;
                    datalist.appendChild(option);
                });
            } catch (err) {
                console.error("Autocomplete error:", err);
            }
        })();
    }, 300);
});

async function fetchWeather() {
    const city = document.getElementById("city").value;
    try {
        const res = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
        const data = await res.json();
        const out = document.getElementById("output");
        if (data.error) {
            out.textContent = data.error;
        } else {
            out.textContent = `Weather in ${data.city}: ${data.temperature}${data.units}`;
        }
    } catch (err) {
        document.getElementById("output").textContent = "Failed to fetch weather.";
    }
}