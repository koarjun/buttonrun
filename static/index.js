function runJobSop1() {
    let job_name = 'job1';
    showLoader();
    fetch('/run_job/job_name=' + job_name)
        .then(response => response.json())
        .then((response) => {
            dismissLoader();
            showMessage(response.data);
            showNotification();
        })
}

function runJobSop2() {
    showLoader();
    fetch('/run_job', { method: 'POST' })
        .then(response => response.json())
        .then((response) => {
            dismissLoader();
            showMessage(response.data);
            showNotification();
        });
}

function showMessage(data) {
    document.querySelector('#message').innerHTML = data;
}

window.onload = function () {
    document.querySelector('#job_sop1').addEventListener('click', runJobSop1);
    document.querySelector('#job_sop2').addEventListener('click', runJobSop2);
    document.querySelector('.bx--toast-notification__close-button').addEventListener('click', dismissNotification);
    dismissNotification();
    dismissLoader();
}

function dismissNotification() {
    hide('.bx--toast-notification');
}

function showNotification() {
    show('.bx--toast-notification');
}

function dismissLoader() {
    hide('.bx--loading-overlay');
}

function showLoader() {
    show('.bx--loading-overlay');
}

function show(selector) {
    document.querySelector(selector).style.visibility = "visible";
}

function hide(selector) {
    document.querySelector(selector).style.visibility = "hidden";
}