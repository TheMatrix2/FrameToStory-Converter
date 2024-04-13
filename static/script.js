// document.getElementById('videoFile').addEventListener('change', function(e) {
//     let fileName = e.target.files[0].name;
//     let nextSibling = e.target.nextElementSibling;
//     nextSibling.innerText = fileName;
// });

function clearChoice(){
    let fileInput = document.getElementById('videoFile');
    fileInput.value = '';
    let fileNameElement = fileInput.nextElementSibling;
    fileNameElement.innerText = 'Choose video file';
}