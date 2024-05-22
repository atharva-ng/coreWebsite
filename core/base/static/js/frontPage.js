function animateCounter(elementId, endValue) {
  let counterElement = document.getElementById(elementId);
  let currentValue = 0;
  let increment = endValue < 200 ? 1 : Math.floor(endValue / 100);

  function updateDisplay() {
    if (elementId == "faculty") {
      counterElement.textContent = `${currentValue}`
    } else {
      counterElement.textContent = `${currentValue}K+`;
    }
    if (currentValue < endValue) {
      currentValue += increment;
      requestAnimationFrame(updateDisplay);
    } else {
      if (elementId == "faculty") {
        counterElement.textContent = `${endValue}`;
      } else {
        counterElement.textContent = `${endValue}K+`;
      }
    }
  }

  requestAnimationFrame(updateDisplay);
}

document.addEventListener('DOMContentLoaded', function () {
  var currentTag = document.getElementsByClassName("active")
  currentTag[0].classList.remove("active");
  var element = document.getElementById("id_home");
  element.classList.add('active')
  animateCounter("alumni", 13);
  animateCounter("students", 3);
  animateCounter("faculty", 700);
  animateCounter("patents", 500);
});
