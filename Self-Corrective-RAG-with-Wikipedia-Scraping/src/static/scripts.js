function getAnswer() {
    var question = document.getElementById('question').value;
    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'question=' + encodeURIComponent(question)
    })
    .then(response => response.json())
    .then(data => displayAnswer(data.answer)); // Pass answer to display function
}

function displayAnswer(answer) {
    const answerElement = document.getElementById('answer');

    // Clear previous answer
    answerElement.innerHTML = ''; 

    // Example logic to format lists or headers
    if (Array.isArray(answer)) { // If the answer is an array (list)
        const ul = document.createElement('ul');
        answer.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            ul.appendChild(li);
        });
        answerElement.appendChild(ul);
    } else { // If it's just a string, display it as a paragraph
        const p = document.createElement('p');
        p.textContent = answer;
        answerElement.appendChild(p);
    }
}

function provideFeedback() {
    var question = document.getElementById('question').value;
    var feedback = document.getElementById('feedback').value;

    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'question=' + encodeURIComponent(question) + '&feedback=' + encodeURIComponent(feedback)
    })
    .then(response => response.json())
    .then(data => displayAnswer(data.answer)); // Update with new answer after feedback
}

function resetChat() {
    document.getElementById('question').value = ''; // Clear question input
    document.getElementById('feedback').value = ''; // Clear feedback input
    document.getElementById('answer').innerText = ''; // Clear answer display
}
