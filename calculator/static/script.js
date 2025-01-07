function appendToDisplay(value) {
    document.getElementById('display').value += value;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function calculateResult() {
    const display = document.getElementById('display');
    const expression = display.value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ operation: 'calculate', expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result !== undefined) {
            display.value = data.result;
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
