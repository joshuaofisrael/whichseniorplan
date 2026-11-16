(function () {
  var select = document.getElementById("state-picker");
  var button = document.getElementById("state-go");
  function go() {
    if (select && select.value) window.location.href = select.value;
  }
  if (button) button.addEventListener("click", go);
  if (select) select.addEventListener("change", go);
})();
