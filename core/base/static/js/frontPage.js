function animateCounter(elementId, endValue) {
  let counterElement = document.getElementById(elementId);
  let currentValue = 0;
  let increment = endValue < 200 ? 1 : Math.floor(endValue / 100);

  function updateDisplay() {
    if (elementId == "CEO") {
      counterElement.textContent = `${currentValue}`
    } else {
      counterElement.textContent = `${currentValue}+`;
    }
    if (currentValue < endValue) {
      currentValue += increment;
      requestAnimationFrame(updateDisplay);
    } else {
      if (elementId == "CEO") {
        counterElement.textContent = `${endValue}+`;
      } else {
        counterElement.textContent = `${endValue}+`;
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
  animateCounter("alumni", 16000);
  animateCounter("students", 3000);
  animateCounter("CEO", 7400);
});
