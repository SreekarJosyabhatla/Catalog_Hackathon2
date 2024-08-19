function addQuestion() {
  const div = document.createElement("div");
  div.className = "form-group question";
  div.innerHTML = `
        <label>Question:</label>
        <input type="text" name="question" class="form-control" required>
        <label>Correct Answer:</label>
        <input type="text" name="correct_answer" class="form-control" required>
    `;
  document.getElementById("questions").appendChild(div);
}
