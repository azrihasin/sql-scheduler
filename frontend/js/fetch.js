async function fetchdata (url, data, callback){
    await fetch(
        url,
        {
            method: 'post',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json'
            }
        }
    ).then(function(response){
        return response.json();
    }).then(callback);
}

async function fetchfile (url, file, callback){
    await fetch(
        url,
        {
            method: 'post',
            body: file,
            headers: {
                'Content-Type': 'application/pdf'
            }
        }
    ).then(function(response){
        return response.json();
    }).then(callback);
}