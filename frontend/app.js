(function () {
  "use strict";

  var mode = "login"; // "login" | "register"

  var form        = document.getElementById("auth-form");
  var title       = document.getElementById("form-title");
  var submitBtn   = document.getElementById("submit-btn");
  var feedback    = document.getElementById("feedback");
  var toggleLink  = document.getElementById("toggle-link");
  var togglePrompt = document.getElementById("toggle-prompt");
  var emailInput  = document.getElementById("email");
  var passInput   = document.getElementById("password");

  function setMode(newMode) {
    mode = newMode;
    feedback.textContent = "";
    feedback.className = "feedback";
    if (mode === "register") {
      title.textContent = "Register";
      submitBtn.textContent = "Register";
      togglePrompt.textContent = "Already have an account?";
      toggleLink.textContent = "Login";
    } else {
      title.textContent = "Login";
      submitBtn.textContent = "Login";
      togglePrompt.textContent = "Don't have an account?";
      toggleLink.textContent = "Register";
    }
  }

  toggleLink.addEventListener("click", function (e) {
    e.preventDefault();
    setMode(mode === "login" ? "register" : "login");
  });

  function showFeedback(message, type) {
    feedback.textContent = message;
    feedback.className = "feedback " + type;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var email = emailInput.value.trim();
    var password = passInput.value;

    if (!email || !password) {
      showFeedback("Please fill in all fields.", "error");
      return;
    }

    var url = mode === "login" ? "/api/login" : "/api/register";
    submitBtn.disabled = true;
    feedback.textContent = "";

    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password })
    })
      .then(function (res) {
        return res.json().then(function (data) {
          return { status: res.status, body: data };
        });
      })
      .then(function (result) {
        if (mode === "login") {
          if (result.status === 200) {
            showFeedback("Login successful!", "success");
          } else {
            showFeedback(result.body.error || "Invalid credentials.", "error");
          }
        } else {
          if (result.status === 201) {
            showFeedback("Registered! You can now log in.", "success");
            setMode("login");
          } else {
            showFeedback(result.body.error || "Registration failed.", "error");
          }
        }
      })
      .catch(function () {
        showFeedback("Network error. Please try again.", "error");
      })
      .finally(function () {
        submitBtn.disabled = false;
      });
  });
})();
