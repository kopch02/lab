function copyToClipboard() {
    var text = document.getElementById("myText").innerText;
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(function() {
      }, function() {
        manualCopy(text);
      });
    } else {
      manualCopy(text);
    }
  }
  function manualCopy(text) {
    var textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    document.execCommand("copy");
    document.body.removeChild(textArea);
  }