
url = "http://128.110.219.22:5000/api";
//url = "http://localhost:5000/api";
const image_input = document.querySelector("#image-input");
var display_image = document.querySelector("#display-image");
var result = document.querySelector("#result");
image_input.addEventListener("change", function () {
  const reader = new FileReader();
  reader.readAsDataURL(this.files[0]);
  reader.onload = function (e) {
    display_image.setAttribute("src", this.result);
  };
});
function uploadFile(form) {
  const formData = new FormData(form);
  var oOutput = document.getElementById("static_file_response");
  var oReq = new XMLHttpRequest();
  oReq.open("POST", url, true);
  oReq.onload = function (oEvent) {
    if (oReq.status == 200) {
      oOutput.innerHTML = "Uploaded!";
      console.log(oReq.response);
    } else {
      oOutput.innerHTML =
        "Error occurred when trying to upload your file.<br />";
    }
  };
  oOutput.innerHTML = "Sending file!";
  console.log("Sending file!");
  oReq.send(formData);
  oReq.onload = function () {
    result.innerHTML = "Result is " + this.responseText;   
  };

}