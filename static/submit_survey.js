function count_yes_survey(formId) {
  const form = document.getElementById(formId);
  const YesCount = form.querySelectorAll('input[type="radio"]:checked[value="Yes"]').length;
    
  document.getElementById("Yes-count").textContent = YesCount;
  document.getElementById("result-message").textContent = "Thank you for checking in.";
  const showResourceLink = document.getElementById("resource-link");
  
  if (YesCount > 5) {
    showResourceLink.innerHTML =
      '<a href="/resources">Link to Further Resources</a>';
     document.getElementById("result-message").textContent = "You may consider discussing any changes in memory or thinking with a doctor.";
    
  }
}