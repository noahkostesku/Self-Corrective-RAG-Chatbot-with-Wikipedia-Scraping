function getAnswer() {
    //Retrieve the user's question
    var question = document.getElementById('question').value;
    fetch('/', {
        method: 'POST',
        headers: {'Content-Type': 'application/x-www-form-urlencoded'},
        body: 'question=' + encodeURIComponent(question)
    })
    .then(response => response.json())
    .then(data => displayAnswer(data.answer));
}

function displayAnswer(answer) {
    const answerElement = document.getElementById('answer');

    //Clear previous answer in user-interface
    answerElement.innerHTML = ''; 

    //Format chatbot output
    if (Array.isArray(answer)) { 
        const ul = document.createElement('ul');
        answer.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            ul.appendChild(li);
        });
        answerElement.appendChild(ul);
    } else {
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
    //Update with new answer after feedback
    .then(data => displayAnswer(data.answer));
}
//Clear question input, feeback input, and answer display
function resetChat() {
    document.getElementById('question').value = ''; 
    document.getElementById('feedback').value = ''; 
    document.getElementById('answer').innerText = '';
}
