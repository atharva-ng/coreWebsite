document.addEventListener("DOMContentLoaded", function () {
  var currentTag = document.getElementsByClassName("active")
  currentTag[0].classList.remove("active");
  var element = document.getElementById("id_aboutUs");
  element.classList.add('active')
});