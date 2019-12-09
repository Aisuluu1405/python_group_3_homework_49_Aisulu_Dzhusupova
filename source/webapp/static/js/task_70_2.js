function getToken()
{
    $.ajax({
        url: 'http://localhost:8000/api/login/',
        method: 'post',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function (response, status) {localStorage.setItem('apiToken', response.token);},
        error: function (response, status) {console.log(response);}
    });
}
function projectsList() {
    $.ajax({
    url: 'http://localhost:8000/api/projects/',
    method: 'get',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    dataType: 'json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});
}
function issuesList() {
    $.ajax({
    url: 'http://localhost:8000/api/issues/',
    method: 'get',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    dataType: 'json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});
}
function issueProject() {
    $.ajax({
    url: 'http://localhost:8000/api/projects/1',
    method: 'get',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    dataType: 'json',
    success: function(response, status){console.log(response.issues);},
    error: function(response, status){console.log(response);}
});
}
function addIssue() {
    $.ajax({
        url: 'http://localhost:8000/api/issues/',
        headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
        method: 'post',
        data: JSON.stringify({summary: 'Домашка', description: 'Домашнее задание №70 DRF',  status: 1, type: 1, project: 2,
            created_by: 2,  assigned_to: 2}),
        dataType: 'json',
        contentType: 'application/json',
        success: function (response, status) {console.log(response);},
        error: function (response, status) {console.log(response);}
    });
}
function deleteIssue() {
    $.ajax({
    url: 'http://localhost:8000/api/issues/96/',
    method: 'delete',
    headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
    dataType: 'json',
    success: function(response, status){console.log('Ok, issue delete.');},
    error: function(response, status){console.log(response);}
});
}

getToken();
if(localStorage.getItem('apiToken')){
    projectsList();
    issuesList();
    issueProject();
    // addIssue();
    // deleteIssue();
}
else{console.log('Токена нет!')};