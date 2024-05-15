$(document).ready(function() {
    $("#loginForm").submit(function(event) {
        event.preventDefault();

        var formData = {
            email: $("#email").val(),
            password: $("#password").val()
        };

        $.ajax({
            type: "POST",
            url: "http://localhost:8000/login/user",
            data: JSON.stringify(formData),
            contentType: "application/json",
            success: function(response) {
                window.location.href = '/chat';
            },
            error: function(xhr, status, error) {
                if (xhr.status === 401) {
                    $("#errorMessage").text(xhr.responseJSON.detail);
                    $("#errorModal").modal("show");
                } else {
                    console.error("Login failed:", error);
                }
            }
        });
    });
});
