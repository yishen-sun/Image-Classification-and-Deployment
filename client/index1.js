
url = "http://128.110.219.22:5000/api";
// console.log(url);
//   const image_input = document.querySelector("#image-input");
//   var display_image = document.querySelector("#display-image");
//   image_input.addEventListener("change", function () {
//     const reader = new FileReader();
//     reader.readAsDataURL(this.files[0]);
//     reader.onload = function (e) {
//       var xhr = new XMLHttpRequest();
//       xhr.open("POST", url, true);
//       xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
//       form_data = new FormData();
//       form_data.append("base64", this.result);
//       console.log(form_data);
//       xhr.send(form_data);
  
//       xhr.onload = function () {
//         console.log(this.responseText);
//         //var data = JSON.parse(this.responseText);
//         //console.log(data);
//       };
  
//       //console.log(e);
//       //console.log(this.result);
//       display_image.setAttribute("src", this.result);
//     };
//   });
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
  //display_image.setAttribute("src");
}