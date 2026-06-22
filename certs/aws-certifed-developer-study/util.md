## Udemy trascript copy

```js
function createCopyButton() {
  let existingButton = document.getElementById("copy-button");
  if (existingButton) {
    existingButton.remove();
  }

  let button = document.createElement("button");
  button.id = "copy-button";
  button.innerText = "복사하기";
  button.style.position = "fixed";
  button.style.top = "10px";
  button.style.left = "10px";
  button.style.zIndex = "1000";
  button.style.padding = "10px 20px";
  button.style.fontSize = "16px";
  button.style.cursor = "pointer";
  document.body.appendChild(button);

  button.addEventListener("click", function () {
    let elements = document.querySelectorAll(
      ".transcript--cue-container--Vuwj6 span"
    );
    console.log(elements);
    if (elements.length === 0) {
      alert("Transcript를 켜주세요!");
      return;
    }
    let transcriptText = "";
    elements.forEach((element) => {
      transcriptText += element.innerText + "\n";
    });

    navigator.clipboard
      .writeText(transcriptText)
      .then(() => {
        alert("복사되었습니다!");
      })
      .catch((err) => {
        console.error("복사 실패:", err);
      });
  });
}

createCopyButton();
```
