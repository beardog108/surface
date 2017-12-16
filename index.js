async function sha256(str) {
    const buf = await crypto.subtle.digest("SHA-256", new TextEncoder("utf-8").encode(str));
    return Array.prototype.map.call(new Uint8Array(buf), x=>(('00'+x.toString(16)).slice(-2))).join('');
  }
  
function generateKey(text, position){
    var buf = new Uint8Array(32); 
    sha256(crypto.getRandomValues(buf)).then(function(stuff){
       if (stuff.indexOf(text) == position){
           console.log(stuff);
       }
    });
}

function httpGet(theUrl) {
    // https://stackoverflow.com/a/4033310
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

document.getElementById('body').onclick = function(e){
    if (e.target.className == 'item'){
        e.target.select();
    }
}

document.getElementById('sites').innerHTML = DOMPurify.sanitize(httpGet('http://127.0.0.1:5000/getsites'));

//text = '1111'
//keyGeneration = setInterval(function(){ generateKey(text, 5)}, 10)
