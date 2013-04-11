// -------------
// Error logging
//
// Depends on: jquery
//
// -------------
function peyote(endpointUrl) {
    window.onerror = function(msg, url, line) {
        var jsonStr = '{"message":"'+msg+'","level":"ERROR","filename":"'+url+'"';

        if(line !== undefined) {
            jsonStr += ',"line":'+line+'}';
        } else {
            jsonStr += '}';
        }

        $.ajax({
            type: 'POST',
            url: "http://localhost:8000/api/v1/peyote/",
            crossDomain: true,
            data: jsonStr,
            processData: false,
            dataType: 'json',
            contentType: "application/json; charset=utf-8"
        });
        console.log("error logged to server");

        return false;
    };
}
