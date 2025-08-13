<DOCTYPE html>
<html>
<head>
  <title>Simple JavaScript Example</title>
</head>
<body>

<h1>Hello!</h1>
<p id="message">Click the button to see a message.</p>

<button onclick="showMessage()">Click Me</button>

<script>
  function showMessage() {
    document.getElementById("message").innerText = "You clicked the button!";
  }
</script>

</body>
</html>
