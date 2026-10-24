
const params = new URLSearchParams(window.location.search);
const level = params.get("level") || "easy";
document.getElementById("level").innerText =
  `Level: ${level.charAt(0).toUpperCase() + level.slice(1)}`;

function loadQuestion() {
  fetch(`/new-question?level=${level}`)
  .then(response => response.json())
  .then (data => 
    {
      document.getElementById("question").innerText = data.question;
      document.getElementById("feedback").innerText = "";
      document.getElementById("answer").value ="";
    })
  .catch(() => {
    document.getElementById("question").innerText = "Failed To Load Question"
  })
}

function submitAnswer() {
  const answerInput = document.getElementById("answer");
  const answer = parseInt(answerInput.value, 10);

  if (isNaN(answer)) {
    document.getElementById("feedback").innerText = "Please enter a valid number";
    return;
  }

  fetch("/check-answer", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ answer: answer }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.correct) {
        document.getElementById("feedback").innerText = "Correct!";
      } else {
        document.getElementById("feedback").innerText = `Incorrect. Correct answer was ${data.correct_answer}.`;
      }  
      document.getElementById("score").innerText = `Score: ${data.score}`;
    })
    .catch(() => {
      document.getElementById("feedback").innerText = "Error submitting answer.";
    });
}