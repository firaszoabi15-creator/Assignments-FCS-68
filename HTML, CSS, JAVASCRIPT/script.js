function addGreeting() {
        const name = document.getElementById("nameInput").value;
        const div = document.getElementById("greeting");

        if (name === "") {
          div.innerHTML = "<p>No input found!</p>";
        } else {
          div.innerHTML = `<p>Hello, ${name}!</p>`;
        }
      }
      let num = 0;
function addCount() {
    const buttonCounter = document.getElementById("Countbutton");
    num += 1;
    buttonCounter.innerHTML = num;
}