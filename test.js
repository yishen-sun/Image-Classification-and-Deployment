url = "http://localhost:8000/api";
var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
form_data = new FormData();
form_data.append("base64", "this.result");
xhr.send(form_data);

xhr.onload = function () {
console.log(this.responseText);
//var data = JSON.parse(this.responseText);
//console.log(data);
};
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
//       xhr.send(form_data);
  
//       xhr.onload = function () {
//         console.log(this.responseText);
//         //var data = JSON.parse(this.responseText);
//         //console.log(data);
//       };
  
//       console.log(e);
//       console.log(this.result);
//       display_image.setAttribute("src", this.result);
//     };
//   });