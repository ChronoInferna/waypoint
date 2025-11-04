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

[startInput, endInput].forEach((input) => {
  input.addEventListener("focus", () => {
    input.classList.add("has-focus");
  });

  input.addEventListener("blur", () => {
    input.classList.remove("has-focus");
  });
});

routeBtn.addEventListener("click", async () => {
  const start = startInput.value.trim();
  const end = endInput.value.trim();

  if (!start || !end) {
    output.textContent =
      "Please enter a start location and an end destination.";
    return;
  }

  output.textContent = "Loading route...";

  try {
    const res = await fetch("/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ start, end }),
    });

    if (!res.ok) throw new Error(`Server error: ${res.status}`);

    const json = await res.json();
    if (json.message) output.textContent = json.message;
    else {
      output.textContent =
        "Route found using Djikstra's Algorithm:\n\n" +
        json.djikstra.flights.map((airport) => `${airport}`).join("\n") +
        `\nTotal travel time: ${json.djikstra.time} minutes` +
        "\n\n" +
        "Route found using BFS Algorithm:\n\n" +
        json.bfs.flights.map((airport) => `${airport}`).join("\n") +
        `\nTotal travel time: ${json.bfs.time} minutes`;
    }
  } catch (err) {
    output.textContent = `Error: ${err.message}`;
    console.error(err);
  }
});
