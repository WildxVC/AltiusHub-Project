document.addEventListener('DOMContentLoaded', function() {
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(profileForm);
            fetch('/users/profile/', {
                method: 'PUT',
                body: formData,
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('token'),
                },
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    const taskForm = document.getElementById('task-form');
    if (taskForm) {
        taskForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(taskForm);
            fetch('/api/tasks/', {
                method: 'POST',
                body: formData,
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('token'),
                },
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // Add the new task to the list
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = searchInput.value;
            fetch(`/api/search/?search=${query}`)
            .then(response => response.json())
            .then(data => {
                const results = data.results;
                const searchResults = document.getElementById('search-results');
                searchResults.innerHTML = '';
                results.forEach(result => {
                    const li = document.createElement('li');
                    li.textContent = result.title;
                    searchResults.appendChild(li);
                });
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});