(function () {
  function extend(destination, source) {
    for (var key in source) {
      destination[key] = source[key];
    }
  }

  var cupboard = {};

  cupboard.timers = {};

  cupboard.startTimeout = function (time, identifier, action) {
    if (cupboard.timers[identifier]) {
      clearTimeout(cupboard.timers[identifier]);
    }
    cupboard.timers[identifier] = setTimeout(action, time);
  };

  cupboard.cancelTimeout = function (identifier) {
    if (cupboard.timers[identifier]) {
      clearTimeout(cupboard.timers[identifier]);
      delete cupboard.timers[identifier];
    }
  };

  cupboard.startInterval = function (time, identifier, action) {
    if (cupboard.timers[identifier]) {
      clearInterval(cupboard.timers[identifier]);
    }
    cupboard.timers[identifier] = setInterval(action, time);
  };

  cupboard.cancelInterval = function (identifier) {
    if (cupboard.timers[identifier]) {
      clearInterval(cupboard.timers[identifier]);
      delete cupboard.timers[identifier];
    }
  };

  cupboard.extend = extend;

  window.stopExecutionOnTimeout = cupboard;
})();