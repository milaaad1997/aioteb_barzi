
function diagnose () {
  document.getElementById('diagnose').addEventListener('click', function() {
    fetch('/diagnose', {method: 'POST'})
    .then(response => response.text())
    .then(data => {
        document.getElementById('results').innerHTML = data;
    });
});
}

function reload () {
  document.getElementById('return').addEventListener('click', function() {
    location.reload();
});
}


// function diagnose () {
//     const data = null;

//       const xhr = new XMLHttpRequest ();

//       xhr.addEventListener('readystatechange' , function () {

//       if (this.readyState === this.DONE) { 
          

       



//       }
// })
// xhr.open('POST', 'http://127.0.0.1:5000/start');



// xhr.send(data);
// console.log(xhr);
// }
