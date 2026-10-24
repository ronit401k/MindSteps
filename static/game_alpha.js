const params = new URLSearchParams(window.location.search);
const alpha_level = params.get("alpha_level") || "easy";
document.getElementById("alpha_level").innerText =
  `Level: ${alpha_level.charAt(0).toUpperCase() + alpha_level.slice(1)}`;

function loadAlphabetQuestion() {
  fetch(`/alphabet-new-question?alpha_level=${alpha_level}`)
    .then(response => response.json())
    .then(data => {
      document.getElementById("question").innerText = data.question;
      document.getElementById("shown-letter").innerText = data.shown;
      document.getElementById("feedback").innerText = "";
    })
    .catch(() => {
      document.getElementById("question").innerText = "Failed to load question.";
    });
}

function submitAlphabetAnswer(answerAlpha) {
  fetch("/alphabet-check-answer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer: answerAlpha }),
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("feedback").innerText =
        data.correct ? "Nice job!" : "Incorrect. Let’s do another one.";
      document.getElementById("score").innerText = `Score: ${data.score}`;

    })
    .catch(() => {
      document.getElementById("feedback").innerText = "Error submitting answer.";
    });
}
