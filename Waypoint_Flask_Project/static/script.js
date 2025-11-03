const startInput = document.getElementById("startInput");
const endInput = document.getElementById("endInput");
const reverseBtn = document.getElementById("reverseBtn");
const routeBtn = document.getElementById("routeBtn");
const output = document.getElementById("output");

reverseBtn.addEventListener("click", () => {
    const temp = startInput.value;
    startInput.value = endInput.value;
    endInput.value = temp;
});

//Placeholder bhvr already handled by browser and CSS opacity
//Ensure placeholder reappears if text removed

[startInput, endInput].forEach(input => {
    input.addEventListener("focus", () => {
        input.classList.add('has-focus');
    });

    input.addEventListener("blur", () => {
        input.classList.remove('has-focus');
    });
});

routeBtn.addEventListener("click", async () => {
    const start = startInput.value.trim();
    const end = endInput.value.trim();

    if (!start || !end) {
        output.textContent = "Please enter a start location and an end destination.";
        return;
    }

    output.textContent = "Loading route...";

    try {
        const res = await fetch("/process", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ start, end })
        });

        if (!res.ok) throw new Error('Server error: ${res.status}');

        const json = await res.json();
        output.textContent = json.message || "Route calculated.";
    }
    catch (err) {
        output.textContent = "Error: ${err.message}";
        console.error(err);
    }
});

